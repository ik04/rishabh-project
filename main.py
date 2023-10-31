from qiskit import QuantumCircuit, Aer, execute

def quantum_coin_flip():
    # Create a quantum circuit with 1 qubit
    circuit = QuantumCircuit(1, 1)  # Add a classical bit for measurement

    # Apply a Hadamard gate to create superposition
    circuit.h(0)

    # Measure the qubit
    circuit.measure(0, 0)

    # Simulate the circuit using the Aer simulator
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots=1)
    result = job.result()

    # Get the measurement result (Heads or Tails)
    counts = result.get_counts(circuit)
    return list(counts.keys())[0]

def play_coin_flip_game():
    total_rounds = 5  # You can adjust the number of rounds
    wins = 0

    for round in range(1, total_rounds + 1):
        print(f"Round {round}:")
        result = quantum_coin_flip()
        print(f"The quantum coin landed on: {result}")

        if result == "0":
            wins += 1

    print(f"You won {wins} out of {total_rounds} rounds!")

play_coin_flip_game()
