
import logic
import sys
import subprocess
import shutil
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from threading import Timer
from datetime import datetime

upgrade_counter = 0
server_version = ""
repeating_timer = None

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


def MainLoopTimer():
    print(f"MainLoopTimer: {str(datetime.now())}")
    global repeating_timer

    if repeating_timer:
        repeating_timer.stop()

    try:
        MainLoop()
    except Exception as e:
        logic.ci_print(f"MainLoopTimer::Error: {e}", "ERROR")

    if repeating_timer:
        repeating_timer.start()
    else:
        repeating_timer = RepeatedTimer(5, MainLoopTimer)


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

        logic.ci_print("local_ver: " + local_ver)
        logic.ci_print("update_to_ver: " + update_to_ver)

        if str(update_to_ver) == "None":
            update_to_ver = ""

        if (bool(update_to_ver != "") & bool(update_to_ver != local_ver) & bool(upgrade_counter < 10)):
            upgrade_counter += 1
            logic.ci_print(
                f"Starting auto upgrade from: {local_ver} to: {update_to_ver}, Upgrade count: {upgrade_counter}")
            upgrade_version(update_to_ver, local_ver)

        logic.Main()
    except Exception as inst:
        logic.ci_print(f"MainLoop::Error {inst}", "ERROR")


def StartMainLoop():
    global repeating_timer
    try:
        repeating_timer = RepeatedTimer(5, MainLoopTimer)
    except Exception as inst:
        logic.ci_print("StartMainLoop::Error " + str(inst))


def args(argv):
    if len(argv) > 1 and argv[1] == "Start":
        StartMainLoop()


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
    args(sys.argv)
    #args([0, 'Start'])
    monitor_main_file("logic.py")