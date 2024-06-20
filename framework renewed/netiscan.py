#!/usr/bin/env python

import scapy.all as nitro
import argparse
import pyfiglet
import os
import netifaces
import time

os.sys.path.append('/usr/bin')
result = pyfiglet.figlet_format('404_is', font="slant")
print(result) 
print("A Network scanning tool designed by obadare victor")
interfaces = netifaces.interfaces()
for interface in interfaces:
    print(interface)
input_value = raw_input("404 would need you to enter the ipaddress you want to scan>>") + "/24"

def scan(ip):
    _arp_request = nitro.ARP(pdst=ip)
    broadcast = nitro.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/_arp_request
    answered_list = nitro.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    
    clients_list = []
    for value in answered_list:
        client_dictionary = {"ip": value[1].psrc, "mac": value[1].hwsrc}
        clients_list.append(client_dictionary)
    return (clients_list)
   
def print_result(result_list):
    print("IP\t\t\tMAC address\n............................................................")
    for client in result_list:
        print (client["ip"] + "\t\t" + client["mac"] )

options = input_value
scan_result = scan(options) 
print_result(scan_result)
time.sleep(100000)