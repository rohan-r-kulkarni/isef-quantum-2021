import numpy as np
from qiskit import QuantumCircuit, IBMQ, transpile, execute
from qiskit.visualization import plot_histogram, plot_gate_map, plot_circuit_layout
from qiskit.tools.monitor import job_monitor
from qiskit.compiler import transpile, assemble
import matplotlib.pyplot as plt

IBMQ.load_account()

#build circuit:
circuit = QuantumCircuit(3, 3)
circuit.h(0)
circuit.measure(0, 0)

#execute circuit:
provider = IBMQ.get_provider(hub='ibm-q')
backend = provider.get_backend('ibmq_qasm_simulator')

job_exp = execute(circuit, backend=backend, shots=1024)

# mapped_circuit = transpile(circuit, backend=backend)
# qobj = assemble(mapped_circuit, backend=backend, shots=1024)
# job = backend.run(qobj)
print(job)
#get results:
# result = job.result()
# counts = result.get_counts()
# print(result)

# plot_circuit_layout(new_circ_lv3, backend)
