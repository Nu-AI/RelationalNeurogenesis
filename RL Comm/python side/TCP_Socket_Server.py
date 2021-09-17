# TCP Socket Server
# A Socket Class using TCP/IP protocol to communicate with Unity Engine (applicable to any TCP really)
# This is the Server Side Code

# Tej Pandit @digitej

import socket

# Communication Socket Class
class CommunicationSocket(object):

    def __init__(self, port):
        # Input the Port Number for the Socket
        self.port = port
        self.connection = None
        self.client_address = None

        # Create Socket Object
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port - 8052
        server_address = ('localhost', self.port)
        print('Server Socket on %s port %s' % server_address)
        self.sock.bind(server_address)

    def start(self):
        # Listen for incoming connections
        self.sock.listen(1)

        # Wait until a connection is received
        while True:
            # Wait for a connection
            print('Waiting for Client.......')
            self.connection, self.client_address = self.sock.accept()

            # if connection successful
            if self.client_address is not None:
                print('Connected Client: ', self.client_address)
                break

    def stop(self):
        # Close the Connection Socket
        self.connection.close()

    def receiveData(self):
        try:
            if self.client_address is not None:
                data = None
                # Receive the data in small chunks and retransmit it
                while True:
                    data = self.connection.recv(4096)
                    if data is not None:
                        print('received "%s"' % data)
                        return data

        finally:
            # Close the connection
            self.connection.close()

    def sendData(self, data):
        self.connection.sendall(data)
