#coding: utf-8

import sys
import subprocess

def sky_process_list():
    """
    get process list from os
    """
    pstr = subprocess.check_output('sh -c "pgrep SkyDaemon SkyAgent"', shell=True)
    if pstr is None:
        sys.exit()
    return pstr.splitlines()

def main():
    # process list
    plist = sky_process_list()

    # kill processes
    subprocess.call(['kill'] + plist])

if __name__ == '__main__':
    main()