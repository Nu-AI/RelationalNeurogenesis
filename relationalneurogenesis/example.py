# Project   : Relational Neurogenesis
# Author    : Tej Pandit
# Date      : April 2021
# File      : example.py
# Info      : Example demonstrating the use of the Relational Neurogenesis framework
# Instr     : Follow all PART sections, (EXAMPLE sections only apply to this example)

'''
# INDEX -------------------------------------------------------
# Part-I    : Explains how to structure your network dimensions
# Part-II   : Explains how to structure your weight matrix
# Part-III  : Explains how to structure your activity matrix
# Part-IV   : Explains how to select neuro-evolutionary mechanisms
# Part-V    : Explains how to select rules to apply
# Part-VI   : Explains how to set thresholds
# Part-VII  : Explains how to execute relational neurogenesis
'''

import numpy as np
import relationalneurogenesis as rn

# Constants
input_dim = 4
output_dim = 4
init_hidden_layers = 3
min_nodes_per_layer = 4
max_nodes_per_layer = 10

# Variables
weights = []
activations = []
score = 0

'''
PART-I    : Explains how to structure your network dimensions
--------------------------------------------------------------

# network_dim = [input, hidden_1, hidden_2,.... hidden_N, output]
# network_dim = [4, 6, 7, 8, 4] ....for example
--------------------------------------------------------------
'''


# EXAMPLE: Generate random network architecture
network_dim = np.random.randint(max_nodes_per_layer-min_nodes_per_layer, size=init_hidden_layers) + min_nodes_per_layer
network_dim = np.insert(network_dim, 0, input_dim)
network_dim = np.append(network_dim, output_dim)
print(network_dim)

'''
PART-II   : Explains how to structure your weight matrix
--------------------------------------------------------------

NOTE: input to first hidden layer connections are preserved and not touched by the algorithm
NOTE: input to first hidden layer connections ARE included in weight matrix

Weight Matrix Structure (weight notation = w_X_Y  ,  X = current layer node,  Y = next layer node)
[
    connections from layer 1 (INPUT LAYER) to layer 2  (layer 1 = NA nodes, layer 2 = NB nodes)
    [   
        [ w_1_1   w_1_2   w_1_3   w_1_4....  w_1_NB  ]  <--input node 1
        [ w_2_1   w_2_2   w_2_3   w_2_4....  w_1_NB  ]  <--input node 2
        [ w_3_1   w_3_2   w_3_3   w_3_4....  w_1_NB  ]  <--input node 3
          :       :       :       :          :
        [ w_NA_1  w_NA_2  w_NA_3  w_NA_4...  w_NA_NB ]  <--input node NA
    ]
    
    connections from layer 2 to layer 3  (layer 2 = NB nodes, layer 3 = NC nodes)
    [
        [ w_1_1   w_1_2   w_1_3   w_1_4....  w_1_NC  ]  <--node 1
        [ w_2_1   w_2_2   w_2_3   w_2_4....  w_1_NC  ]  <--node 2
        [ w_3_1   w_3_2   w_3_3   w_3_4....  w_1_NC  ]  <--node 3
          :       :       :       :          :
        [ w_NB_1  w_NB_2  w_NB_3  w_NB_4...  w_NB_NC ]  <--node NB
    ]
    :
    :
    :
    
    connections from layer L-1 to layer L (OUTPUT LAYER) (layer L-1 = NY nodes, layer L = NZ output nodes)
    [
        [ w_1_1   w_1_2   w_1_3   w_1_4....  w_1_NZ  ]  <--node 1
        [ w_2_1   w_2_2   w_2_3   w_2_4....  w_1_NZ  ]  <--node 2
        [ w_3_1   w_3_2   w_3_3   w_3_4....  w_1_NZ  ]  <--node 3
          :       :       :       :          :
        [ w_NY_1  w_NY_2  w_NY_3  w_NY_4...  w_NY_NZ ]  <--node NY
    ]
]

To access weights simply use
WeightMatrix [layer where edge starts] [starting node] [ending node]  
--------------------------------------------------------------
'''

# EXAMPLE: Generate random weight matrix
for i in range(network_dim.size-1):
    layer = np.random.random((network_dim[i], network_dim[i+1]))
    weights.append(layer)

# print(weights)
# print(weights[1][2][3])

