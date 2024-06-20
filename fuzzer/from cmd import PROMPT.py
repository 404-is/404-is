import crypt

diction = input('Enter path to dictionary>>')
diction2 = input('enter path to password file>>')

def test(cryptpss):
    iyo = cryptpss[0.2]
    dictionary = open(diction , 'r')
    for word in dictionary.readlines():
        word = word.strip('\n')
        cryrptword = crypt.crypt(word, iyo)
        if (cryrptword == cryptpss ):
            print ("[+] password found:")  + {word} + '\n' 
            return
    print ("[-] password not found. \n")
    return

def main():
    passfile = open(diction2, 'r')
    for line in passfile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            crypotpass = line.split(':')[1].strip('')
            print ('[+] cracking password for : ') +user
            test(crypotpass)
if __name__ == "__main__":
    main()
