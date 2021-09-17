# Main Controller
# Ties the Learning Engine to Unity Engine and uses the TCP socket library
# This is the Server Side Code

# Tej Pandit @digitej

import sys
import numpy
from TCP_Socket_Server import CommunicationSocket
from ConfigReceiver import ConfigReceiver
from Decoder import Decoder
from Encoder import Encoder

# Create a Communication Socket Class object and Specify the Port Number - 8052
sock = CommunicationSocket(8052)

# Start the Socket
sock.start()

# Create a Configuration Object
configRec = ConfigReceiver(sock)

# Receive the Configuration Settings
configObs, configActs = configRec.start()

# Create a Decoder to decipher the incoming data (observations)
decoder = Decoder(configObs)

# Create an Encoder to encode the data before transmitting (actions)
encoder = Encoder(configActs)

# Send some Data
sock.sendData("Meow")

# Receive some Data
data = sock.receiveData()

print(data)
