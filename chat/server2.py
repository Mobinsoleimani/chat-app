import socket
import threading

# host = '127.0.0.1'
# port = 55555

server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 59000))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    if client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            client.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat '.encode('ascii'))
            nicknames.remove(nickname)
            break
def receive():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')
        client.send('NICK'.encode('ascii'))
        nicknames.append(nickname)
        clients.append(client)
        print('Nickname of the client is {nickname}')
        broadcast(f'{nicname} joined the chat '.encode('ascii'))
        client.send('connected to the server !'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
print("server is listing...")
receive()