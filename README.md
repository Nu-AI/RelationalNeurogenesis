# Relational Neurogenesis
Relational Neurogenesis is a framework that supports neuroevolutionary mechanisms in deep reinforcement learning networks to enhance lifelong learning capabilities.

Published Source : [Relational Neurogenesis for Lifelong Learning Agents](https://dl.acm.org/doi/10.1145/3381755.3381766)

Full Thesis : [Relational Neurogenesis for Lifelong Learning Agents](https://scholarworks.rit.edu/theses/10096/)

![](https://github.com/Nu-AI/Research_Tej_Pandit/blob/main/Relational%20Neurogenesis/RN_algorithm.png)

## Instructions
using relationalneurogenesis/example.py as a reference, you can instantiate and use components of the RN framework. 

| INDEX | EXPLANATION |
| ------ | ------ |
| Part-I | Explains how to structure your network dimensions |
| Part-II | Explains how to structure your weight matrix |
| Part-III | Explains how to structure your activity matrix |
| Part-IV | Explains how to select neuro-evolutionary mechanisms |
| Part-V | Explains how to select rules to apply |
| Part-VI | Explains how to set thresholds |
| Part-VII | Explains how to execute relational neurogenesis |

## Initialization

```python
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
```

## Part-I
_How to structure your network dimensions_
```
network_dim = [input, hidden_1, hidden_2,.... hidden_N, output]
network_dim = [4, 6, 7, 8, 4] ....for example
```

EXAMPLE: Generate random network architecture
```python
network_dim = np.random.randint(max_nodes_per_layer-min_nodes_per_layer, size=init_hidden_layers) + min_nodes_per_layer
network_dim = np.insert(network_dim, 0, input_dim)
network_dim = np.append(network_dim, output_dim)
print(network_dim)
```

## Part-II
_How to structure your weight matrix_

NOTE: input to first hidden layer connections are preserved and not touched by the algorithm<br />
NOTE: input to first hidden layer connections ARE included in weight matrix

```python
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
```
To access weights simply use
```python
WeightMatrix [layer where edge starts] [starting node] [ending node]
```

EXAMPLE: Generate random weight matrix
```python
for i in range(network_dim.size-1):
    layer = np.random.random((network_dim[i], network_dim[i+1]))
    weights.append(layer)

print(weights)
print(weights[1][2][3])
```

## Part-III
_How to structure your activity matrix_

```python
Activity Matrix Structure (activation notation = a_L_N  ,  L = current layer number,  N = current layer node number)
[
    activations layer-wise
    [ a_1_1   a_1_2   a_1_3   a_1_4....  a_1_NA ]  <--layer 1  (having NA nodes) <--input layer (raw data inputs)
    [ a_2_1   a_2_2   a_2_3   a_2_4....  a_1_NB ]  <--layer 2  (having NB nodes)
    [ a_3_1   a_3_2   a_3_3   a_3_4....  a_1_NC ]  <--layer 3  (having NC nodes)
      :       :       :       :          :
    [ a_L_1   a_L_2   a_L_3   a_L_4....  w_L_NZ ]  <--layer L  (having NZ nodes) <--output layer (network outputs)
]
```

To access activations simply use
```python
ActivityMatrix [layer] [node]
```

EXAMPLE: Generate random activity matrix
```python
for i in range(network_dim.size):
    layer = np.random.random(network_dim[i])
    activations.append(layer)

print(activations)
print(activations[1][3])
```

## Part-IV
_How to select neuro-evolutionary mechanisms_

NEURO-EVOLUTIONARY MECHANISM LIST:

1 - NEUROGENESIS<br />
2 - SYNAPTOGENESIS<br />
3 - NEURON TERMINATION<br />
4 - SYNAPSE TERMINATION<br />

Pass mechanisms as a parameter to the relational neurogenesis function
```
mechanisms = [1, 3]         <-- for partial activation
mechanisms = [1, 2, 3, 4]   <-- for complete activation
```

EXAMPLE: Select all mechanisms
```python
mechanisms = [1, 2, 3, 4]
```

## Part-V
_How to select rules_

MECHANISM RULE LIST:

A)  NEUROGENESIS<br />
1 - plateauing merit<br />
2 - learning opposing concepts<br />
3 - low margin of confidence

B)  SYNAPTOGENESIS<br />
4 - random exploration<br />
5 - poor connectivity

C)  NEURON TERMINATION<br />
6 - node not contributing<br />
7 - identical activation

D)  SYNAPSE TERMINATION<br />
8 - weight not contributing<br />
9 - removal of nodes

Pass rules as a parameter to the relational neurogenesis function
```
rules = [1, 2, 4, 6, 7]               <-- for partial activation
rules = [1, 2, 3, 4, 5, 6, 7, 8, 9]   <-- for complete activation
```

EXAMPLE: Select all rules
```python
rules = [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Part-VI
_How to set thresholds_

THRESHOLD LIST:

A)  NEUROGENESIS<br />
1 - plateauing merit<br />
2 - learning opposing concepts<br />
3 - low margin of confidence

B)  SYNAPTOGENESIS<br />
4 - random exploration<br />
5 - poor connectivity

C)  NEURON TERMINATION<br />
6 - node not contributing<br />
7 - identical activation

D)  SYNAPSE TERMINATION<br />
8 - weight not contributing<br />
9 - removal of nodes
```
threshold ID [  1,   2,   3,   4,   5,   6,   7,   8,   9]
```

Pass rules as a parameter to the relational neurogenesis function
```
thresholds = [0.6, 0.0, 0.7, 0.0, 0.5, 0.6, 0.0, 0.0, 0.2]   <-- for partial control
thresholds = [0.6, 0.3, 0.7, 0.6, 0.5, 0.6, 0.7, 0.8, 0.5]   <-- for complete control
```

NOTE: These are EXAMPLE thresholds, FIND YOUR OWN<br />
NOTE: THRESHOLDS are highly sensitive to the dataset/environment

EXAMPLE: Set your thresholds
```python
thresholds = [0.6, 0.3, 0.7, 0.6, 0.5, 0.6, 0.7, 0.8, 0.5]
```

## Part-VII
_How to execute relational neurogenesis_

Create Relational Neurogenesis object
```python
RN = rn.RelationalNeurogenesis(weights, activations, score, mechanisms, rules, thresholds)
```

Execute Relational Neurogenesis after passing params and constraints
```python
RN.relationalneurogenesis()
```
NOTE: This function is called every cycle/epoch (or every N cycles/epochs)
