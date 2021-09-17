# Project   : Relational Neurogenesis
# Author    : Tej Pandit
# Date      : April 2021
# File      : rn.py
# Info      : Main Relational Neurogenesis library

from relationalneurogenesis import params
from relationalneurogenesis import metrics
from relationalneurogenesis import threshold
from relationalneurogenesis import neurogenesis
from relationalneurogenesis import synaptogenesis
from relationalneurogenesis import neurondeath
from relationalneurogenesis import synapsedeath


class RelationalNeurogenesis:
    def __init__(self, weights, activations, score, mechanisms, rules, thresholds, verbose):
        self.weights = weights
        self.activations = activations
        self.score = score
        self.mechanisms = mechanisms
        self.rules = rules
        self.thresholds = thresholds
        self.verbose = verbose

    def relationalneurogenesis (self, weights, activations, score, mechanisms, rules, thresholds, verbose):
        self.weights = weights
        self.activations = activations
        self.score = score
        self.mechanisms = mechanisms
        self.rules = rules
        self.thresholds = thresholds
        self.verbose = verbose
        print('rel gen')

    def getweights (self):
        print(self.verbose)
