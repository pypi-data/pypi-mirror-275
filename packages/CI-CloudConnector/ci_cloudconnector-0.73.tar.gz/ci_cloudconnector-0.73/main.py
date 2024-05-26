import logic, datetime
from datetime import datetime
import subprocess
import sys
import importlib



upgradeCounter = 0
serverVersion = ""
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


def reloadLC():
    try:
        logic.ci_print("! About to reload", "ERROR")
        logic.reboot()
        # reload(CI_LC_BL)
        # CI_LC_BL.initConfig()
    except Exception as inst:
        logic.handleError("reloadLC::Error ", inst)
        # print "Error reload " + str(inst)
        # logging.warning('Error in reload :: ' + str(inst))



def update_and_run(script_path, package_name, package_version):
    try:

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


    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")



def upgradeLC(ver="", currentVer=""):
    try:
        logic.ci_print("upgradeLC version: " + ver)

        update_and_run("main.py", "CI_CloudConnector", ver);

    except Exception as inst:
        logic.handleError("upgradeLC::Error ", inst)
        # print "Error upgrade " + str(inst)
        # logging.warning('Error in upgrade :: ' + str(inst))


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

            # fileName = "WatchDog_" + datetime.now().strftime("%Y%m%d-%H%M%S")+ '.txt'
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
    except Exception as inst:
        logic.ci_print("MainLoopTimer::Error MainLoop " + str(inst), "ERROR")

    if threadTimer:
        threadTimer.start()
    else:
        logic.ci_print("MainLoopTimer::threadTimer not found!", "ERROR")
        print("threadTimer not found!")
        threadTimer = RepeatedTimer(5, MainLoopTimer)
        logic.ci_print("MainLoopTimer::Starting threadTimer again!", "ERROR")


def MainLoop():
    global serverVersion
    global upgradeCounter

    try:
        # get version and update if needed
        logic.getCloudVersion()
        localVer = str(logic.getLocalVersion())
        updateToVer = str(logic.getServerSugestedVersion())
        # to prevent upgrading to much in case of a problem we count upgrade attempts and stop when its too big, but if the version changes we try again
        if serverVersion != updateToVer:
            serverVersion = updateToVer
            upgradeCounter = 0

        logic.ci_print("local ver=" + localVer)
        logic.ci_print("server ver= " + updateToVer)

        if str(updateToVer) == "None":
            updateToVer = ""
        if (
            bool(updateToVer != "")
            & bool(updateToVer != localVer)
            & bool(upgradeCounter < 10)
        ):
            upgradeCounter = upgradeCounter + 1
            logic.ci_print(
                "Local Version is different than server suggested version, start auto upgrade from:"
                + localVer
                + " To:"
                + updateToVer
                + " Upgrade count:"
                + str(upgradeCounter)
            )
            upgradeLC(updateToVer, localVer)
            reloadLC()

        # Get Values and send to cloud
        logic.Main()
    except Exception as inst:
        logic.ci_print("MainLoop::Error " + str(inst), "ERROR")


def StartMainLoop():

    global threadTimer
    try:
        logic.ci_print("CI_CloudConnector Started")
        logic.updateAliveFile("Started")


        threadTimer = RepeatedTimer(5, MainLoopTimer)#5
        watchDogThreadTimer = RepeatedTimer(30, watchDogLoop)#30
        # threadTimer = RepeatedTimer(5, test)
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
    print(
        "CI_CloudConnector.py getCloudVersion : check server suggected version and time"
    )
    print(
        "CI_CloudConnector.py getCloudTags  : Get Tags defenition from Cloud and save into file"
    )
    print("CI_CloudConnector.py LocalDefTagsFiles : Show the tags saved in file")
    print("CI_CloudConnector.py readModBusTags : Read Tags Fom Modbus and save to file")
    print(
        "CI_CloudConnector.py readEtherNetIP_Tags : Read Tags Fom EtehernatIP and save to file"
    )
    print(
        "CI_CloudConnector.py handleAllValuesFiles : Send Values from all files to cloud"
    )
    print(
        "CI_CloudConnector.py TestMainLoopOnce : test main loop functionality one time"
    )
    print("CI_CloudConnector.py Test : Test Components")
    print("==============================================")


def args(argv):
    # print 'Argument List:', str(argv)
    # print 'Argument List:', str(len(argv))
    # if (len(sys.argv)==1):
    #    CI_LC_BL.MainLoopStart()
    if len(argv) > 1 and argv[1] == "help":
        showHelp()

    if len(argv) > 1 and argv[1] == "Start":
        StartMainLoop()

    if len(argv) > 1 and argv[1] == "Config":
        logic.initConfig(True)

    if len(argv) > 1 and argv[1] == "Test":
        logic.Test()

    if len(argv) > 1 and argv[1] == "getCloudTags":
        token = ""
        token = logic.getCloudToken()
        logic.getCloudTags(token)

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
        token = logic.getCloudToken()
        logic.handleAllValuesFiles(token)

    if len(argv) > 1 and argv[1] == "TestMainLoopOnce":
        MainLoop()

    if len(argv) > 1 and argv[1] == "upgradeLC":
        upgradeLC()

    if len(argv) > 1 and argv[1] == "getCloudVersion":
        logic.getCloudVersion()


def menu(option="help"):
    args(["", option])


# handle
# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)
# print 'Argument List:', str(sys.argv[1])

# MainLoop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logic.createLibIfMissing()
    logic.initConfig()
    args(sys.argv)
