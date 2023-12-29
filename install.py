#install pkg 
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White
import os
import sys
import time
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)
delay_print(green+'Update...........')
os.system('termux-setup-storage')
os.system('apt upgrade -y')
os.system('apt update -y')
os.system("apt install -y root-repo -y")
os.system("apt install -y tsu wpa-supplicant pixiewps iw")
os.system("pkg install -y root-repo")
os.system("pkg install -y git tsu python wpa-supplicant pixiewps iw")
os.system("pkg install aircrack-ng -y")
#success..........
os.system('clear')
import sys
import time
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)
delay_print(green+'successfully update...')
os.system('python3 wifi.py')


