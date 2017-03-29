#!/usr/bin/python

# simulate ssh process
import sys
import getpass

str=input("Are you sure you want to continue connecting (yes/no)?")
while True:
	if str == "yes":
		break
	elif str == "no":
		print("Host key verification failed.")	
		sys.exit()
	else:
		str=input("Please type 'yes' or 'no':")

str=getpass.getpass("root@x.x.x.x's password:")
if str != "123456":
	print("Connection closed by x.x.x.x")
print(str)
		

