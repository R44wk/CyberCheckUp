import os
import time


def banner ():
    os.system("clear")
    print ("""

 /$$$$$$            /$$                            /$$$$$$  /$$                           /$$               /$$   /$$          
 /$$__  $$          | $$                           /$$__  $$| $$                          | $$              | $$  | $$          
| $$  \__/ /$$   /$$| $$$$$$$   /$$$$$$   /$$$$$$ | $$  \__/| $$$$$$$   /$$$$$$   /$$$$$$$| $$   /$$        | $$  | $$  /$$$$$$ 
| $$      | $$  | $$| $$__  $$ /$$__  $$ /$$__  $$| $$      | $$__  $$ /$$__  $$ /$$_____/| $$  /$$/ /$$$$$$| $$  | $$ /$$__  $$
| $$      | $$  | $$| $$  \ $$| $$$$$$$$| $$  \__/| $$      | $$  \ $$| $$$$$$$$| $$      | $$$$$$/ |______/| $$  | $$| $$  \ $$
| $$    $$| $$  | $$| $$  | $$| $$_____/| $$      | $$    $$| $$  | $$| $$_____/| $$      | $$_  $$         | $$  | $$| $$  | $$
|  $$$$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$$| $$      |  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$        |  $$$$$$/| $$$$$$$/
 \______/  \____  $$|_______/  \_______/|__/       \______/ |__/  |__/ \_______/ \_______/|__/  \__/         \______/ | $$____/ 
           /$$  | $$                                                                                                  | $$      
          |  $$$$$$/                                                                                                  | $$      
           \______/                                                                                                   |__/      

By: @Rumpels7il7skin 


                """)
banner()

def leak ():
    
    os.system("/root/Documents/CyberCheckUp/pwndb/pwndb.py --target @{} --output loot/pwndb.txt".format(domain))
    time.sleep(5)

def dork ():
    
    os.system("/root/Documents/CyberCheckUp/uDork/uDork.py -d {} -e all -o loot/dorks".format(domain))
    os.system("/root/Documents/CyberCheckUp/uDork/uDork.py -d {} -s Admin".format(domain))
    
def scan ():
    
    os.system("/root/Documents/CyberCheckUp/Sublist3r/sublist3r.py -v -d {} -b  -o loot/domains.txt".format(domain))
    time.sleep(5)
    os.system("nmap -sF -sV -A --open -iL {} -oX loot/scan.xml".format(file))
 



###############################################################################################3

while (True):
    print("""
    Select option:\n
    1) Give a domain 
    2) List of IPs
    3) Run!
    0) Exit.
    """)
    option=input("Ccu:~# ")

    if option == 1:
        domain = raw_input("Give me a domain: ")
    elif option == 2:
        file= input(("Path of file: "))
    elif option == 3:
        
        leak ()
        dork ()
        scan ()

        print("End execution!!")
        break


    elif option == 0:
        print ("Exit.....")
        break
    else:
        print("Invalid option")


