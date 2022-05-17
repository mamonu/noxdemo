import pandas as pd
import numpy as np
import scipy as sp



# Create a dataframe
def create_df():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    return df


# Create a numpy array
def create_arr():
    return np.array([[1, 2], [3, 4]])


# Create a scipy sparse matrix
def create_sp_mat():
    return sp.sparse.csr_matrix([[1, 2], [3, 4]])