'''
PART-III  : Explains how to structure your activity matrix
--------------------------------------------------------------

Activity Matrix Structure (activation notation = a_L_N  ,  L = current layer number,  N = current layer node number)
[
    activations layer-wise
    [ a_1_1   a_1_2   a_1_3   a_1_4....  a_1_NA ]  <--layer 1  (having NA nodes) <--input layer (raw data inputs)
    [ a_2_1   a_2_2   a_2_3   a_2_4....  a_1_NB ]  <--layer 2  (having NB nodes)
    [ a_3_1   a_3_2   a_3_3   a_3_4....  a_1_NC ]  <--layer 3  (having NC nodes)
      :       :       :       :          :
    [ a_L_1   a_L_2   a_L_3   a_L_4....  w_L_NZ ]  <--layer L  (having NZ nodes) <--output layer (network outputs)
]

To access activations simply use
ActivityMatrix [layer] [node]
--------------------------------------------------------------
'''

# EXAMPLE: Generate random activity matrix
for i in range(network_dim.size):
    layer = np.random.random(network_dim[i])
    activations.append(layer)

# print(activations)
# print(activations[1][3])

'''
PART-IV   : Explains how to select neuro-evolutionary mechanisms
--------------------------------------------------------------
NEURO-EVOLUTIONARY MECHANISM LIST:

1 - NEUROGENESIS
2 - SYNAPTOGENESIS
3 - NEURON TERMINATION
4 - SYNAPSE TERMINATION

Select mechanisms:
mechanisms = [1, 3]         <-- for partial activation
mechanisms = [1, 2, 3, 4]   <-- for complete activation

Pass mechanisms as a parameter to the relational neurogenesis function
--------------------------------------------------------------
'''

# EXAMPLE: Select all mechanisms
mechanisms = [1, 2, 3, 4]

'''
PART-V    : Explains how to select rules to apply
--------------------------------------------------------------
MECHANISM RULE LIST:

A)  NEUROGENESIS
1 - plateauing merit
2 - learning opposing concepts
3 - low margin of confidence

B)  SYNAPTOGENESIS
4 - random exploration
5 - poor connectivity

C)  NEURON TERMINATION
6 - node not contributing
7 - identical activation

D)  SYNAPSE TERMINATION
8 - weight not contributing
9 - removal of nodes

Select mechanisms:
rules = [1, 2, 4, 6, 7]               <-- for partial activation
rules = [1, 2, 3, 4, 5, 6, 7, 8, 9]   <-- for complete activation

Pass rules as a parameter to the relational neurogenesis function
--------------------------------------------------------------
'''

# EXAMPLE: Select all rules
rules = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
PART-VI   : Explains how to set thresholds
--------------------------------------------------------------
THRESHOLD LIST:

A)  NEUROGENESIS
1 - plateauing merit
2 - learning opposing concepts
3 - low margin of confidence

B)  SYNAPTOGENESIS
4 - random exploration
5 - poor connectivity

C)  NEURON TERMINATION
6 - node not contributing
7 - identical activation

D)  SYNAPSE TERMINATION
8 - weight not contributing -----------------------;
9 - removal of nodes                               |
                                                   |
                                                   |
threshold ID [  1,   2,   3,   4,   5,   6,   7,   8,   9]

Set Thresholds: 
thresholds = [0.6, 0.0, 0.7, 0.0, 0.5, 0.6, 0.0, 0.0, 0.2]   <-- for partial control
thresholds = [0.6, 0.3, 0.7, 0.6, 0.5, 0.6, 0.7, 0.8, 0.5]   <-- for complete control

NOTE: These are EXAMPLE thresholds, FIND YOUR OWN
NOTE: THRESHOLDS are highly sensitive to the dataset/environment

Pass rules as a parameter to the relational neurogenesis function
--------------------------------------------------------------
'''

# EXAMPLE: Set your thresholds
thresholds = [0.6, 0.3, 0.7, 0.6, 0.5, 0.6, 0.7, 0.8, 0.5]
# NOTE: These are EXAMPLE thresholds, FIND YOUR OWN
# NOTE: THRESHOLDS are highly sensitive to the dataset/environment

'''
PART-VII  : Explains how to execute relational neurogenesis
--------------------------------------------------------------
# Create Relational Neurogenesis object
RN = rn.RelationalNeurogenesis(weights, activations, score)

# Execute Relational Neurogenesis after passing params and constraints
# This function is called every cycle/epoch (or every N cycles/epochs)
RN.relationalneurogenesis()
--------------------------------------------------------------
'''

# EXAMPLE: Create Relational Neurogenesis object
RN = rn.RelationalNeurogenesis(weights, activations, score)

# EXAMPLE: Execute Relational Neurogenesis after passing params and constraints
RN.relationalneurogenesis()



