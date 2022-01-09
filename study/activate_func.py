import numpy as np
def step(x):
    if x > 0:
        return 1
    else:
        0

def sigmoid(x):
    y = 1 / (1 + np.exp(-1))

def ReLU(x):
    return np.maximum(0,x)

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y
    


