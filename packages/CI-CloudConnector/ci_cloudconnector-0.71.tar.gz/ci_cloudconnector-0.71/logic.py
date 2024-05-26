import logging, time, datetime, sys, os, socket, configparser, random, tzlocal, glob, fnmatch
from cpppo.server.enip import address, client
from datetime import datetime
import platform


VER = "0.60"
test = 'yochai'
TagsDefenitionFileName = "TagsDefenition.txt"
TagsValuesFileName = "[NEW]TagsValues"
TagsValueDir = "TagValues"
HomeDir = "CI_LC"
GetTagsFromServerMinRateSeconds = 10
GetCloudVersionFromServerMinRateSeconds = 10
g_VerifySSL = False  # True = do not allow un verified connection , False = Allow

# config
cfg_serverAddress = ""
cfg_userName = ""
cfg_passWord = ""
cfg_maxFiles = ""
cfg_LogLevel = ""

sugestedUpdateVersion = ""
configFile = "config.ini"
ScanRateLastRead = {}
currentToken = ""
g_connectorTypeName = ""
g_lastGetTagsFromServer = None
g_lastGetCloudVersionFromServer = None
g_app_log = None

def enum(**enums):
    return type("Enum", (), enums)

TagStatus = enum(Invalid=10, Valid=20)

def initLog(loglevel=""):

    global VER
    global g_app_log
    try:
        if g_app_log:
            return

        myLevel = logging.WARNING
        if loglevel == "DEBUG":
            myLevel = logging.DEBUG
        if loglevel == "INFO":
            myLevel = logging.INFO
        if loglevel == "ERROR":
            myLevel = logging.ERROR

        # logging.basicConfig(filename='CI_CloudConnector.log',level=myLevel , format='%(asctime)s %(message)s')
        # logger = logging.getLogger()
        # logger.setLevel(myLevel)

        from logging.handlers import RotatingFileHandler

        log_formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s"
        )
        logFile = "CI_CloudConnector.log"
        my_handler = RotatingFileHandler(
            logFile,
            mode="a",
            maxBytes=5 * 1024 * 1024,
            backupCount=7,
            encoding=None,
            delay=0,
        )
        my_handler.setFormatter(log_formatter)
        # my_handler.setLevel(myLevel)

        app_log = logging.getLogger("root")
        app_log.setLevel(myLevel)

        app_log.addHandler(my_handler)
        my_handler.doRollover()

        app_log.critical("===============================")
        app_log.critical("CI_CloudConnector Log Init ::" + VER)
        g_app_log = app_log
    except Exception as ex:
        print("Error in initLog " +  str(ex))


# ============================
def readLastRowsFromLog(maxNumberOfRows=10):
    logFile = "CI_CloudConnector.log"
    ans = []
    i = maxNumberOfRows
    for line in reversed(open(logFile, "r").readlines()):
        # print line.rstrip()
        ans.append(line.rstrip())
        i = i - 1
        if i <= 0:
            return ans
    return ans


# ============================
def setLogLevel(lvl):
    try:
        if str(lvl) in ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"]:
            lvl = logging.getLevelName(str(lvl))

        # print 'level=' + str(lvl)
        if g_app_log:
            g_app_log.critical("Set Log Level to " + logging.getLevelName(lvl))
            g_app_log.setLevel(lvl)
    except Exception as inst:
        print("Error in setLogLevel", inst)


# ============================
def ci_print(msg, level=""):
    global g_app_log
    try:
        if level == "DEBUG":
            g_app_log.debug(msg)
        elif level == "INFO":
            g_app_log.info(msg)
        elif level == "ERROR":
            g_app_log.error(msg)
        else:
            g_app_log.warning(msg)

        # print(level+"::"+msg)
    except Exception as inst:
        g_app_log.warning("Main Exception :: " + inst)


# ============================
def SendLogToServer(log):

    try:
        print("send ::") + log
        ret = addCloudConnectorLog(log, datetime.now)
    except:
        return



# ============================
def handleError(message, err):
    try:
        err_desc = str(err)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        srtMsg = (
            message
            + " , "
            + str(err_desc)
            + " , "
            + str(exc_type)
            + " , "
            + str(fname)
            + " , "
            + str(exc_tb.tb_lineno)
        )
        # print(message, err_desc, exc_type, fname, exc_tb.tb_lineno)
        ci_print(srtMsg, "ERROR")
    except Exception as errIgnore:
        ci_print("Error in handleError " + str(errIgnore), "ERROR")



# ============================
def updateAliveFile(timeStamp=None, pid=None):

    ret = False
    try:
        fileName = "/" + HomeDir + "/lc_pid.txt"
        # write tags to file
        data = {}
        if pid == None:
            pid = os.getpid()
        if timeStamp == None:
            timeStamp = str(datetime.now())

        data["pid"] = pid
        data["now"] = timeStamp
        f = open(fileName, "w")
        json.dump(data, f)
        f.close()
        ret = True
    except Exception as inst:
        handleError("Error in updateAliveFile !! ", inst)

    return ret


