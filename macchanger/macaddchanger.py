import subprocess
import string
import random
import re
import pyfiglet
import netifaces
import time

result = pyfiglet.figlet_format('404_is', font="slant")
print(result)
print("A MAC Address spoofer designed by obadare victor")

print("Avaliable interfaces are as follows:")

interfaces = netifaces.interfaces()
for interface in interfaces:
    print(interface)


def random_mac():
    """Generate and return mac address needed"""
    # get the hexdigits uppercased
    hexdigits = ''.join(set(string.hexdigits.upper()))
    # second character must be 0, 2, 4, 6, 8, A, C, or E
    mac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac += random.choice("A024C6E8")
            else:
                mac += random.choice(hexdigits)
        mac += ":"
    return mac.strip(":")

def current_mac(iface):
    # use the ifconfig to get interface details
    output = subprocess.check_output(f"ifconfig {iface}", shell=True).decode()
    return re.search("ether (.+) ", output).group().split()[1].strip()

def change_mac(iface, new_mac):
    # disable network interface selected 
    subprocess.check_output(f"ifconfig {iface} down", shell=True)
    # change current mac address 
    subprocess.check_output(f"ifconfig {iface} hw ether {new_mac}", shell=True)
    # enable the network interface 
    subprocess.check_output(f"ifconfig {iface} up", shell=True)

if __name__ == "__main__":

    
    argsinterface = input("kindly input  you interface:")
    iface = argsinterface
    argsrandom = input("kindly specify if you want a randpom mac by pressing any letter:")
    argsmac = input("kindly specify if you want a specific mac if No press enter:")

    if argsrandom:
        
        new_mac = random_mac()
    elif argsmac:
        
        new_mac = argsmac
    
    old_mac = current_mac(iface)
    print("[*] System old MAC address:", old_mac)
    
    change_mac(iface, new_mac)
   
    new_mac = current_mac(iface)
    print("[+] System New MAC address:", new_mac)
    
time.sleep(200000)