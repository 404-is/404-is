import pikepdf
from tqdm import tqdm
import pyfiglet

import sys

result = pyfiglet.figlet_format('404_is', font='slant')
print(result)

path_to_wordlist = input ("404 would require you to enter path to wordlist:") 

path_to_pdf = input ("404 would require you to enter path to pdf you want to crack:")

# load password 
passwords = [ line.strip() for line in open(path_to_wordlist) ]


# crack password
for password in tqdm(passwords, "404 is Decrypting PDF"):
    try:
        # open PDF file
        with pikepdf.open(path_to_pdf, password=password) as pdf:
            # Password decrypted successfully, break out of the loop
            print("[+] 404 has found Password:", password)
            break
    
    except pikepdf._qpdf.PasswordError as e:
        
        continue
    except IndexError:
        print("\n[+] 404 Detected an error, try checking if router hasnt blocked 404...Quitting\n")
    except FileNotFoundError:
        print("\n[+] 404 Detected an error, check the file path again..Quitting\n")


