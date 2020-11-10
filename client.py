import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 55055))

nick_name = input("Enter your nick name: ")

def recieve():
	while True:
		try:
			message = client.recv(1024).decode('ascii')
			if message == 'NICK':
				client.send(nick_name.encode('ascii'))
			else:
				print(message)
		except:
			print('An error occurred!')
			client.close()
			break

def write():
	while True:
		message = f'{nick_name}:{input("")}'
		client.send(message.encode('ascii'))

recieve_thread = threading.Thread(target = recieve)
recieve_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start() 
