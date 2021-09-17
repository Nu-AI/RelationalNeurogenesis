# Configuration Receiver
# Receives and saves the configuration settings from Unity Engine
# This is the Server Side Code

# Tej Pandit @digitej

import numpy

class ConfigReceiver(object):

    def __init__(self, sock):
        self.sock = sock

    def start(self):
        # Request Configuration from Unity Engine
        self.sock.sendData("config")
        print("Configuring.....")

        # Observations
        configObs = []
        text = self.sock.receiveData()
        if text == "observations":
            text = self.sock.receiveData()
            data = text.split("=")
            if data[0] == "segments":
                n = int(data[1])
            else:
                n = 1
            configObs.append([] for i in range(n))
            for i in range(0, n):
                text = self.sock.receiveData()
                data = text.split(",")
                # Segment Data Name
                configObs[i].append(data[0])
                # Data Type
                configObs[i].append(data[1])
                # Dimensions
                configObs[i].append(data[2].split("x"))

        # Actions
        configActs = []
        text = self.sock.receiveData()
        if text == "actions":
            text = self.sock.receiveData()
            data = text.split("=")
            if data[0] == "segments":
                n = int(data[1])
            else:
                n = 1
            configActs.append([] for i in range(n))
            for i in range(0, n):
                text = self.sock.receiveData()
                data = text.split(",")
                # Segment Data Name
                configActs[i].append(data[0])
                # Data Type
                configActs[i].append(data[1])
                # Dimensions
                configActs[i].append(data[2].split("x"))

        # Return the Observation and Action Configurations as Lists
        return configObs, configActs
