#python 
#Youtube chanel name: Real tips & trikes 660
#wifi_hack 
#wps_hack 
#start 
import os
import sys
import time

# কালার ভেরিয়েবলগুলো এখানে রাখা হলো
reset="\033[0m"         
black="\033[0;30m"      
red="\033[0;31m"        
green="\033[0;32m"      
yellow="\033[0;33m"     
blue="\033[0;34m"       
purple="\033[0;35m"     
cyan="\033[0;36m"       
white="\033[0;37m"      

# ===================================================
# Auto Shortcut (Alias) Setup - এই অংশটুকু এখানে বসবে
# ===================================================
bashrc_path = os.path.expanduser("~/.bashrc")
alias_cmd = 'alias wifihack="python ~/wifi_hack/file/wpa.py"\n'

if os.path.exists(bashrc_path):
    with open(bashrc_path, "r") as f:
        content = f.read()
else:
    content = ""

if 'alias wifihack=' not in content:
    with open(bashrc_path, "a") as f:
        f.write("\n# Auto-generated alias for Wifi Hack tool\n")
        f.write(alias_cmd)
    
    print(green + "[+] Shortcut 'wifihack' has been added automatically!" + reset)
    print(yellow + "[!] Type 'source ~/.bashrc' or restart Termux after exiting to use the shortcut.\n" + reset)
    time.sleep(3) # মেসেজটি পড়ার জন্য ৩ সেকেন্ড সময় দেবে
# ===================================================


# এরপর থেকে আপনার আগের কোড শুরু হবে...
print('Chack Update')
os.system('git pull')
os.system('clear')

os.system('figlet -f big Wifi - Hack |lolcat')
print(green+'                      Version : 3.0 ' + reset)
print()
print(blue+'======================================================' + reset)
print(red+'Note: I wont be responsible fo any illigal activites.' + reset)
print(blue+'======================================================' + reset)
print()

#main.coding
#________________________________________
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

delay_print(green+'%37s' % '   |Devoloped By : Raz Ahamed|\n' + reset)
print()
print(red + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + reset)
print(blue + 'Youtube Chanel: Real  tips and Trikes 660' + reset)
print(blue + 'Telegarm Grop : https://t.me/realtips6600' + reset)
print(red + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + reset)

# লুপ শুরু
while True:
    print(green + 'Root chack.......' + reset)
    os.system('sudo python3 wifi_hack/file/wps.py -i wlan0 -K')
    
    # ইনপুট নেওয়া
    are = input(cyan + 'Are you continue (y/n):- ' + reset).strip().lower()
    
    if are == 'y':
        os.system('python3 wpa.py')
        continue
        
    elif are == 'n':
        os.system('clear')
        os.system('figlet -f big Thanks |lolcat')
        time.sleep(2) 
        os.system('kill -9 $PPID') 
        sys.exit() 
        
    else:
        print(red + "Invalid Input! Exiting..." + reset)
        time.sleep(2)
        os.system('kill -9 $PPID')
        sys.exit()
