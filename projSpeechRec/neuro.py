# -*- coding: utf-8 -*-
"""
Created on Thu May  4 22:32:14 2023

@author: Proph
"""

import numpy as np
import data

def sigmoid(x):                                        
  return 1 / (1 + np.exp(-x))

np.random.seed(1)

synaptic_weights = 2 * np.random.random((30,1)) - 1

for i in range(100000):
    input_layer = data.training_inputs
    outputs = sigmoid( np.dot(input_layer, synaptic_weights) )
    
    err = data.training_otputs - outputs
    
    adjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))
    
    synaptic_weights += adjustments
    
    
    
def find_command(x):
    new_inputs = np.array(data.adapt(x))

    outputs = sigmoid( np.dot(new_inputs, synaptic_weights) )
    #print(outputs)
    return outputs[0]