from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

# Example 1: |0> state
qc = QuantumCircuit(1)  # one qubit
state = Statevector.from_instruction(qc)
plot_bloch_multivector(state)
plt.show()

# Example 2: |+> state (Hadamard applied to |0>)
qc = QuantumCircuit(1)
qc.h(0)  # Apply Hadamard
state = Statevector.from_instruction(qc)
plot_bloch_multivector(state)
plt.show()

# Example 3: Custom rotation
qc = QuantumCircuit(1)
qc.rx(1.0, 0)  # Rotate around X axis by 1 radian
qc.ry(0.5, 0)  # Rotate around Y axis by 0.5 radian
state = Statevector.from_instruction(qc)
plot_bloch_multivector(state)
plt.show()