# ============================
def getAliveFile():

    ret = None
    try:
        fileName = "/" + HomeDir + "/lc_pid.txt"
        # read alive file
        f = open(fileName, "r")
        ret = json.load(f)
        # print 'getAliveFile file=' + str(ret)
    except Exception as inst:
        handleError("Error in getAliveFile", inst)
    return ret


# ============================
def checkIsAlive():

    ret = {}
    ret["isAlive"] = False
    isAliveTimeOutSeconds = 300
    try:
        ans = getAliveFile()
        pid = ans["pid"]
        lastTimeStampStr = ans["now"]

        if lastTimeStampStr == "Started":
            # in case the machine was restarted
            ret["isAlive"] = False
            return ret

        # print 'lastTimeStampStr ' +lastTimeStampStr
        lastTimeStamp = datetime.strptime(lastTimeStampStr, "%Y-%m-%d %H:%M:%S.%f")
        now = datetime.now()
        diff = (now - lastTimeStamp).total_seconds()
        ret["diff"] = diff
        # print 'Diff = ' + str(diff)
        if diff <= isAliveTimeOutSeconds:
            ret["isAlive"] = True

    except Exception as inst:
        # print 'error in checkIsAlive ' + str(inst)
        handleError("Error in checkIsAlive", inst)
    return ret



# ============================
def initConfig(overwrite=False):

    global cfg_serverAddress
    global cfg_userName
    global cfg_passWord
    global cfg_maxFiles
    global cfg_LogLevel

    try:
        filePath = "/" + HomeDir + "/" + configFile

        strLogLevels = " , other options (DEBUG , INFO , WARNING , ERROR)"

        if os.path.exists(filePath) and not overwrite:

            config = configparser.ConfigParser()
            config.read(filePath)

            cfg_serverAddress = config.get("Server", "Address")
            cfg_userName = config.get("Server", "username")
            cfg_passWord = config.get("Server", "password")
            cfg_maxFiles = config.get("Server", "maxFiles")
            cfg_LogLevel = config.get("Logging", "Level", fallback=cfg_LogLevel)

            initLog(cfg_LogLevel)

            ci_print(f"serverAddress: {cfg_serverAddress}", "INFO")
            ci_print(f"userName: {cfg_userName}", "INFO")
            ci_print(f"password: {cfg_passWord}", "INFO")
            ci_print(f"maxFiles: {cfg_maxFiles}", "INFO")
            ci_print(f"Logging Level: {cfg_LogLevel} {strLogLevels}", "INFO")

        else:
            ci_print(f"Config not found or overwrite is True, creating new one in {filePath}", "INFO")
            config = configparser.ConfigParser()
            config.add_section("Server")
            config.add_section("Logging")

            def get_input(prompt, current_value):
                value = input(prompt + f" (Currently: {current_value}): ")
                return value if value else current_value

            cfg_serverAddress = get_input("Enter Server Address (e.g., https://localhost:63483)", cfg_serverAddress)
            cfg_userName = get_input("Enter new user name", cfg_userName)
            cfg_passWord = get_input("Enter password", cfg_passWord)
            cfg_maxFiles = get_input("Enter Max Files", cfg_maxFiles)
            cfg_LogLevel = get_input(f"Enter Logging Level {strLogLevels}", cfg_LogLevel)

            config.set("Server", "Address", cfg_serverAddress)
            config.set("Server", "username", cfg_userName)
            config.set("Server", "password", cfg_passWord)
            config.set("Server", "maxFiles", cfg_maxFiles)
            config.set("Logging", "Level", cfg_LogLevel)

            with open(filePath, "w") as configfile:
                config.write(configfile)
                ci_print("Config settings updated.", "INFO")

            initConfig()  # Reload the config after updating

    except Exception as inst:
        handleError("Error in initConfig", inst)


# ============================
def reboot():

    try:
        ci_print("About to reboot machine!!", "CRITICAL")

        if platform.system() == "Windows":
            print("reboot NO NEED", "INFO")
            #subprocess.run(["shutdown", "/r", "/t", "0"], check=True)
        else:
            print("reboot NO NEED", "INFO")
            #os.system("sudo reboot")
    except Exception as inst:
        handleError("Error in reboot", inst)


# ============================


# Cloud Functions
# ============================
import requests
import json

cfg_serverAddress = "your_server_address"
g_VerifySSL = True
currentToken = ""
cfg_userName = "your_username"
cfg_passWord = "your_password"


