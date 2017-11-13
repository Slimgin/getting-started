#! /usr/bin/env python3

import ipaddress

ipaddr_input = input('Please enter an IP Address in the form x.x.x.x/24: ')

ip_net =  ipaddress.ip_network(ipaddr_input, strict=False)
print ("The IP Network address is %s " % (ip_net[0]))


#print (ipaddr_input)