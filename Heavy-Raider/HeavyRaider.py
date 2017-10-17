#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen
import time

os.system('cat /root/Cylon-Raider/banner_reaver.txt')
os.system('cat /root/Cylon-Raider/Heavy-Raider/DISCLAIMER.txt')


def WASH_run():
    os.system('clear')
    # os.system('python /root/Cylon-Raider/Heavy-Raider/WASH.py')
    # os.system("gnome-terminal -e 'bash -c \"python /root/Cylon-Raider/routersploit/rsf.py; exec bash\"'")
    os.system("gnome-terminal -e 'bash -c \"python /root/Cylon-Raider/Heavy-Raider/WASH.py; exec bash\"'")
    return

def REAVER_run():
    os.system('clear')
    # os.system('python /root/Cylon-Raider/Heavy-Raider/REAVER.py')
    os.system("gnome-terminal -e 'bash -c \"python /root/Cylon-Raider/Heavy-Raider/REAVER.py; exec bash\"'")
    return

def main():
    opt_List = [
        '\n\t#1. Use WASH to scan for WPS enabled networks',
        '#2. Run Reaver from the information that you gathered from #1'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "1":
        os.system('clear')
        WASH_run()
        main()
    elif opt_Choice == "2":
        os.system('clear')
        REAVER_run()
        main()
    else:
        os.system('clear')
        print 'You have entered a invalid option'
        main()
    return

main()
