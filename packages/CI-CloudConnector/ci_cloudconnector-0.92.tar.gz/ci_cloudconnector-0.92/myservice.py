import sys
import time

import psutil
import win32api
import win32con
import win32serviceutil
import win32service
import win32event
import subprocess
import main


class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = "CloudConnectorService2"
    _svc_display_name_ = "CloudConnectorService2"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)

    def SvcDoRun(self):
        try:
            main.init()
            main.args([0, 'Start'])
            main.monitor_main_file("logic.py")
        except Exception as e:
            # Log or handle any exceptions
            pass

        # Wait for the stop event
        win32event.WaitForSingleObject(self.stop_event, win32event.INFINITE)

    def SvcStop(self):

        # Add a delay before terminating the process
        time.sleep(1)  # Adjust the delay time as needed

        # Get the PID of the current process
        pid = self.GetPID()
        # Terminate the process with the given PID
        self.TerminateProcess(pid)
        # Set the stop event to signal the service to stop
        win32event.SetEvent(self.stop_event)

    def GetPID(self):
        return win32api.GetCurrentProcessId()

    def TerminateProcess(self, pid):
        try:
            # Open the process handle
            hProcess = win32api.OpenProcess(win32con.PROCESS_TERMINATE, 0, pid)
            # Terminate the process
            win32api.TerminateProcess(hProcess, 0)
            # Close the process handle
            win32api.CloseHandle(hProcess)
        except Exception as e:
            # Log or handle any exceptions
            pass


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(MyService)