def getCloudToken():

    global cfg_serverAddress
    global g_VerifySSL
    global currentToken

    if currentToken:
        return currentToken

    url = f"{cfg_serverAddress}/api/CloudConnector/Token"

    try:
        response = requests.post(
            url,
            data={
                "grant_type": "password",
                "username": cfg_userName,
                "password": cfg_passWord,
            },
            headers={
                "User-Agent": "python",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            verify=g_VerifySSL,
        )

        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.text

        jsonData = json.loads(data)
        token = jsonData.get("access_token", "")

        if token:
            currentToken = token

    except requests.exceptions.RequestException as e:
        handleError("Error getting Token", e)
        token = ""
    except json.JSONDecodeError as e:
        handleError("Error decoding token response", e)
        token = ""
    except KeyError as e:
        handleError("Token not found in response", e)
        token = ""

    return token


# ============================
# make http request to cloud if fails set currentToken='' so it will be initialized next time
# ============================
def ciRequest(url, data, postGet="get", method="", token=""):
    print("start ciRequest " + method)
    ans = {}
    ans["isOK"] = False
    global currentToken
    ansIsSucessful = False
    try:
        if token == "":
            print("Skipping " + method + " - no Token")
            return ""
        else:
            if postGet == "post":
                response = requests.post(
                    url,
                    data,
                    headers={
                        "Content-Type": "application/json",
                        "Accept": "text/plain",
                        "Authorization": "bearer %s" % token,
                    },
                    verify=g_VerifySSL,
                )
            else:
                response = requests.get(
                    url,
                    data=None,
                    headers={"Authorization": "bearer %s" % token},
                    verify=g_VerifySSL,
                )
            print("response=" + str(response), "DEBUG")
            if response.status_code == 403:
                currentToken = ""
            ansIsSucessful = True
    except Exception as err:
        handleError("Error in ciRequest " + method, err)
        currentToken = ""
        ansIsSucessful = False

    ans["isOK"] = ansIsSucessful
    ans["response"] = response
    return ans



# ============================
def setClock(newUtcDate):

    # strTime = '19/12/2016 13:53:55 +02:00'
    # unixTime = '2006-08-07 12:34:56'
    # newDate = unixTime
    # newDate = strTime
    try:
        if newUtcDate == "":
            return

        serverUtcTime = datetime.strptime(newUtcDate, "%Y-%m-%d %H:%M:%S")
        # print 'serverUtcTime=' + str(serverUtcTime)
        utcNow = datetime.utcnow()
        diff = (utcNow - serverUtcTime).total_seconds()
        # print 'differencr from now=' + str(diff)
        if abs(diff) > 3:
            ci_print(
                "setting new system time to "
                + str(serverUtcTime)
                + "(UTC) ,Currently: "
                + str(utcNow)
                + "(UTC)", "INFO"
            )
            set_system_time(newUtcDate)
            now = datetime.now()
            ci_print("New Local Time is " + str(now), "INFO")

    except Exception as inst:
        handleError("Error in setClock ", inst)


def set_system_time(new_utc_date):
    try:
        if new_utc_date == '':
            return

        if platform.system() == "Windows":
            print("set_system_time NO NEED FOR Windows", "INFO")
            #command = f"powershell -Command \"Set-Date -Date '{new_utc_date}'\""
            #subprocess.run(command, shell=True, check=True)
        else:
            # Command to set system time in Linux
            os.system('sudo date --set="%s"' % new_utc_date + "+00:00")

        ci_print(f"System time set to {new_utc_date}", "INFO")
    except Exception as inst:
        handleError("Error in set_system_time", inst)

# ============================
def getCloudVersion():

    global GetCloudVersionFromServerMinRateSeconds
    global g_lastGetCloudVersionFromServer
    global currentToken
    global VER

    if currentToken == "":
        currentToken = getCloudToken()
    token = currentToken
    # initConfig()
    # token = getCloudToken()
    global sugestedUpdateVersion

    tags = None
    try:
        now = datetime.now()
        getVersionTimePass = 0
        if g_lastGetCloudVersionFromServer:
            getVersionTimePass = (now - g_lastGetCloudVersionFromServer).total_seconds()

        ci_print(
            "Last Get version from server was "
            + str(getVersionTimePass)
            + " seconds ago , getVersionRate="
            + str(GetTagsFromServerMinRateSeconds), "INFO"
        )
        if (
            getVersionTimePass == 0
            or getVersionTimePass > GetCloudVersionFromServerMinRateSeconds
        ):
            # print "update pid file for watchdog"
            # do after clock settings because some times the machine loads with old clock and trigger watchdog
            updateAliveFile()

            # print "handleNewRequests"
            handleNewRequests()

            # print 'getting version from server'
            g_lastGetCloudVersionFromServer = datetime.now()
            IpAddress = socket.gethostbyname(socket.gethostname())
            url = (
                cfg_serverAddress
                + "/api/CloudConnector/GetVersion/?version="
                + VER
                + "&IpAddress="
                + IpAddress
            )

            ret = ciRequest(url, None, "get", "getCloudVersion", token)
            response = ret["response"]
            if ret["isOK"] == False:
                return ""

            ci_print("gettags response=" + response.text, "INFO")
            ans = json.loads(response.text)
            updateToVersion = ans[0]
            serverTime = ans[1]
            setClock(serverTime)

            sugestedUpdateVersion = updateToVersion
            if bool(updateToVersion != "") & bool(updateToVersion != VER):
                ci_print(
                    "! > Local Version : "
                    + str(VER)
                    + " But Server suggest Other Version : "
                    + str(updateToVersion), "INFO"
                )

                # printTags(tags)
    except Exception as err:
        print(str(err))
        handleError("Error getting Version from cloud", err)
        sugestedUpdateVersion = ""

    return sugestedUpdateVersion


# ============================
def getCloudTags(token=""):

    global g_lastGetTagsFromServer
    global GetTagsFromServerMinRateSeconds
    # initConfig()
    # token = getCloudToken()

    tags = None
    try:
        IpAddress = socket.gethostbyname(socket.gethostname())
        url = cfg_serverAddress + "/api/CloudConnector/GetTags/"

        tags = None

        now = datetime.now()
        getTagsTimePass = 0
        if g_lastGetTagsFromServer:
            getTagsTimePass = (now - g_lastGetTagsFromServer).total_seconds()


        ci_print(
            "Last Get tags from server was "
            + str(getTagsTimePass)
            + " seconds ago , getTagsRate="
            + str(GetTagsFromServerMinRateSeconds), "INFO"
        )
        if getTagsTimePass == 0 or getTagsTimePass > GetTagsFromServerMinRateSeconds:
            ret = ciRequest(url, None, "get", "getCloudTags", token)
            if ret and ret["isOK"] == True:
                response = ret["response"]
                g_lastGetTagsFromServer = datetime.now()
                ans = json.loads(response.text)
                arangedTags = arrangeTagsByScanTime(ans["Tags"])
                tags = {}
                tags["Tags"] = arangedTags
                # write tags to file
                f = open(TagsDefenitionFileName, "w")
                json.dump(tags, f)
                f.close()

                ci_print(
                    "Get Cloud Counters recieved " + str(len(arangedTags)) + " Tags", "INFO"
                )
            else:
                ci_print("Get Cloud Counters from server failed ", "WARNING")
    except Exception as inst:
        print(str(inst))
        handleError("Error getting tags from cloud", inst)
        tags = None

    if tags == None:
        tags = getTagsDefenitionFromFile()

    ci_print(str(tags), "INFO")
    return tags


# ============================
def arrangeTagsByScanTime(tags):

    ans = {}
    try:
        for index in range(len(tags)):
            scanRate = tags[index]["ScanRate"]

            if scanRate in ans:
                tagsListPerScanRate = ans[scanRate]
            else:
                ans[scanRate] = []

            ans[scanRate].append(tags[index])
    except Exception as err:
        handleError("arrangeTagsByScanTime", err)
    return ans


# ============================
def printTags(tags):
    try:
        ci_print("Print Tags : List Contains " + str(len(tags)) + " Tags", "INFO")
        ci_print(str(tags))
        for index in range(len(tags)):
            msg = (
                "Tag Id: "
                + str(tags[index]["TagId"])
                + " ,TagName: "
                + str(tags[index]["TagName"])
                + " ,TagAddress: "
                + str(tags[index]["TagAddress"])
            )
            msg = msg + " ,ScanRate: " + str(tags[index]["ScanRate"])
            ci_print(msg, "INFO")

    except Exception as inst:
        handleError("Error in printTags", inst)


# ============================
def setCloudTags(tagValues, token=""):

    global TagStatus
    updatedSuccessfully = False
    try:
        # url = HTTP_PREFIX + '://'+cfg_serverAddress+'/api/CloudConnector/SetCounterHistory/'
        url = cfg_serverAddress + "/api/CloudConnector/SetCounterHistory/"

        payload = []
        for index in range(len(tagValues)):
            TagId = tagValues[index]["TagId"]
            timeStamp = str(tagValues[index]["time"])

            value = tagValues[index]["value"]
            status = TagStatus.Invalid
            if str(tagValues[index]["status"]) == "20":
                status = TagStatus.Valid

            ci_print("TagId = " + str(TagId) + " : " + str(value), "INFO")


            tagVal = {
                "TagId": TagId,
                "TimeStmp": timeStamp,
                "StatusCE": status,
                "Value": value,
            }
            payload.append(tagVal)

        ci_print(str(payload), "INFO")
        ret = ciRequest(url, json.dumps(payload), "post", "setCloudTags", token)
        response = ret["response"]

        ci_print(response.text, "INFO")

        updatedSuccessfully = response.status_code == 200

    except Exception as inst:
        handleError("Error setting tags in cloud", inst)
        return False

    return updatedSuccessfully


# ============================
def sendLogFileToCloud(numberOfRows=10, timestamp="", requestId=""):

    try:
        requestId = str(requestId)
        lines = readLastRowsFromLog(numberOfRows)
        for line in lines:
            # print "line:" + line
            addCloudConnectorLog(line, timestamp, str(requestId))
    except Exception as inst:
        handleError("sendLogFileToCloud: Error setting tags in cloud", inst)
        return False


# ============================
def addCloudConnectorLog(log, timeStamp="", requestId=""):

    global currentToken
    if timeStamp == "":
        timeStamp = datetime.now()
    updatedSuccessfully = False

    token = currentToken
    if token == "":
        print("no token skip addCloudConnectorLog", "INFO")
        return
    try:
        url = cfg_serverAddress + "/api/CloudConnector/SetCounterLog/"

        payload = []
        logData = {"Log": log, "TimeStamp": str(timeStamp), "RequestId": requestId}
        payload.append(logData)
        # print str(payload)
        ret = ciRequest(url, json.dumps(payload), "post", "SetConnectorLog", token)
        response = ret["response"]

        # print (response.text)
        # logging.info('setCloudTags response = ' + str(response) + ' : ' + response.text )
        # print '==' + str(response.status_code)
        updatedSuccessfully = response.status_code == 200

    except Exception as inst:
        handleError("Exception in addCloudConnectorLog", inst)
        return False

    return updatedSuccessfully


# ============================
def getCloudConnectorRequests():

    global currentToken
    token = currentToken

    ci_print("start getCloudConnectorRequests", "INFO")
    ans = None
    try:
        url = cfg_serverAddress + "/api/CloudConnector/GetCloudConnectorRequests/"
        ret = ciRequest(url, None, "get", "GetCloudConnectorRequests", token)
        # print "ret=" + str(ret)
        response = ret["response"]
        if ret["isOK"] == True:
            ans = json.loads(response.text)
    except Exception as inst:
        handleError("Error getting requests from cloud", inst)
        ans = None

    ci_print("Requests = " + str(ans), "INFO")
    return ans


# ============================
def updateCloudConnectorRequests(requestId, status):

    global currentToken
    updatedSuccessfully = False

    token = currentToken
    if token == "":
        ci_print("no token skip updateCloudConnectorRequests", "WARNING")
        return
    try:
        url = (
            cfg_serverAddress
            + "/api/CloudConnector/SetCounterRequestStatus/?requestId="
            + str(requestId)
            + "&status="
            + str(status)
        )
        # print "url="+url
        ret = ciRequest(url, "", "post", "SetCounterRequestStatus", token)
        response = ret["response"]

        print(response.text)
        # logging.info('setCloudTags response = ' + str(response) + ' : ' + response.text )
        # print '==' + str(response.status_code)
        updatedSuccessfully = response.status_code == 200

    except Exception as inst:
        handleError("Exception in addCloudConnectorLog", inst)
        # handleError("Error setting tags in cloud", inst)
        return False

    return updatedSuccessfully


# get requests from cloud and handle it
# ============================
def handleNewRequests():

    try:
        requests = getCloudConnectorRequests()
        if requests:
            ci_print("Got " + str(len(requests)) + " new requests", "DEBUG")
            # print "requests::" + str(requests)

            for request in requests:
                try:
                    # print 'request[Type]=' + str(request['Type'])
                    if request["Type"] == 1:  # send logs
                        # print "Handling request " + str(request)
                        requestData = json.loads(request["Data"])
                        rownCount = requestData["Rows"]
                        ret = updateCloudConnectorRequests(request["Id"], 2)  # in process
                        requestData = json.loads(request["Data"])
                        # print "--------request['Id']===" + str(request['Id'])
                        sendLogFileToCloud(rownCount, "", request["Id"])
                        ret = updateCloudConnectorRequests(request["Id"], 3)  # Done
                    if request["Type"] == 2:  # change logs level
                        ci_print(
                            "Handling change log level request " + str(request), "INFO"
                        )
                        requestData = json.loads(request["Data"])
                        newLogLevel = requestData["Level"]
                        ret = updateCloudConnectorRequests(request["Id"], 2)  # in process
                        setLogLevel(newLogLevel)
                        ret = updateCloudConnectorRequests(request["Id"], 3)  # Done
                    if request["Type"] == 3:  # reboot
                        ci_print("Handling reboot request " + str(request), "INFO")
                        ret = updateCloudConnectorRequests(request["Id"], 3)  # Done
                        reboot()
                except Exception as innerinst:
                    print("error handling request ") + str(innerinst)
                    handleError("Error setting tags in inner handleNewRequests", innerinst)
    except Exception as inst:
        handleError("Error in handleNewRequests", inst)
        return False


# ============================
# PLC Functions
# ============================
def fill_Invalids(tagsDefenitions, values):

    global TagStatus

    retValues = []
    try:
        time = str(datetime.now(tzlocal.get_localzone()))
        valuesDict = {}
        ci_print("start fill_Invalids", "INFO")
        # prepare values dictionery
        for val in values:
            # print "val" + str(val)
            # print "val[u'TagId']=" + str(val[u'TagId'])
            valuesDict[val["TagId"]] = val
        # print "valuesDict="+str(valuesDict)
        for tagdef in tagsDefenitions:
            TagId = tagdef["TagId"]
            # print "tagdef" + str(tagdef)
            if TagId in valuesDict:
                retValues.append(valuesDict[TagId])
            else:
                tagAddress = tagdef["TagAddress"]
                val = {
                    "TagAddress": tagAddress,
                    "TagId": TagId,
                    "time": time,
                    "value": None,
                    "status": TagStatus.Invalid,
                }
                retValues.append(val)
        # print "=============="
        # print str(retValues)
    except Exception as inst:
        handleError("Error in fill_Invalids", inst)

    return retValues


# ippp
# ============================
def readEtherNetIP_Tags(tags_definitions):

    global TagStatus
    ci_print("start readEtherNetIP_Tags", "INFO")
    ans = []

    arranged_tags = arrange_tags_by_plc(tags_definitions)

    try:

        for plc_address, tags_def_list in arranged_tags.items():
            tags = [tag_def["TagAddress"] for tag_def in tags_def_list]
            ci_print("readEtherNetIP_Tags: Read tags " + str(tags), "DEBUG")

            with client.connector(host=plc_address, port=address[1], timeout=1.0) as connection:
                operations = client.parse_operations(tags)
                failures, transactions = connection.process(
                    operations=operations,
                    depth=1,
                    multiple=0,
                    fragment=False,
                    printing=False,
                    timeout=1.0,
                )

            #host = plc_address  # Controller IP address
            #port = address[1]  # default is port 44818
            #depth = 1  # Allow 1 transaction in-flight
            #multiple = 0  # Don't use Multiple Service Packet
            #fragment = False  # Don't force Read/Write Tag Fragmented
            #timeout = 1.0  # Any PLC I/O fails if it takes > 1s
            #printing = False  # Print a summary of I/O

            ci_print("transactions " + str(transactions), "INFO")
            ci_print("failures " + str(failures), "INFO")


            # client.close()
            # sys.exit( 1 if failures else 0 )

            for index, tag_def in enumerate(tags_def_list):
                tag_address = tag_def["TagAddress"]
                try:
                    if transactions[index]:
                        tag_id = int(tag_def["TagId"])
                        value = transactions[index][0]
                        time = str(datetime.now(tzlocal.get_localzone()))
                        ci_print("get register tagAddress=" + str(tag_address) + " value=" + str(value), "INFO")
                        val = {
                            "TagAddress": tag_address,
                            "TagId": tag_id,
                            "time": time,
                            "value": value,
                            "status": TagStatus.Valid,
                        }
                        ans.append(val)
                    else:
                        ci_print("Error reading Tag " + tag_address, "INFO")
                except ValueError:
                    handleError("Error reading tag value " + tag_address, ValueError)

        ci_print("End Read readEtherNetIP Tag", "INFO")
    except Exception as inst:
        handleError("Error in readEtherNetIP_Tags", inst)

    return fill_Invalids(tags_definitions, ans)


def arrange_tags_by_plc(tags_definitions):

    arranged_tags = {}

    for tag_def in tags_definitions:
        plc_address = tag_def.get("PlcIpAddress")
        if plc_address:
            if plc_address not in arranged_tags:
                arranged_tags[plc_address] = []
            arranged_tags[plc_address].append(tag_def)

    return arranged_tags

# ============================
def readModBusTags(tags_definitions):

    ans = []

    arranged_tags = arrange_tags_by_plc(tags_definitions)

    try:
        ci_print("Start Read ModBus Tag", "INFO")

        for plc_address in arranged_tags:
            maxOffset = 0
            for p in arranged_tags[plc_address]:
                offset = int(p.TagAddress)
                maxOffset = max(maxOffset, offset)

            from pymodbus.client import ModbusTcpClient as ModbusClient

            client = ModbusClient(plc_address, port=502)
            client.connect()

            rr = client.read_input_registers(0, maxOffset)  # 30000
            ci_print(str(rr.registers), "INFO")


            for index in range(len(plc_address)):
                try:
                    offset = int(plc_address[index]["TagAddress"]) - 1
                    TagId = int(plc_address[index]["TagId"])

                    value = rr.registers[offset]
                    time = str(datetime.now(tzlocal.get_localzone()))
                    ci_print("get register offset=" + str(offset) + " value=" + str(value), "INFO")
                    val = {
                        "TagAddress": offset,
                        "TagId": TagId,
                        "time": time,
                        "value": value,
                        "status": TagStatus.Valid,
                    }
                    ans.append(val)
                    # ans.update({offset:[offset,CounterId,datetime.now(),value]})
                except ValueError:
                    ci_print(
                        "Error reading tag value " + plc_address[index]["TagAddress"],
                        "DEBUG",
                    )

            client.close()

        ci_print("End Read ModBus Tag", "INFO")
        return ans
    except Exception as inst:
        handleError("error reading modbus", inst)
        return fill_Invalids(tags_definitions, ans)


# ============================
def readSimulation_Tags(tagsDefinitions):

    ans = []

    try:
        for tag_def in tagsDefinitions:
            try:
                TagId = int(tag_def.get("TagId"))
                value = random.uniform(-10, 10)
                time = str(datetime.now(tzlocal.get_localzone()))
                val = {
                    "TagId": TagId,
                    "time": time,
                    "value": value,
                    "status": TagStatus.Valid,
                }
                ans.append(val)
            except (ValueError, TypeError) as e:
                ci_print(f"Error processing tag definition: {e}")

        ci_print("End Read readSimulation_Tags", "INFO")
    except Exception as inst:
        handleError("Error in readSimulation_Tags", inst)

    return ans


# ============================
def printTagValues(tagValues):
    ci_print("Count " + str(len(tagValues)) + " Tags", "INFO")
    for index in range(len(tagValues)):
        ci_print(str(tagValues[index]), "INFO")


# ============================
def getLocalVersion():
    return VER


# ============================
def getServerSugestedVersion():
    return sugestedUpdateVersion


# ============================
# Tag Files Functions
# ============================
def writeTagsDefenitionToFile(tags):

    try:

        f = open(TagsDefenitionFileName, "w")
        json.dump(tags, f)
        f.close()
        return
    except Exception as inst:
        handleError("Error in writeTagsDefenitionToFile", inst)


# ============================
def getTagsDefenitionFromFile():

    try:
        f2 = open(TagsDefenitionFileName, "r")
        tags = json.load(f2)
        f2.close()
        ci_print("Got " + str(len(tags)) + " Tags From File", "INFO")
        # print tags
        return tags
    except Exception as inst:
        handleError("Error in getTagsDefenitionFromFile", inst)


# ============================
def delTagsDefenitionFile():

    try:
        os.remove(TagsDefenitionFileName)
        return
    except Exception as inst:
        handleError("Error in delTagsDefenitionFile", inst)


# ============================
def getTagsValuesFromFile(fileName):

    try:
        ci_print("Start get Values From File " + fileName, "INFO")
        f2 = open(fileName, "r")
        vals = json.load(f2)
        f2.close()
        ci_print("Got " + str(len(vals)) + " Values From File", "INFO")
        return vals
    except Exception as inst:
        handleError("Error in getTagsValuesFromFile", inst)


# ============================
def saveValuesToFile(values, fileName):

    try:
        numOfFiles = len(
            fnmatch.filter(os.listdir("/" + HomeDir + "/" + TagsValueDir), "*.txt")
        )
        ci_print("Number of files in folder : " + str(numOfFiles), "INFO")
        if numOfFiles < 10000:
            if fileName == "":
                fileName = (
                    TagsValuesFileName
                    + datetime.now().strftime("%Y%m%d-%H%M%S%f")
                    + ".txt"
                )
            # fileName = "./" + TagsValueDir + '/' + fileName
            fileName = "/" + HomeDir + "/" + TagsValueDir + "/" + fileName
            ci_print("Start save Values To File " + fileName, "INFO")
            # write tags to file
            f = open(fileName, "w")
            json.dump(values, f)
            f.close()
            time.sleep(1)  # prevent two files in same ms
        else:
            ci_print("Too many files in folder!!!", "WARNING")
    except Exception as inst:
        handleError("Error in saveValuesToFile", inst)

# ============================
def handleValuesFile(fileName, token=""):

    try:
        ci_print("Start handleValuesFile " + fileName, "INFO")
        values = getTagsValuesFromFile(fileName)
        isOk = setCloudTags(values, token)
        if isOk:
            os.remove(fileName)
            ci_print("file removed " + fileName, "INFO")
            return True
        else:
            # errFile = replaceFileName(fileName,"ERR")
            errFile = fileName.replace("/[NEW]", "/ERR/[ERR]")
            os.rename(fileName, errFile)
            ci_print("Error Handling File " + errFile, "WARNING")
    except Exception as inst:
        handleError("Error in handleValuesFile", inst)
    return False

# ============================
def handleAllValuesFiles(token=""):

    try:
        ci_print("Started handleAllValuesFiles", "INFO")
        # if token=='':
        #    token = getCloudToken()
        i = 0
        dirpath = "/" + HomeDir + "/" + TagsValueDir + "/"
        filesSortedByTime = [
            s for s in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, s))
        ]
        filesSortedByTime.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
        ci_print(
            "in Dir " + dirpath + " Found " + str(len(filesSortedByTime)) + " files",
            "INFO",
        )
        for file in filesSortedByTime:
            if file.endswith(".txt") and file.startswith("[NEW]"):
                i = i + 1
                ci_print("about to process file:" + file, "INFO")
                handleValuesFile("/" + HomeDir + "/" + TagsValueDir + "/" + file, token)

        if i > 0:
            ci_print(str(i) + " Files handled", "INFO")
    except Exception as inst:
        ci_print("Error handleAllValuesFiles " + str(inst))


