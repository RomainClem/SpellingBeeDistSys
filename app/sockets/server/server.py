import socket
import threading
from time import sleep
import pika
import json
# Consume data from Rabbit mq

class ClientThread(threading.Thread):

    def __init__(self, client_address, client_socket, identity):
        threading.Thread.__init__(self)
        self.c_socket = client_socket
        print("Connection no. " + str(identity))
        print("New connection added: ", client_address)
    
    
    def callback(self, channel, method, properties, body):
        print("From game server")
        print(f" [x] Received -> {json.loads(body)}")
        self.c_socket.send(bytes(json.loads(body), 'UTF-8'))
        
    
    def run(self):
        print("Connection from : ", clientAddress)
        while True:
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            # connection = pika.BlockingConnection(pika.ConnectionParameters('server'))
            channel = connection.channel()
            channel.queue_declare(queue='player-stats')
            channel.basic_consume(queue='player-stats',
                                auto_ack=True,
                                on_message_callback=self.callback)

            print(' [*] Waiting for messages. To exit press CTRL+C')
            channel.start_consuming() 
        print("Client at ", clientAddress, " disconnected...")



# Server

LOCALHOST = "127.0.0.1"
# LOCALHOST = "0.0.0.0" # Used for Docker
PORT = 64001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))

print("Server started")
print("Waiting for client request..")

counter = 0

while True:
    server.listen(1)
    my_socket, clientAddress = server.accept()
    counter = counter + 1
    new_thread = ClientThread(clientAddress, my_socket, counter)
    new_thread.start()