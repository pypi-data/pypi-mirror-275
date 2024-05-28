import logic, datetime
from datetime import datetime
import subprocess
import sys
import importlib
import subprocess
import shutil
import os

upgrade_counter = 0
server_version = ""
threadTimer = None
watchDogThreadTimer = None

from threading import Timer

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


def reload_lc():
    try:
        logic.ci_print("Reloading LC...", "ERROR")
        logic.reboot()

    except Exception as ex:
        logic.handle_error("Error in reload_lc: ", ex)


def update_and_run(script_path, package_name, package_version):
    try:
        print(f'package_version: {package_version}')

        if package_version == '':
            subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--upgrade", f"{package_name}"])
        else:
            # Install or upgrade the package
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "--force-reinstall", f"{package_name}=={package_version}"])

        # Locate the installed package
        package_info = subprocess.check_output([sys.executable, "-m", "pip", "show", package_name]).decode()
        package_location = None
        for line in package_info.splitlines():
            if line.startswith("Location:"):
                package_location = line.split(": ")[1]
                break

        if package_location is None:
            print("Could not determine the package location.")
            return

        # Construct the path to the installed package
        installed_package_path = package_location
        destination_path = os.getcwd()

        logic_source = os.path.join(installed_package_path, "logic.py")
        main_source = os.path.join(installed_package_path, "main.py")

        if not os.path.isfile(logic_source) or not os.path.isfile(main_source):
            print(f"logic.py or main.py not found in {installed_package_path}.")
            return

        # Copy files to the destination
        shutil.copy(logic_source, destination_path)
        shutil.copy(main_source, destination_path)

        print(f"Copied logic.py and main.py to {destination_path}")


    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


def upgrade_version(new_version="", current_version=""):
    try:
        logic.ci_print("Upgrade version: " + new_version)
        update_and_run("main.py", "CI_CloudConnector", new_version)

    except Exception as ex:
        logic.handle_error("Upgrade version Error: ", ex)


def watchDogLoop():
    global threadTimer
    try:
        print("watchDogLoop::Start")
        logic.ci_print("watchDogLoop::Start", "DEBUG")
        ret = logic.checkIsAlive()
        isAlive = ret["isAlive"]
        diff = ret["diff"]
        msg = ""
        if isAlive == False:
            print("watchDogLoop::MainLoop Not Working, restarting ") + str(diff)
            logic.ci_print(
                "watchDogLoop::MainLoop Not Working , restarting", "CRITICAL"
            )
            print("watchDogLoop::threadTimer = ") + str(threadTimer)
            logic.ci_print(
                "watchDogLoop::threadTimer = " + str(threadTimer), "CRITICAL"
            )
            if threadTimer:
                if diff < 250:
                    logic.ci_print(
                        "watchDogLoop::Found threadTimer try start again, <250 ",
                        "CRITICAL",
                    )
                    threadTimer.stop()
                    threadTimer = RepeatedTimer(5, MainLoopTimer)
                    msg = "watchDogLoop::Found threadTimer try start again, <250 "
                if diff > 250 and diff < 900:
                    print("watchDogLoop:: restarting timer")
                    logic.ci_print(
                        "watchDogLoop::Found threadTimer but its not working, restarting timer ",
                        "CRITICAL",
                    )
                    threadTimer.stop()
                    threadTimer = RepeatedTimer(5, MainLoopTimer)
                    msg = "watchDogLoop::Found threadTimer but its not working, restarting timer "
                if diff > 900:
                    logic.ci_print(
                        "watchDogLoop::Found threadTimer but its not working more then 900 sec, reboot machine ",
                        "CRITICAL",
                    )
                    logic.reboot()
                    msg = "watchDogLoop::Found threadTimer but its not working more then 900 sec, reboot machine "

                logic.ci_print(
                    "watchDogLoop::threadTimer.is_running = "
                    + str(threadTimer.is_running),
                    "CRITICAL",
                )
            else:
                print("watchDogLoop:: No thread Timer")
                if diff > 250 and diff < 900:
                    print("watchDogLoop:: restarting timer")
                    logic.ci_print(
                        "watchDogLoop::No timer , restarting timer ", "CRITICAL"
                    )
                    threadTimer = RepeatedTimer(5, MainLoopTimer)
                    msg = "watchDogLoop::No timer , restarting timer "
                    # CI_LC_BL.reboot()
                if diff > 900:
                    logic.ci_print(
                        "watchDogLoop::threadTimer not found over 900, reboot machine ",
                        "CRITICAL",
                    )
                    logic.reboot()
                    msg = (
                        "watchDogLoop::threadTimer not found over 900, reboot machine "
                    )

            fileName = "WatchDog.log"
            f = open(fileName, "a")
            text = (
                str(datetime.now())
                + " , offline time = "
                + str(diff)
                + " sec "
                + msg
                + "\n"
            )
            f.write(text)
            # json.dump(str(datetime.now()), f)
            f.close()
            # CI_LC_BL.reboot()
    except Exception as inst:
        logic.ci_print("watchDogLoop::Error " + str(inst), "ERROR")


