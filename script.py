import xbmc
import urlparse
import sys
import time
import os

try:
        params = urlparse.parse_qs('&'.join(sys.argv[1:]))
        command = params.get('command',None)[0].split(" ")
except:
        command = None

if command and command[0] == 'activate':
        xbmc.executebuiltin('CECActivateSource')

elif command and command[0] == 'toggle':
        xbmc.executebuiltin('CECToggleState')

elif command and command[0] == 'standby':
        xbmc.executebuiltin('CECStandby')

elif command and command[0] == 'stop_and_standby':
        if xbmc.Player().isPlaying():
                xbmc.executebuiltin("PlayerControl(Stop)")
                time.sleep(3)
        xbmc.executebuiltin('CECStandby')

elif command[0] == 'cec_client':
        cec_command = "echo '{}' | cec-client -s".format(" ".join(command[1:])
        os.system(cec_command)
