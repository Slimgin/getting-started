#! /usr/bin/env python


input_ip = raw_input("Please input an IP address: ")
octet = input_ip.split(".")

if int(octet[0]) == 10:
    print ("This is a Class A Private Network")
	
elif int(octet[0]) == 172 and 16 <= int(octet[1]) <= 31:
    print ("This is a Class B Private Network")
	
elif int(octet[0]) == 192 and int(octet[1]) == 168:
	print ("This is a Class C Private Network")

else:
   print ("This is a Public IP Address")

#print octet[0]

#print type(octet[0])

