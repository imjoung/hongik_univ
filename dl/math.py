import math

def sigmoid(x, deff=False):
  if deff:
    return sigmoid(x)*(1-sigmoid(x))
  else:
    return 1 / (1 + math.exp(-x))
