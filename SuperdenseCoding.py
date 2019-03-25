'''
    File: SuperdenseCoding.py
    Author: Collin Farquhar
    Description: An an example of superdense coding where two entangled qubits
        are entangled and then given separately to two parties (Alice and Bob). 
        
        Alice wants to send a two (classical) bit message to Bob and can do so by applying quantum
        operation to her qubit and sending it to Bob.

        Bob then measures the state of the two qubits to reveal the two
        classical bit message.

        There is no way to convey two bits of information with one classial
        bit. 
'''

from pyquil import Program
from pyquil import get_qc
from pyquil.gates import *

def entangle_qubits():
    """
        Paramaters:
            None
        Returns:
            p: ('pyquil.quil.Program') a pyquil Program to entangle qubits to
               the |+> Bell state 
    """

    p = Program()
    p += H(0)
    p += CNOT(0,1)

    return p

def Alice_Encode(p, cbits):
    """
        Paramaters:
            p: (pyquil.quil.Program) a pyquil Program that entangles qubits
            cbits: (string) the two classical bits that Alice wants to send to Bob
        Returns:
            p: (pyquil.quil.Program) a pyquil Program with Alice's operation on
               the entangled qubits
    """
    
    # Alice's quantum operation
    if cbits == '00':
        p += I(0)
    elif cbits == '01':
        p += X(0)
    elif cbits == '10':
        p += Z(0)
    elif cbits == '11':
        p += Z(0)
        p += X(0)
    else:
        exit("Invalid cbit string")

    return p

def Bob_measurement(p):
    """
        Paramaters:
            p: (pyquil.quil.Program) The program representing the operations done on the qubits
            after Alice's encodes the the information and sends her qubit to Bob
        Returns:
            p: (pyquil.quil.Program) The full superdense coding Program
            result: (np.ndarray) The result of Bob's measurement on the 2 qubits
    """

    p += CNOT(0,1)
    p += H(0)

    qc = get_qc("2q-qvm")
    #result = qc.run_and_measure(p, trials=10) 
    ro = p.declare('ro', 'BIT', 2)
    p += MEASURE(0, ro[0])
    p += MEASURE(1, ro[1])
    executable = qc.compile(p)
    result = qc.run(executable)

    return p, result

def main():
    print("First, we entangle two qubits and give one to Alice and one to Bob.")
    p = entangle_qubits()

    print("\nEnter the two classical bits Alice would like to send to Bob:")
    cbit_string = input("  Possiblities are {00, 01, 10, 11}: ")
    Alice_p = Alice_Encode(p, cbit_string)
    print("\nTo send those bits, alice applies the following quantum operations to her qubit:")
    print(Alice_p[2:])
    print("\nAlice sends her qubit to Bob.")

    p, result = Bob_measurement(Alice_p)
    print("\nBob applies the following quantum operations:")
    print(p[-5:-3])
    print("\nResult of Bob's measurement:")
    print(result)


if __name__ == '__main__':
    main()