# ============================
def createLibIfMissing():

    try:
        dirName = "/" + HomeDir + "/"
        d = os.path.dirname(dirName)
        if not os.path.exists(d):
            os.makedirs(dirName)
            ci_print('Home DIR  Created :: ' + dirName, "INFO")

        dirName = "/" + HomeDir + "/" + TagsValueDir + "/"
        d = os.path.dirname(dirName)
        if not os.path.exists(d):
            os.makedirs(dirName)
            ci_print('TagsValueDir Created', "INFO")

        dirName = "/" + HomeDir + "/" + TagsValueDir + "/ERR/"
        d = os.path.dirname(dirName)
        if not os.path.exists(d):
            os.makedirs(dirName)
            ci_print('TagsValueDir/ERR Created', "INFO")

    except Exception as inst:
        ci_print("Error createLibIfMissing " + str(inst))

    # ============================


# ============================
# Remove oldest file
# ============================
def removeOldestFile():

    global cfg_maxFiles

    try:
        dirName = "/" + HomeDir + "/" + TagsValueDir + "/"
        dir = os.path.dirname(dirName)
        if os.path.exists(dir):
            list_of_files = glob.glob(dirName + '*.txt')
            num_of_files = len(list_of_files)
            maxFiles = int(cfg_maxFiles)

            if maxFiles < num_of_files & num_of_files > 0:
                # In case more than one file is exceeding cfg_maxFiles.
                # Used for initial case where num of files is much bigger than config MaxFiles.
                for x in range(maxFiles, num_of_files):
                    oldest_file = min(list_of_files, key=os.path.getctime)
                    os.remove(oldest_file)
                    list_of_files.remove(oldest_file)

    except Exception as inst:
        handleError("Error in removeOldestFile", inst)


