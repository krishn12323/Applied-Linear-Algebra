from vec import Vec

v1 = Vec([1, 2, 3])
v2 = Vec([4, 5, 6])

print("v1 =", v1)
print("v2 =", v2)

print("Addition:", v1 + v2)
print("Subtraction:", v1 - v2)
print("Scalar multiplication:", 2 * v1)

v1 += v2
print("After += :", v1)

print("Negative:", -v1)

print("Length:", len(v1))

print("Zeros:", Vec.zeros(5))
print("Ones:", Vec.ones(5))
print("Uniform:", Vec.uniform(5))

print("Norm:", v1.norm())