#!/usr/bin/env python3
import numpy as np
import unittest

def submatriu_exacta(M, i_first,i_last,j_first,j_last, k):
    return(np.sum(M[i_first:i_last+1, j_first:j_first+1])==k)

def reduccio_CI_a_SE(M):
    rows = M.shape[0]
    columns = M.shape[1]
    for j in range(columns):
        if j+1 == columns:
            break
        equals = True
        for i in range(rows):
            if not submatriu_exacta(M,i,i,j,j,M[i,j+1]):
                equals = False    
                continue
        if equals == True:
            return True
    return False

class Test_reduccio_CI_a_SE(unittest.TestCase):
    M = np.array([
        [6,1,1],
        [7,2,2],
        [9,3,3]
    ])

    N = np.array([
        [99,92,1],
        [99,97,2],
        [99,97,3]
    ])

    Q = np.array([
        [99,92,1,0,0],
        [99,97,2,0,0],
        [99,97,3,0,0]
    ])
    R = np.array([
        [99,92,1,0,0],
        [99,97,2,0,3],
        [99,97,3,0,0]
    ])
    def test_redducio_cas_valid(self):
        self.assertTrue(reduccio_CI_a_SE(self.M))

    def test_redducio_cas_valid_3x5(self):
        self.assertTrue(reduccio_CI_a_SE(self.Q))

    def test_reduccio_cas_invalid(self):
        self.assertFalse(reduccio_CI_a_SE(self.N), "case should return false")

    def test_reduccio_cas_invalid_3x5(self):
        self.assertFalse(reduccio_CI_a_SE(self.R), "case should return false")
class Test_submatriu_exacta(unittest.TestCase):

    M1 = np.array([
        [3,2,1],
        [6,7,2],
        [2,7,3]
    ])
    n = M1.shape[0]
    N1 = np.array([
        [3,2,1],
        [6,7,2],
        [2,7,3]
    ])
    def test_submatriu_cas_valid_1_element(self):
        self.assertTrue(submatriu_exacta(self.M1,1,1,1,1,7))

    def test_submatriu_cas_valid_1col(self):
        self.assertTrue(submatriu_exacta(self.M1,0,self.n,0,0,11))

    def test_submatriu_cas_valid_2col(self):
        self.assertTrue(submatriu_exacta(self.M1,0,self.n,1,1,16))

    def test_submatriu_cas_valid_3col(self):
        self.assertTrue(submatriu_exacta(self.M1,0,self.n,2,2,6))

    def test_submatriu_cas_invalid(self):
        self.assertFalse(submatriu_exacta(self.N1,0,self.n,0,0,24))

if __name__ == "__main__":
    unittest.main()