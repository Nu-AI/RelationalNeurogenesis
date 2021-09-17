# Encoder
# Encoding the Action Values to match the receivers expected format
# This is the Server Side Code

# Tej Pandit @digitej

import struct
import numpy

# Encoder Class to encode data before transmitting (actions)
class Encoder(object):

    # Load Config for Actions
    def __init__(self, config):
        self.config = config
        print(self.config)

        for i in range(len(self.config)):
            pass

    def encode(self, data):
        for i in range(len(self.config)):
            pass
        #return encoded_data