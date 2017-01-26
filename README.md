# splunkpython

This python file is to be called by Splunk when there is actionable data, in this case an IP address, that you want auto blocked.  In this example it's creating a txt file that will be hosted via your choice of a dameon and then the firewall(Palo Alto in this case) can pull the file over for blocking.

Context for running the script.

"python3 splunk2pa.py insertIPaddressHere"

This script could easily be changed to facilitate iptables or other technologies as it fits your enviroment.

If you are running python3 this file should work as is, if you prefer python2 you will need to uncomment some varibles and comment others.  These are listed in the file

This script does some ip validation and basic error handling.

Be sure you create the txt file you want this file to append to or the script will fail.

Please feel free to contact me with any criticism you have.
