import threading
import socket

host ='127.0.0.1'
port = 55055

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))

server.listen()

clients = []
nick_names = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nick_name = nick_names[index]
            broadcast(f'{nick_name} left the chat!'.encode('ascii'))
            nick_names.remove(nick_name)
            break

def recieve():
    while  True:
        client, address = server.accept()
        print(f"connected with {str(address)}")

        client.send('NICK'. encode('ascii'))
        nick_name = client.recv(1024).decode('ascii')
        nick_names.append(nick_name)
        clients.append(client)

        print(f'Nickname of client is {nick_name}!')
        broadcast(f' {nick_name} joined the chat!'.encode('ascii'))
        client.send('connected to the server!'.encode('ascii'))


        thread = threading.Thread(target = handle_client, args=(client,))
        thread.start()
print('server is listening')
recieve()




