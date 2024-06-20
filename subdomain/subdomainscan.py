import requests

import pyfiglet
import sys

result = pyfiglet.figlet_format('404_is', font='slant')
print(result)


domain = input("404 would require you to enter the domain:")

path_to_wordlist = input("404 would require you to enter path to your wordlist: ")

file = open(path_to_wordlist)

content = file.read()

subdomains = content.splitlines()


discovered_subdomains = []
for subdomain in subdomains:
    
    url = f"http://{subdomain}.{domain}"
    try:
        
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("[+] Discovered subdomain:", url)
        
        discovered_subdomains.append(url)


with open("discovered_subdomains.txt", "w") as f:
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)