#!/usr/bin/python
from scapy.all import *
import netaddr
network=raw_input("Enter the network address eg. 192.168.10.0/24 \n")
count=0
addresses=netaddr.IPNetwork(network)
for maa in addresses:
   if (maa==addresses.network or maa==addresses.broadcast):
     continue;
   resp=sr1(IP(dst=str(maa))/ICMP(),timeout=0.5,verbose=0)
   if str(type(resp))=="<type 'NoneType'>":
     print str(maa)+' is not responding'
   elif int(resp.getlayer(ICMP).type==3) and int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]:
       print str(maa)+' is blocking ping'
   else:
       print str(maa)+' is Live and responding'
       count += 1
print "Out of "+addresses.size+" the "+count+" are respoding"
