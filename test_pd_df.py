import demo
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix


def test_pd():
    result = demo.create_df()
    expected = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert result.equals(expected)


def test_np():
    # Create a numpy array

    expected = np.array([[1, 2], [3, 4]])
    result = demo.create_arr()

    assert np.array_equal(result, expected)


def test_scipy():
    expected = csr_matrix([[1, 2], [3, 4]])
    result = demo.create_sp_mat()
    assert (expected != result).nnz == 0

    
