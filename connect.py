#!/usr/bin/python

# simulate ssh process
import sys
import getpass

def main():
	str=input("Are you sure you want to continue connecting (yes/no)?")
	while True:
		if str == "yes":
			break
		elif str == "no":
			print("Host key verification failed.")	
			sys.exit()
		else:
			str=input("Please type 'yes' or 'no':")
	
	
	for i in range(3):
		str=getpass.getpass("root@x.x.x.x's password:")
		if str == "123456":
			break
		else:
			if i != 2:
				print("Permission denied, please try again.")
			else:
				print("Connection closed by x.x.x.x")
				sys.exit()

	print(str)
		


#do		
if __name__ == "__main__":
	main()
else:
	pass
