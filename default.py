import os, sys, subprocess
import xbmc, xbmcaddon, xbmcgui
import time

if __name__ == '__main__':
    xbmc.log("Disabling sleep! %s" % time.time(), level=xbmc.LOGNOTICE)
    subprocess.call('xset s off', shell=True)
    subprocess.call('xset -dpms', shell=True)
    xbmc.log("Sleep disabled! %s" % time.time(), level=xbmc.LOGNOTICE)
    
    monitor = xbmc.Monitor()
    while not monitor.abortRequested():
        # Sleep/wait for abort for 10 seconds
        if monitor.waitForAbort(10):
            # Abort was requested while waiting. We should exit
            break

    xbmc.log("Enabling sleep! %s" % time.time(), level=xbmc.LOGNOTICE)
    subprocess.call('xset +dpms', shell=True)
    subprocess.call('xset s 600', shell=True)
    xbmc.log("Sleep enabled! %s" % time.time(), level=xbmc.LOGNOTICE)

    