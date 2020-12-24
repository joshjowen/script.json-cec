#!/usr/bin/env python
import xbmc
import sys
import time

try:
    from urllib.parse import parse_qs
except ImportError:
    from urlparse import parse_qs


def handle_command():
    try:
        params = parse_qs('&'.join(sys.argv[1:]))
        command = params.get('command', None)
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


if __name__ == "__main__":
    handle_command()