def MainLoopTimer():
    global threadTimer

    if threadTimer:
        threadTimer.stop()

    try:
        MainLoop()
    except Exception as e:
        logic.ci_print(f"MainLoopTimer::Error in main_loop: {e}", "ERROR")

    if threadTimer:
        threadTimer.start()
    else:
        logic.ci_print("MainLoopTimer::thread_timer not found!", "ERROR")
        threadTimer = RepeatedTimer(5, MainLoopTimer)
        logic.ci_print("MainLoopTimer::Started thread_timer again!", "INFO")


def MainLoop():
    global server_version
    global upgrade_counter

    try:
        # Get version and update if needed
        logic.get_cloud_version()
        local_ver = str(logic.getLocalVersion())
        update_to_ver = str(logic.getServerSugestedVersion())

        # To prevent upgrading too much in case of a problem, count upgrade attempts and stop when it's too big.
        # If the version changes, try again.
        if server_version != update_to_ver:
            server_version = update_to_ver
            upgrade_counter = 0

        logic.ci_print("Local version = " + local_ver)
        logic.ci_print("Server version = " + update_to_ver)

        if str(update_to_ver) == "None":
            update_to_ver = ""

        if (bool(update_to_ver != "") & bool(update_to_ver != local_ver) & bool(upgrade_counter < 10)):
            upgrade_counter += 1
            logic.ci_print(
                f"Starting auto upgrade from: {local_ver} to: {update_to_ver}, Upgrade count: {upgrade_counter}")
            upgrade_version(update_to_ver, local_ver)
            reload_lc()

        logic.Main()
    except Exception as inst:
        logic.ci_print(f"MainLoop::Error {inst}", "ERROR")


def StartMainLoop():
    global threadTimer
    try:
        logic.ci_print("CI_CloudConnector Started")
        logic.updateAliveFile("Started")

        threadTimer = RepeatedTimer(5, MainLoopTimer)
        watchDogThreadTimer = RepeatedTimer(30, watchDogLoop)
    except Exception as inst:
        logic.ci_print("StartMainLoop::Error " + str(inst))


def showHelp():
    print("==============================================")
    print("CI_CloudConnector Version: " + logic.getLocalVersion())
    print("CI_CloudConnector.py :Start application")
    print("CI_CloudConnector.py help   : display command line help")
    print("CI_CloudConnector.py Start  : Start Main Loop")
    print("CI_CloudConnector.py Config : UpdateConfig defenitions")
    print("==============================================")
    print("CI_CloudConnector.py getCloudVersion : check server suggected version and time")
    print("CI_CloudConnector.py getCloudTags  : Get Tags defenition from Cloud and save into file")
    print("CI_CloudConnector.py LocalDefTagsFiles : Show the tags saved in file")
    print("CI_CloudConnector.py readModBusTags : Read Tags Fom Modbus and save to file")
    print("CI_CloudConnector.py readEtherNetIP_Tags : Read Tags Fom EtehernatIP and save to file")
    print("CI_CloudConnector.py handleAllValuesFiles : Send Values from all files to cloud")
    print("CI_CloudConnector.py TestMainLoopOnce : test main loop functionality one time")
    print("CI_CloudConnector.py Test : Test Components")
    print("==============================================")


def args(argv):
    if len(argv) > 1 and argv[1] == "help":
        showHelp()

    if len(argv) > 1 and argv[1] == "Start":
        StartMainLoop()

    if len(argv) > 1 and argv[1] == "Config":
        logic.initialize_config(True)

    if len(argv) > 1 and argv[1] == "Test":
        logic.Test()

    if len(argv) > 1 and argv[1] == "getCloudTags":
        token = ""
        token = logic.get_cloud_token()
        logic.get_cloud_tags(token)

    if len(argv) > 1 and argv[1] == "LocalDefTagsFiles":
        tagsDef = logic.getTagsDefenitionFromFile()
        logic.printTags(tagsDef)

    if len(argv) > 1 and argv[1] == "readModBusTags":
        tagsDef = logic.getTagsDefenitionFromFile()
        # printTags(tagsDef)
        values = logic.readModBusTags(tagsDef)
        logic.printTagValues(values)
        logic.saveValuesToFile(values, "")

    if len(argv) > 1 and argv[1] == "readEtherNetIP_Tags":
        tagsDef = logic.getTagsDefenitionFromFile()
        logic.printTags(tagsDef)
        values = logic.readEtherNetIP_Tags(tagsDef)
        logic.printTagValues(values)
        logic.saveValuesToFile(values, "")

    if len(argv) > 1 and argv[1] == "handleAllValuesFiles":
        token = ""
        token = logic.get_cloud_token()
        logic.handleAllValuesFiles(token)

    if len(argv) > 1 and argv[1] == "TestMainLoopOnce":
        MainLoop()

    if len(argv) > 1 and argv[1] == "upgradeLC":
        upgrade_version()

    if len(argv) > 1 and argv[1] == "getCloudVersion":
        logic.get_cloud_version()



import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MainFileChangeHandler(FileSystemEventHandler):
    def __init__(self, main_file):
        super().__init__()
        self.main_file = main_file

    def on_modified(self, event):
        if event.src_path.endswith(self.main_file):
            print("Main file has been modified. Restarting script...")
            os.execv(sys.executable, ['python'] + sys.argv)




def monitor_main_file(main_file):
    event_handler = MainFileChangeHandler(main_file)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def init():
    logic.create_directories_if_missing()
    logic.initialize_config()


if __name__ == '__main__':
    init()
    #args(sys.argv)
    args([0, 'Start'])
    monitor_main_file("logic.py")