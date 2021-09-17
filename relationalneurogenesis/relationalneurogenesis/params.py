# Project   : Relational Neurogenesis
# Author    : Tej Pandit
# Date      : April 2021
# File      : params.py
# Info      : Collect parameters from neural network (weights & activations)


class Params:
    def __init__(self, weights, activations, score, mechanisms, rules, thresholds, verbose):
        self.weights = weights
        self.activations = activations
        self.score = score
        self.mechanisms = mechanisms
        self.rules = rules
        self.thresholds = thresholds
        self.verbose = verbose

    def getweights (self):
        print('weights')
