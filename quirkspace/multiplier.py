'''
File: multiplier.py
Author: Collin Farquhar
Description: Multiply gates and state vectors 

Note: I will take the "first bit" to mean the bit on the left of the binary
representation, to compliment the standard textbook representation
'''

from gates import *

# print functions
def print_vec(vec):
    f = lambda z : z.real if z.imag==0 else z
    print('\n'.join(['{:8.3}'.format(f(item)) for item in vec]))

def print_mat(mat):
    f = lambda z : z.real if z.imag==0 else z
    print('\n'.join([''.join(['{:8.3}'.format(f(item)) for item in row]) for row in mat]))

def multiply(gate_operations, n_qubits=2):
    composite_gate = np.identity(n_qubits**2)

    right_gate = gate_operations.pop(-1)
    while len(gate_operations) > 0:
        left_gate = gate_operations.pop(-1)
        mult_gates = [left_gate, right_gate]
        expanded_gates = []

        # expand gates
        for gate in mult_gates:
            if gate.qubit == 0:
                expanded_gate = gate.matrix
            else:
                expanded_gate = np.identity(2) 
            for n in range(n_qubits):
                if n == gate.qubit:
                    expanded_gate = np.kron(expanded_gate, gate.matrix)
                else:
                    expanded_gate = np.kron(expanded_gate, np.identity(2)) 
            expanded_gates.append(expanded_gate) 

        composite_gate = np.dot(expanded_gates[0], expanded_gates[1])
        right_gate = left_gate 

    return composite_gate

def main():
    X0 = quantum_gate(X, 0)
    X1 = quantum_gate(X, 1)
    c_gate = multiply([X0, X1], 2)
    print(c_gate)
    print(type(c_gate))

if __name__ == "__main__":
    main()
