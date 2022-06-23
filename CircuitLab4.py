import numpy as np
from qiskit import *
from qiskit.circuit import Parameter
import matplotlib.pyplot as plt

theta = Parameter('θ')

n = 6

qc = QuantumCircuit(6, 1)

for i in range(n-1):
    if (i < 3):
        qc.h(i)
    qc.cx(i, i+1)

qc.barrier()
qc.rz(theta, range(6))
qc.barrier()

for i in reversed(range(n-1)):
    if (i > 1 and i < 4):
        qc.h(i+1)
    qc.cx(i+1, i)
        
qc.measure(0, 0)

theta_range = np.linspace(0, 2 * np.pi, 128)

circuits = [qc.bind_parameters({theta: theta_val})
            for theta_val in theta_range]
            
backend = BasicAer.get_backend('qasm_simulator')
job = backend.run(transpile(circuits, backend))
counts = job.result().get_counts()
qc.draw('mpl')

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.plot(theta_range, list(map(lambda c: c.get('0', 0), counts)), '.-', label='0')
ax.plot(theta_range, list(map(lambda c: c.get('1', 0), counts)), '.-', label='1') 
ax.set_xticks([i * np.pi / 2 for i in range(5)])
ax.set_xticklabels(['0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'], fontsize=14)
ax.set_xlabel('θ', fontsize=14)
ax.set_ylabel('Counts', fontsize=14)
ax.legend(fontsize=14)