def arrange_by_connector_type(tags_def):
    arranged_tags = {}

    for tag in tags_def:
        connector_type = tag.get('connectorTypeName', '')  # Provide a default value if key doesn't exist
        if connector_type not in arranged_tags:
            arranged_tags[connector_type] = []
        arranged_tags[connector_type].append(tag)

    return arranged_tags

# ============================
# Main Loop
# ============================
def Main():

    global ScanRateLastRead
    global currentToken
    try:
        ci_print("Loop started at " + str(datetime.now()), "INFO")
        if currentToken == "":
            currentToken = getCloudToken()
        # currently must get tags from cloud to init server before setting values
        tagsDefScanRatesAns = getCloudTags(currentToken)
        tagsDefScanRates = tagsDefScanRatesAns["Tags"]

        for scanRate in tagsDefScanRates:

            if scanRate in (None, 'null'):
                continue

            scanRateInt = int(scanRate)
            scanRateStr = str(scanRate)
            diff = 0
            if scanRateStr in ScanRateLastRead:
                now = datetime.now()
                diff = (now - ScanRateLastRead[scanRateStr]).total_seconds()
                # print ('diff = -------' + str(diff))

            ci_print("*********************", "INFO")
            ci_print("diff=" + str(diff) + " scanRateInt=" + str(scanRateInt), "INFO")
            print("diff=" + str(diff) + " scanRateInt=" + str(scanRateInt))
            if diff + 3 > scanRateInt or diff == 0:
                ci_print(
                    "Get Tag Values For Scan Rate "
                    + str(scanRate)
                    + " ' time Form Last Run:"
                    + str(diff)
                    + " Sec", "INFO"
                )
                tagsDef = tagsDefScanRates[scanRate]
                arranged_tags = arrange_by_connector_type(tagsDef)

                for connector_type in arranged_tags:
                    print(connector_type)
                    values = None
                    if connector_type == "Simulation":
                        values = readSimulation_Tags(arranged_tags[connector_type])
                    if connector_type == "Modbus":
                        values = readModBusTags(arranged_tags[connector_type])
                    if connector_type == "Ethernet/IP":
                        values = readEtherNetIP_Tags(arranged_tags[connector_type])
                        if values == []:
                            ci_print("Ethernet Empty values ::1", "ERROR")
                            values = readEtherNetIP_Tags(arranged_tags[connector_type])
                            if values == []:
                                time.sleep(0.1)
                                ci_print("Ethernet Empty values ::1", "ERROR")
                                values = readEtherNetIP_Tags(arranged_tags[connector_type])
                                if values == []:
                                    time.sleep(1)
                                    ci_print("Ethernet Empty values ::2", "ERROR")
                                    values = readEtherNetIP_Tags(arranged_tags[connector_type])

                    if len(values) > 0:
                        printVal = (
                            " Val="
                            + str(values[0]["value"])
                            + " "
                            + str(len(values))
                            + " Tags"
                        )
                        ci_print(printVal, "INFO")
                        print(
                            str(datetime.now())
                            + " Send Vals:"
                            + str(scanRate)
                            + " diff "
                            + str(diff)
                            + printVal
                        )
                    else:
                        printVal = " No Values"
                        ci_print(printVal, "ERROR")
                        print(
                            str(datetime.now())
                            + " Send Vals:"
                            + str(scanRate)
                            + " diff "
                            + str(diff)
                            + printVal
                        )

                    if values:
                        saveValuesToFile(values, "")
                        removeOldestFile()

                        now = datetime.now()
                        ci_print("scanRateStr time updated==>" + str(now), "INFO")
                        ScanRateLastRead[scanRateStr] = now


        if currentToken != "":
            handleAllValuesFiles(currentToken)
        else:
            ci_print("No Token, skipping upload step", "WARNING")
    except Exception as inst:
        handleError("Error in Main", inst)
        currentToken = ""

    ci_print("===============================", "INFO")
    ci_print("CI_CloudConnector Ended", "INFO")


