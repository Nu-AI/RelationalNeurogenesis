# Decoder
# Decoding the Observation Values received from Unity Engine
# This is the Server Side Code

# Tej Pandit @digitej

import struct
import numpy

# Decoder Class to decode the received data from Unity Engine (observations)
class Decoder(object):

    # Load Config for Observations
    def __init__(self, config):
        self.config = config
        print(self.config)

        for i in range(len(self.config)):
            pass

    def decode(self, data):
        for i in range(len(self.config)):
            pass
        #return decoded_data