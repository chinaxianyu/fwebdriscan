#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import sys
print("""
 _____              _         _ _                          
|  ___|_      _____| |__   __| (_)_ __ ___  ___ __ _ _ __  
| |_  \ \ /\ / / _ \ '_ \ / _` | | '__/ __|/ __/ _` | '_ \ 
|  _|  \ V  V /  __/ |_) | (_| | | |  \__ \ (_| (_| | | | |
|_|     \_/\_/ \___|_.__/ \__,_|_|_|  |___/\___\__,_|_| |_|
                                                           

""")
try:
	urldir=sys.argv[1]
	filename=sys.argv[2]
	filedir=open(filename)
	for line in filedir.readlines():
	        df=line.strip("\n")
       		url=str(urldir+df)
        	web_status=requests.get(url)
     		A=web_status.status_code
        	A=str(A)
        	print("[+] DIR: "+url+"      STATUS:"+A+"")

except:
	print("[!]Error!")
	print("""\n\n[-]Help:
参数:
	fwebdirscan.py [url (all: http or https)]  [ file ]

Exmaple:
	fwebdirscan.py http://www.sg95.cn dir.txt
""")

