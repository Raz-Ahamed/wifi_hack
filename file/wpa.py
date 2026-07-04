#python 
#Youtube chanel name: Real tips & trikes 660
#wifi_hack 
#wps_hack 
#start 
import os
import sys
import time

print('Chack Update')
os.system('git pull')
os.system('clear')

# কালার ভেরিয়েবল
reset="\033[0m"         # Reset/Default Color
black="\033[0;30m"      # Black
red="\033[0;31m"        # Red
green="\033[0;32m"      # Green
yellow="\033[0;33m"     # Yellow
blue="\033[0;34m"       # Blue
purple="\033[0;35m"     # Purple
cyan="\033[0;36m"       # Cyan
white="\033[0;37m"      # White

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
        continue # আবার প্রথম থেকে রান হবে
        
    elif are == 'n':
        os.system('clear')
        os.system('figlet -f big Thanks |lolcat')
        time.sleep(2) # টার্মিনাল কাটার আগে ২ সেকেন্ড 'Thanks' লেখাটি দেখাবে
        os.system('kill -9 $PPID') # এটি মূল টার্মিনাল উইন্ডোটি পুরোপুরি ক্লোজ করে দেবে
        sys.exit()
        
    else:
        print(red + "Invalid Input! Exiting..." + reset)
        sys.exit()
