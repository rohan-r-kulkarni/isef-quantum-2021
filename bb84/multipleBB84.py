from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from numpy.random import randint
import numpy as np
# print("Imports Successful")

n = 10

entangled_sets = [[0, 2],[7,9]] #A+B ALREADY KNOW THIS (protocol)

def encode_message(qc, bits, bases):
    for i in range(n):
        if bases[i] == 0: # Prepare qubit in Z-basis
            if bits[i] == 0:
                pass # |0>
            else:
                qc.x(i) # |1>
        else: # Prepare qubit in X-basis
            if bits[i] == 0:
                qc.h(i) # |+>
            else:
                qc.x(i)
                qc.h(i) # |->
    return qc

def simple_entangle(qc, entangling):
    #correlated entanglement Bell-Pair Producer
    qc.h(entangling[0])
    qc.cx(entangling[0], entangling[1])

    return qc

def measure_message(qc, bases):
    backend = Aer.get_backend('qasm_simulator')
    measurements = [None]*n #create measurement list

    for j in range(n):
        if bases[j] == 0: # measuring in Z-basis
            qc.measure(j,j)
        if bases[j] == 1: # measuring in X-basis
            qc.h(j)
            qc.measure(j,j)
    result = execute(qc, backend, shots=1, memory=True).result()
    counts = result.get_counts(qc)
    sequence = str(next(iter(counts)))

    for k in range(n):
        measurements[k] = str(sequence[n-k-1])

    return measurements

def prep_entangle(alice_bits, alice_bases, entangling):
    #TEMP: Adjust for Alice polarizer to encode in simple Z basis
    #Bob measures in any basis. if incompatible, discarded. If both compatible, both will be correlated
    #if only one is compatible, the other will be appended
    alice_bases[entangling[0]] = 0
    alice_bases[entangling[1]] = 0
    alice_bits[entangling[0]] = 0
    alice_bits[entangling[1]] = 0

def remove_garbage(a_bases, b_bases, bits, entangling):
    output = []
    for q in range(n):
        if a_bases[q] != b_bases[q]:
            # If both did not use same basis,
            # change value to None
            #unless one of them is entangled
            if q == entangling[0]:
                print("b1 eliminated")
                output.append(False)
            elif q == entangling[1]:
                print("b2 eliminated")
                output.append(False)
            else:
                output.append(None)

        else:
            output.append(bits[q])

    return output

def adjust_entangle(bits, entangling):
    if (bits[entangling[0]] == False and bits[entangling[1]] != False):
        bits.append(bits[entangling[1]]+"*") #entangled, so states b1 = b2
        bits.pop(entangling[0])

    if (bits[entangling[1]] == False and bits[entangling[0]] != False):
        bits.append(bits[entangling[0]]+"*") #entangled, so states b1 = b2
        bits.pop(entangling[1])

    return bits

def clear_nones(sequence):
    output = []
    for q in range(len(sequence)):
        if sequence[q] == None or sequence[q] == False:
            pass
        else:
            output.append(sequence[q])

    return output

def bb84(n, entangled_bits):

    qc = QuantumCircuit(n,n)

    ## Step 1
    # Alice generates bits
    alice_bits = randint(2, size=n)


    ## Step 2
    # Create an array to tell us which qubits
    # are encoded in which bases
    alice_bases = randint(2, size=n)

    message = encode_message(qc, alice_bits, alice_bases)

    prep_entangle(alice_bits, alice_bases, entangled_bits)
    entangled = simple_entangle(message, entangled_bits)

    ## Step 3
    # Decide which basis to measure in:
    bob_bases = randint(2, size=n)
    #TEMP: Adjust for Bob polarizer to measure in simple Z basis
    # bob_bases[b1] = 0
    # bob_bases[b2] = 0

    bob_results = measure_message(entangled, bob_bases)

    #TEMP: Add in * to designate entangled bits
    bob_results[entangled_bits[0]] = str(bob_results[entangled_bits[0]])+"*"
    bob_results[entangled_bits[1]] = str(bob_results[entangled_bits[1]])+"*"

    new_alice_bits = []
    for i in range(0, len(alice_bits)):
        new_alice_bits.append(str(alice_bits[i]))

    print("Alice's Sequence:")
    print(new_alice_bits)

    print()
    print("BOB MEASURES:")
    print("Bob unfiltered:")
    print(bob_results)

    print("Length (should be n): " + str(len(bob_results)))

    # Step 4
    print()
    print("RESULTS:")

    alice_uncleared = remove_garbage(alice_bases, bob_bases, new_alice_bits, entangled_bits)
    print("Alice uncleared:")
    print(alice_uncleared)
    bob_uncleared = remove_garbage(alice_bases, bob_bases, bob_results, entangled_bits)
    print("Bob uncleared:")
    print(bob_uncleared)

    # STEP 5: Bob declaration and Alice adjustment
    print()
    alice_adjusted = adjust_entangle(alice_uncleared, entangled_bits)
    bob_adjusted = adjust_entangle(bob_uncleared, entangled_bits)
    print("Alice adjusted:")
    print(alice_adjusted)
    print("Bob adjusted:")
    print(bob_adjusted)

    alice_key = clear_nones(alice_adjusted)
    bob_key = clear_nones(bob_adjusted)

    print()
    print("FINAL:")
    print("Alice Key:")
    print(alice_key)
    print("Bob Key:")
    print(bob_key)
    print("Bob Key Length: " + str(len(bob_key)))
    print("Alice Key Length (should be same ^): " + str(len(alice_key)))

bb84(n, entangled_sets[0])
print()
print()
bb84(n, entangled_sets[1])
