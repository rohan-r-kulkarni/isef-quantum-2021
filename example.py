#import relevant modules
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.visualization import *

#build quantum circuit
qc = QuantumCircuit(3,3)

qc.h(0)
qc.cswap(0,1,2)
qc.h(0)
qc.measure(0,0)

print("Number of Qubits:")
print(len(qc.qubits))

#measure circuit, map qubits to classical registers
# qc.measure(range(4), range(4))

# Execute the circuit on the qasm simulator
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1000)
# Grab results from the job
result = job.result()

# Return counts
counts = result.get_counts(qc)
print("\nResults: ",counts)

#Prints the first result in the counts map
print(next(iter(counts)))

#visualize in terminal
# print(qc)
qc.draw(output='mpl', filename='./out.png') #draws w/ color in file
# plot_histogram(counts).savefig("./out-graph.png") #draws w/ color in file
