import os
import socket
import sys
import operator
import time

# cap_file_dir = cap_file_str
# timestr = timestr
# mon_mode_interface = airodump_upgrade.mon_mode_interface

# # DOesn't work either even though it should
# capture_Interface = airodump_upgrade.mon_mode_interface
cap_file_dir = '/root/Cylon-Raider-Lite/logs/'
timestr = time.strftime("%Y%m%d-%H%M%S")

capture_Interface = 'wlan1mon'
tcpdump_filename = cap_file_dir + 'tcpdump_monitor_mode_' + timestr + '.pcap'



cmd_str = "tcpdump & -w {0} -w {1} &".format(
    str(capture_Interface),
    str(tcpdump_filename)
)

if KeyboardInterrupt:
    exit(0)
# module_name = '/root/Cylon-Raider-Lite/tcp_dump_background.py'
# cmd_str = """gnome-terminal -e 'bash -c \"python {0}; exec bash\"""".format(
#     str(module_name)
# )
# os.system(cmd_str)
# print toolkits.red('TCPDump executed')
# tcpdump_filename = cap_file_dir + timestr + 'tcpdump.pcap'
# cmd_str = "tcpdump -w {0} -i {1}"".format(
#     str(tcpdump_filename),
#     str(mon_mode_interface)
# )
#
# os.system(cmd_str)
