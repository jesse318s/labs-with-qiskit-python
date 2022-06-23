from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, IBMQ
from qiskit.tools.monitor import job_monitor

# Assigns simulation provider if account is active, else enables account before assigning simulation provider
if (IBMQ.active_account()):
    print('Account active.\n')
    provider = IBMQ.get_provider(hub='ibm-q')
else:
    print('Enabling account...')
    IBMQ.enable_account('ENTER API TOKEN HERE')
    print('Account active.\n')
    provider = IBMQ.get_provider(hub='ibm-q')
    
# Initializes quantum circuit
qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

# Applies hadamard gate to all qubits
circuit.h(qreg_q)

# Measures all qubits
circuit.measure(qreg_q, creg_c)

# Runs circuit on QASM simulator once
backend = provider.get_backend('ibmq_qasm_simulator')
job = execute(circuit, backend, shots=1)

print('Executing job...')
job_monitor(job)
counts = job.result().get_counts()

print('RESULT: ', counts, '\n')