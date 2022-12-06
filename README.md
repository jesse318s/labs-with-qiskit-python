# labs-with-qiskit-python

This is the Python code for functional quantum circuits, their test simulations, and the results. These programs were developed in a virtual Jupyter Notebook environment using the Qiskit kernel. <br />
Run your own labs here: https://quantum-computing.ibm.com/

<br />

# Descriptions and Results

- Algorithim Lab VQE Description:
  - "Variational algorithms in Qiskit, like VQE and QAOA, provide the option for a user to give a callback method that can be used to monitor optimization progress as     the algorithm runs and converges to the minimum. The callback is invoked for each functional evaluation by the optimizer and provides the current optimizer value,     evaluation count, current optimizer parameters etc. Note that, depending on the specific optimizer this may not be each iteration (step) of the optimizer, so for       example if the optimizer is calling the cost function to compute a finite difference based gradient this will be visible via the callback."
- Algorithim Lab VQE Results:
  - Energy Convergence: (https://github.com/jesse318s/python-quantum-information-labs/blob/main/LabImages/AlgorithimLabVQEImage1.webp?raw=true)
  - Reference Value: -1.85728
  - Energy Convergence with Reference: (https://github.com/jesse318s/python-quantum-information-labs/blob/main/LabImages/AlgorithimLabVQEImage2.webp?raw=true)

<br />

- Circuit Lab 1 Description:
  - A basic quantum circuit which maps the outcome of the qubits to classical bits.
- Circuit Lab 1 Results: 
  - Counts: {'001': 237, '010': 267, '000': 268, '111': 252}

<br />

- Circuit Lab 2 Description:
  - A basic quantum circuit which maps the outcome of the qubits to classical bits.
- Circuit Lab 2 Results: 
  - Counts: {'0000': 252, '0010': 252, '0001': 254, '0111': 266}

<br />

- Circuit Lab 3 Description:
  - A basic quantum circuit which maps the outcome of the qubits to classical bits. The qubit outcomes are plotted via histogram, and the qubit states are plotted via     q-sphere.
- Circuit Lab 3 Results: 
  - Histogram: (https://github.com/jesse318s/python-quantum-information-labs/blob/main/LabImages/CircuitLab3Image1.webp?raw=true)
  - State Q-Sphere: (https://github.com/jesse318s/python-quantum-information-labs/blob/main/LabImages/CircuitLab3Image2.webp?raw=true)

<br />

- Circuit Lab 4 Description:
  - A parameterized quantum circuit which maps the outcome of the qubits to classical bits. The qubit outcomes are plotted via theta range.
- Circuit Lab 4 Results:
  - Quantum Circuit: (https://github.com/jesse318s/python-quantum-information-labs/blob/main/LabImages/CircuitLab4Image1.webp?raw=true)
  - Theta Range: (https://github.com/jesse318s/python-quantum-information-labs/blob/main/LabImages/CircuitLab4Image2.webp?raw=true)

<br />

- Circuit Lab RNG Description:
  - A simple random number generating quantum circuit, which is run on the ibmq_qasm_simulator.
- Circuit Lab RNG Results:
  - Counts: {'1000': 1}
