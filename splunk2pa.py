#!/usr/bin/python3

#Austin Parker austin@packet415.com
#This script allows the Splunk box to pass
#an IP to a txt file so it can be ingested
#into the Palo Alto for automated blocking

# you could easily modify this script for ip tables or whatever, if there
#is interest in this let me know and I can assist

#The txt file needs be served via http for the palo to ingest it

#place where appropriate for your enviroment

import os,sys
import ipaddress



#put the name of your output file below
outputfile = "splunk2paBlock.txt"

#if your file above doesn't exist the script will error, just to a touch command
#on a linux box on windows use notepad or whatever



ip = sys.argv[1]


#doing IP input validation for IPv4 and IPv6  
#Uncomment the iptuf varible and ipcheck(iputf) if python 2 and comment out ipcheck(ip)
#if python3 leave alone
#iputf = ip.decode('utf-8')
ipcheck = ipaddress.ip_address
#ipcheck(iputf)
ipcheck(ip)



# this is checking the file for the IP being passed, don't want duplicates
try:
    
    banfile = open(outputfile, 'r')
except (OSError,IOError):
        print("File " + (outputfile) + " missing or permissions wrong")
        exit()
knowniplist = banfile.readlines()
banfile.close()
found = False
for line in knowniplist:
    if str(ip) in line:
        print("IP " + (ip) + " already in file " + (outputfile) +", not writing a duplicate")
        found = True
        exit()


#if the IP passed isn't found it will append it to the end of the file
if not found:
    banfile = open(outputfile, 'a')
    banfile.write(str(ip)+"\n")
    banfile.close()
    print("IP was NOT found adding " + (ip) + " to the file " + (outputfile)) 

#Take that punch you miscreant