# -*- coding: utf-8 -*-
"""
Created on Wed May  2 10:01:12 2018

@author: MorJ
"""

import numpy as np
import time

def test_run1():
    print (np.array([[1, 2, 3],[2, 4, 6]]))
    print (np.empty([5,4]))
    print (np.ones([5,4],dtype=int))
    print (np.random.random([5,4]))
    print (np.random.normal(20,100,size=(2,3)))
    print (np.random.randint(0,10,size=10), "\n")
    
    a = np.random.random([5,4])
    
    print (a)
    print (a.shape)
    print ("Dim of array =", len(a.shape))
    print ("Rows =", a.shape[1])
    print ("Cols =", a.shape[0])
    print ("Size =", a.size)
    print ("Dtype=", a.dtype)
    
    np.random.seed(693)
    a = np.random.randint(0,10, size=(5,4))
    print ("Array: \n", a)
    print ("Summ of the array:" , a.sum())
    
    print ("Summ of the rows:" , a.sum(1))
    print ("Summ of the columns:" , a.sum(0))
    
    print ("Min of the rows:" , a.min(1))
    print ("Max of the columns:" , a.max(0))
    print ("Mean of all elements:" , a.mean())
    
def get_max_index(a):
    """Return the index of the maximum value in given 1D array."""
    # TODO: Your code here
    return np.argmax(a)


def test_run():
    t1 = time.time()
    print ("ML4T")
    t2 = time.time()
    print ("The time taken by pritn statement is ",t2-t1," seconds")
    a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32)  # 32-bit integer array
    print ("Array:", a)
    # Find the maximum and its index in array
    print ("Maximum value:", a.max())
    print ("Index of max.:", get_max_index(a)) 
    
    
if __name__ == "__main__":
    test_run()