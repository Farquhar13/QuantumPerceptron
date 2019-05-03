'''
File: gates.py
Author: Collin Farquhar
Description: Defining the basic quantum gates in matrix representation 

Note: I will take the "first bit" to mean the bit on the left of the binary
representation, to compliment the standard textbook representation

Note1: This is a work in progress. More gates to come!
'''

import numpy as np

class quantum_gate:
    def __init__(self, matrix, qubit=0, name=''):
        self.matrix = matrix
        self.qubit = qubit
        self.name = name

    def set_qubit(self, qubit):
        assert type(qubit) is int, "qubit type must be in"
        self.qubit = qubit

    def __str__(self):
        # currently just for gates
        f = lambda z : z.real if z.imag==0 else z
        title = self.name + " acting on qubit {} \n".format(self.qubit)
        return title + '\n'.join([''.join(['{:8.3}'.format(f(item)) for item in row])
                                                                    for row in self.matrix])

# Standard basis
zero = np.array([1, 0], dtype=np.double)
one = np.array([0, 1], dtype=np.double)

# Pauli gates
I = np.array([[1, 0], 
              [0, 1]], dtype=np.double)

X = np.array([[0, 1], 
              [1, 0]], dtype=np.double)

Y = np.array([[0, -1j], 
              [1j, 0]])

Z = np.array([[1, 0], 
              [0, -1]], dtype=np.double)

# Hadamard gate
Z = np.array([[1/np.sqrt(2), 1/np.sqrt(2)], 
              [1/np.sqrt(2), -1/np.sqrt(2)]], dtype=np.double)

# Controlled gates
CX = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 0, 1],
               [0, 0, 1, 0]], dtype=np.double)

CZ = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, -1]], dtype=np.double)


def print_vec(vec):
    f = lambda z : z.real if z.imag==0 else z
    print('\n'.join(['{:8.3}'.format(f(item)) for item in vec]))

def print_mat(mat):
    f = lambda z : z.real if z.imag==0 else z
    print('\n'.join([''.join(['{:8.3}'.format(f(item)) for item in row]) for row in mat]))

def main():
    print("zero")
    print_vec(zero)
    print("one")
    print_vec(one)
    print("I")
    print_mat(I)
    print("X")
    print_mat(X)
    print("Y")
    print_mat(Y)
    print("Z")
    print_mat(Z)
    print("CX")
    print_mat(CX)
    print("CZ")
    print_mat(CZ)

    print("X_gate")
    X_gate = quantum_gate(X, 0, "X")
    print(X_gate)

if __name__ == '__main__':
    main()
