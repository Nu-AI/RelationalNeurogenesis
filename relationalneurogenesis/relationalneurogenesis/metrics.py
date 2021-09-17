# Project   : Relational Neurogenesis
# Author    : Tej Pandit
# Date      : April 2021
# File      : metrics.py
# Info      : Calculate all complex metrics


class Metrics:
    def __init__(self, weights, activations, score, mechanisms, rules, thresholds, verbose):
        self.weights = weights
        self.activations = activations
        self.score = score
        self.mechanisms = mechanisms
        self.rules = rules
        self.thresholds = thresholds
        self.verbose = verbose

    def plateauingmerit (self, score, mechanisms, rules, thresholds, verbose):
        print('rel gen')
