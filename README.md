# splunkpython

This python file is to be called by Splunk when there is actionable data, in this case an IP address, that you want auto blocked.  In this example it's creating a txt file that will be hosted via your choice of a dameon and then the firewall(Palo Alto in this case) can pull the file over for blocking.

This script could easily be changed to facilitate iptables or other technologies as it fits your enviroment.

