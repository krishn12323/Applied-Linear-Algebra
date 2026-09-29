from vec import Vec
import time


# Vector sizes from 2K to 64K
sizes = [2000, 4000, 8000, 16000, 32000, 64000]

# Number of times each operation is repeated
trials = 5

print("Performance of Vec operations")
print("-" * 80)
print(f"{'Size':>8} {'Addition':>12} {'Subtraction':>12} "
      f"{'Scalar Mul':>12} {'Negation':>12} {'Norm':>12}")

for n in sizes:

    # Create two random vectors
    v1 = Vec.uniform(n)
    v2 = Vec.uniform(n)

    # ---------------- Addition ----------------
    start = time.perf_counter()

    for _ in range(trials):
        v1 + v2

    end = time.perf_counter()
    add_time = (end - start) / trials

    # ---------------- Subtraction ----------------
    start = time.perf_counter()

    for _ in range(trials):
        v1 - v2

    end = time.perf_counter()
    sub_time = (end - start) / trials

    # ---------------- Scalar Multiplication ----------------
    start = time.perf_counter()

    for _ in range(trials):
        2 * v1

    end = time.perf_counter()
    mul_time = (end - start) / trials

    # ---------------- Negation ----------------
    start = time.perf_counter()

    for _ in range(trials):
        -v1

    end = time.perf_counter()
    neg_time = (end - start) / trials

    # ---------------- Norm ----------------
    start = time.perf_counter()

    for _ in range(trials):
        v1.norm()

    end = time.perf_counter()
    norm_time = (end - start) / trials

    # Display results
    print(
        f"{n:>8} "
        f"{add_time:>12.6f} "
        f"{sub_time:>12.6f} "
        f"{mul_time:>12.6f} "
        f"{neg_time:>12.6f} "
        f"{norm_time:>12.6f}"
    )