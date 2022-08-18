#!/usr/bin/env python
# coding: utf-8

# In[1]:


''' *Q1) Create a sequence of a given length from a given start point, where the difference between 2 consecutive elements of the 
    expected sequence is also given as step.'''

"Ans="

import numpy as np
def seq(start, length, step):
    ''' start, length and step are in form of integers all representing the attributes as their names suggest
        output -> A numpy array is expected to be returned'''

    # YOUR CODE GOES HERE
    end = (start+(length-1)*step)+1
    if start < 0 :
        end = end -2
    sequence = np.arange(start,end,step)
    
    return sequence

seq(1,5,2)


# In[10]:


'''*Q2) Given an array in form of a matrix of size (n, n), rotate the matrix clockwise by 90º.'''

"Ans="

import numpy as np
def rotate_img(mat):
    '''mat -> A 2d numpy array
       output -> A 2d numpy array is expected to be returned'''

    x=mat.T
    for i in range(len(x)):
        x[i]=x[i,::-1]
    return x    

mx1 = [[1,2,3],[4,5,6],[7,8,9]]
mx1=np.array(mx1)
rotate_img(mx1)


# In[9]:


'''*Q3) Problem Description:

Given a M x N array,

Perform the following operation:

1. Get the odd rows from the array i.e. 1st, 3rd, 5th etc..

2. Convert the above result into 1D array and return it.'''

"Ans="

import numpy as np
def indexing(arr):
    '''
    INPUT: 
    arr -> 2D array of shape M x N
    
    OUTPUT: 
    result -> 1D array
    '''
    
    result = None
    
    
    ## Step 1: Get the odd rows from the array

    new=arr[::2]
    
    
    ## Step 2: Convert it to 1D array
    
    result = new.flatten()
    
    
    ## YOUR CODE ENDS HERE. MAY THE FORCE BE WITH YOU.
    
    return result

mx2 = [[1,2,3],[4,5,6],[7,8,9]]
mx2=np.array(mx2)
indexing(mx2)


# In[8]:


'''*Q4) Problem Statement:

Given a 2d array, write a program to return a subarray such that the subarray consists of the elements from:

1. the second to the fourth row of the original array,

2. the elements in these rows should be from the last three columns of the corresponding rows of the original array,

3. the rows should be in reversed order.'''

"Ans="

import numpy as np


def extract_subarray(arr):
    '''
    INPUT: arr -> 2D array
    
    OUPUT: result -> 2D array
    '''
    
    ### STEP1: Get the rows & cols 

    new = arr[1:4:,-3::]
    
    
    
    
    
    
    
    #### STEP2: Reverse the rows in cols array
    
    result = new[::-1]
    

    return result

mx3 = [[ 0,  1,  2,  3],  
 [ 4,  5,  6,  7],   
 [ 8,  9, 10, 11],   
 [12, 13, 14, 15],   
 [16, 17, 18, 19]]
mx3=np.array(mx3)
extract_subarray(mx3)


# In[ ]:




