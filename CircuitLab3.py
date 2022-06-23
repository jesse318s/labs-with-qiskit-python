from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from numpy import pi
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram
from qiskit.visualization import plot_state_qsphere

qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[0])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.measure(qreg_q[0], creg_c[0])
circuit.h(qreg_q[0])
circuit.h(qreg_q[1])
circuit.measure(qreg_q[1], creg_c[0])

meas = QuantumCircuit(4, 4)
meas.barrier(range(4))
meas.measure(range(4), range(4))
qc = meas.compose(circuit, range(4), front=True)

backend = QasmSimulator()
qc_compiled = transpile(qc, backend)

job_sim = backend.run(qc_compiled, shots=1024)
result_sim = job_sim.result()
counts = result_sim.get_counts(qc_compiled)

job_sim2 = backend.run(qc_compiled, shots=512)
result_sim2 = job_sim2.result()
counts2 = result_sim2.get_counts(qc_compiled)

backendStatevector = BasicAer.get_backend('statevector_simulator')
result = backendStatevector.run(transpile(circuit, backendStatevector)).result()
psi  = result.get_statevector(circuit)

legend = ['First execution', 'Second execution']
plot_histogram([counts, counts2], legend=legend)

plot_state_qsphere(psi)