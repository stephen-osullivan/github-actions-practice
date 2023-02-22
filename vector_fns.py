import numpy as np

def vector_distance(x : np.array, y : np.array):
    #computes distance between two vectors
    sq_diff  = (x-y)**2
    return np.sqrt(sq_diff.sum())