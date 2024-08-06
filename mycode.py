#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os 
import requests
import time
os.system("clear")


PEMBE = '\033[95m'
MAVİ = '\033[94m'
YESİL = '\033[92m'
SARI = '\033[93m'
KIRMIZI = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


print(KIRMIZI + """
  	
	.88b  d88. d8888b.    d88888D d88888b  .o88b. 
	88'YbdP`88 88  `8D    YP  d8' 88'     d8P  Y8 
	88  88  88 88oobY'       d8'  88ooooo 8P      
	88  88  88 88`8b        d8'   88~~~~~ 8b      
	88  88  88 88 `88. db  d8' db 88.     Y8b  d8 
	YP  YP  YP 88   YD VP d88888P Y88888P  `Y88P' 

1: Port Scan
2: Web Extension Browsing
3: Wordpress Scan
4: MD5 (hash)
5: SHA2-256 (hash)
6: FREE PROXY 
7: DDOS Attack
8: Test PROXY
-----------------------------
https://intagram.com/mr_zeec/
-----------------------------
""")

islem = input(BOLD+MAVİ+"The action you want to make? : ")

if(islem == "1"):
	ip = input("Enter Destination IP : ")
	os.system("nmap " + " -sC " + " -sV " + ip)

elif(islem == "2"):
	print("http://domain.com https://domain.com")
	web = input("Web sitesini giriniz: ")
	os.system("dirb " + web)

elif(islem == "3"):
	wp = input("Enter website : ")
	os.system("wpscan " + " --url " + wp)

elif(islem == "4"):
	hash = input("Enter HASH: ")
	os.system("hashcat " + "-m 0 " + " -a 0 " + hash + " " "/usr/share/wordlists/rockyou.txt")
	
elif(islem == "5"):
	has = input("Enter HASH : ")
	os.system("hashcat -m 1400 " " -a 0 " + " has " "/usr/share/wordlists/rockyou.txt")

elif(islem == "6"):
	print("LOADİND !")
	os.system("python3 proxy.py")
	print("File --> /root/Mrzec/proxy")

elif(islem == "7"):
	os.system("python2 ddos.py")

elif(islem == "8"):
	print(KIRMIZI + "If you haven't tried number 6 and want to test your own proxy list, please create a file named proxy in the Mrzec directory and list the IP and port addresses one below the other (you don't need to do this if you are going to test the proxies in this tool) ")	
	print(KIRMIZI + "Starting 3 sec!")
	time.sleep(3)
	os.system("python3 proxytest.py")
else:
	("ERROR !!!")
##Mr.zec https://intagram.com/mr_zeec/
	
