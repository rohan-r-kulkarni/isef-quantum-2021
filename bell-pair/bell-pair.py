from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.visualization import *

# BUILD
#------

# Create a Quantum Circuit acting on the q register
qc = QuantumCircuit(2, 2)
#first param is number of qubits
#second param is number of classical registers

# Add a H gate on qubit 0
qc.h(0)
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
qc.cx(0, 1)

# Map the quantum measurement to the classical bits
measurement = QuantumCircuit(2, 2)
measurement.measure([0,1], [1,0]) #maps 0th qubit to 1st classical register, and vice versa

#append measurement gates to quantum circuit
circuit = qc + measurement

# EXECUTE
#--------

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')
# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=1000)
# Grab results from the job
result = job.result()

# Return counts
counts = result.get_counts(circuit)
print("\nResults: ",counts)

# ANALYZE + VISUALIZE
#--------

print(circuit) #draws in terminal
circuit.draw(output='mpl', filename='./circuit.png') #draws w/ color in file
plot_histogram(counts).savefig("./histogram.png") #draws w/ color in file

# END
