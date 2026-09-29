
from vec import Vec
import numpy as np
import time


# Vector sizes from 2K to 64K
sizes = [2000, 4000, 8000, 16000, 32000, 64000]

# Number of repetitions
trials = 5

print("Custom Vec vs NumPy Performance")
print("-" * 100)
print(f"{'Size':>8} {'Vec Add':>12} {'NumPy Add':>12} "
      f"{'Vec Mul':>12} {'NumPy Mul':>12} "
      f"{'Vec Norm':>12} {'NumPy Norm':>12}")

for n in sizes:

    # Create random vectors
    v1 = Vec.uniform(n)
    v2 = Vec.uniform(n)

    # Create NumPy arrays with the same values
    a1 = np.array(v1.elements)
    a2 = np.array(v2.elements)

    # ---------------- Vec Addition ----------------
    start = time.perf_counter()

    for _ in range(trials):
        v1 + v2

    end = time.perf_counter()
    vec_add_time = (end - start) / trials


    # ---------------- NumPy Addition ----------------
    start = time.perf_counter()

    for _ in range(trials):
        a1 + a2

    end = time.perf_counter()
    numpy_add_time = (end - start) / trials


    # ---------------- Vec Scalar Multiplication ----------------
    start = time.perf_counter()

    for _ in range(trials):
        2 * v1

    end = time.perf_counter()
    vec_mul_time = (end - start) / trials


    # ---------------- NumPy Scalar Multiplication ----------------
    start = time.perf_counter()

    for _ in range(trials):
        2 * a1

    end = time.perf_counter()
    numpy_mul_time = (end - start) / trials


    # ---------------- Vec Norm ----------------
    start = time.perf_counter()

    for _ in range(trials):
        v1.norm()

    end = time.perf_counter()
    vec_norm_time = (end - start) / trials


    # ---------------- NumPy Norm ----------------
    start = time.perf_counter()

    for _ in range(trials):
        np.linalg.norm(a1)

    end = time.perf_counter()
    numpy_norm_time = (end - start) / trials


    # Display results
    print(
        f"{n:>8} "
        f"{vec_add_time:>12.6f} "
        f"{numpy_add_time:>12.6f} "
        f"{vec_mul_time:>12.6f} "
        f"{numpy_mul_time:>12.6f} "
        f"{vec_norm_time:>12.6f} "
        f"{numpy_norm_time:>12.6f}"
    )

