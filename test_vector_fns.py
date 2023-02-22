import vector_fns
import numpy as np

def test_vector_distance():
    # test the vector distance function
    assert vector_fns.vector_distance(np.ones(5),np.zeros(5)).round(2) == np.sqrt(5).round(2)
