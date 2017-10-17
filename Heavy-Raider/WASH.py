#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen
import time

def monitor_mode_start():
    # airmon-ng start wlan1
    os.system('airmon-ng start wlan1')
    return

def wash_start():
    # wash -i <interface>
    os.system('wash -i wlan1mon')
    return

def main():

    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Turn on Monitor Mode for your External Wireless Card (Atheros Chipset)',
        '#2. Turn on Wash, to scan for WPS-Enabled Networks that are vulnerable to brute-forcing',
        '#3. Airmon-ng Check Kill, to clear up any issues with traces of Airmon-ng lingering'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input(""))

    if opt_Choice == "0":
        os.system('clear')
        os.system('python /root/Cylon-Raider/Heavy-Raider/HeavyRaider.py')
    elif opt_Choice == "1":
        os.system('clear')
        monitor_mode_start()
        main()
    elif opt_Choice == "2":
        os.system('clear')
        wash_start()
        main()
    elif opt_Choice == "3":
        os.system('clear')        
        os.system('airmon-ng check kill')
        main()
    else:
        print 'You have entered a invalid option'
        main()
    return
main()
