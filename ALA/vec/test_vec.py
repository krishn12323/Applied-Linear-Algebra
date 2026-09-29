from vec import Vec
import math


# -------------------------
# Vector creation
# -------------------------

v = Vec([1, 2, 3])
assert v.elements == [1, 2, 3]


# -------------------------
# Vector addition
# -------------------------

v1 = Vec([1, 2, 3])
v2 = Vec([4, 5, 6])
assert (v1 + v2).elements == [5, 7, 9]


# -------------------------
# Scalar multiplication
# -------------------------

v = Vec([1, 2, 3])
assert (2 * v).elements == [2, 4, 6]


# -------------------------
# In-place multiplication
# -------------------------

v = Vec([1, 2, 3])
v *= 2
assert v.elements == [2, 4, 6]


# -------------------------
# Length
# -------------------------

v = Vec([10, 20, 30])
assert len(v) == 3


# -------------------------
# Vector subtraction
# -------------------------

v1 = Vec([5, 6, 7])
v2 = Vec([1, 2, 3])
assert (v1 - v2).elements == [4, 4, 4]


# -------------------------
# Negation
# -------------------------

v = Vec([1, -2, 3])
assert (-v).elements == [-1, 2, -3]


# -------------------------
# Scalar addition
# -------------------------

v = Vec([1, 2, 3])
assert (5 + v).elements == [6, 7, 8]


# -------------------------
# In-place vector addition
# -------------------------

v1 = Vec([1, 2, 3])
v2 = Vec([4, 5, 6])

v1 += v2

assert v1.elements == [5, 7, 9]


# -------------------------
# zeros()
# -------------------------

assert Vec.zeros(4).elements == [0, 0, 0, 0]


# -------------------------
# ones()
# -------------------------

assert Vec.ones(4).elements == [1, 1, 1, 1]


# -------------------------
# uniform()
# -------------------------

v = Vec.uniform(5)

assert len(v) == 5
assert all(0 <= x <= 1 for x in v.elements)


# =========================================================
# NORM TESTS
# =========================================================

# Basic norm test
v = Vec([3, 4])
assert math.isclose(v.norm(), 5.0)


# Norm of zero vector
v = Vec([0, 0, 0])
assert math.isclose(v.norm(), 0.0)


# Norm should always be non-negative
v = Vec([-3, -4])
assert v.norm() >= 0


# Norm of negative vector should be same
v1 = Vec([3, 4])
v2 = Vec([-3, -4])

assert math.isclose(v1.norm(), v2.norm())


# Scaling property
# ||c*v|| = |c| * ||v||

v = Vec([3, 4])
scaled = 2 * v

assert math.isclose(
    scaled.norm(),
    2 * v.norm()
)


# =========================================================
# MEAN TESTS
# =========================================================

# Basic mean
v = Vec([2, 4, 6, 8])
assert math.isclose(v.mean(), 5.0)


# Negative numbers
v = Vec([-2, -4, -6])
assert math.isclose(v.mean(), -4.0)


# Single element
v = Vec([7])
assert math.isclose(v.mean(), 7.0)


# Constant vector
v = Vec([5, 5, 5])
assert math.isclose(v.mean(), 5.0)


# Translation property
# Adding 10 to every element increases mean by 10

v1 = Vec([1, 2, 3])
v2 = Vec([11, 12, 13])

assert math.isclose(
    v2.mean(),
    v1.mean() + 10
)


# Permutation should not change mean

v1 = Vec([1, 2, 3, 4])
v2 = Vec([4, 2, 1, 3])

assert math.isclose(
    v1.mean(),
    v2.mean()
)


# Empty vector mean should raise error

try:
    Vec([]).mean()
    assert False
except ValueError:
    pass


# =========================================================
# DEMEAN TESTS
# =========================================================

# Basic demean

v = Vec([2, 4, 6, 8])

result = v.demean()

assert result.elements == [-3, -1, 1, 3]


# Mean of demeaned vector should be zero

v = Vec([2, 4, 6, 8])

result = v.demean()

assert math.isclose(
    result.mean(),
    0.0,
    abs_tol=1e-5
)


# Single element

v = Vec([10])

assert v.demean().elements == [0]


# Constant vector

v = Vec([5, 5, 5])

assert v.demean().elements == [0, 0, 0]


# Demean should not modify original vector

v = Vec([2, 4, 6, 8])

original = v.elements.copy()

result = v.demean()

assert v.elements == original
assert result is not v


# Empty vector should raise error

try:
    Vec([]).demean()
    assert False
except ValueError:
    pass


# =========================================================
# STANDARD DEVIATION TESTS
# =========================================================

# Basic standard deviation

v = Vec([2, 4, 6, 8])

assert math.isclose(
    v.std(),
    math.sqrt(5)
)


# Single element standard deviation is zero

v = Vec([10])

assert math.isclose(
    v.std(),
    0.0
)


# Constant vector has standard deviation zero

v = Vec([5, 5, 5, 5])

assert math.isclose(
    v.std(),
    0.0
)


# Standard deviation must be non-negative

v = Vec([-2, 4, 6, 8])

assert v.std() >= 0


# Translation should not change standard deviation

v1 = Vec([1, 2, 3, 4])
v2 = Vec([11, 12, 13, 14])

assert math.isclose(
    v1.std(),
    v2.std()
)


# Permutation should not change standard deviation

v1 = Vec([1, 2, 3, 4])
v2 = Vec([4, 2, 1, 3])

assert math.isclose(
    v1.std(),
    v2.std()
)


# Positive scaling property
# std(c*v) = |c| * std(v)

v = Vec([1, 2, 3, 4])

scaled = 3 * v

assert math.isclose(
    scaled.std(),
    3 * v.std()
)


# Negative scaling property

v = Vec([1, 2, 3, 4])

scaled = -2 * v

assert math.isclose(
    scaled.std(),
    2 * v.std()
)


# std() should not modify original vector

v = Vec([1, 2, 3, 4])

original = v.elements.copy()

v.std()

assert v.elements == original


# Empty vector should raise error

try:
    Vec([]).std()
    assert False
except ValueError:
    pass


# =========================================================
# ERROR TESTS FOR ORIGINAL FUNCTIONS
# =========================================================

# Invalid vector element

try:
    Vec([1, "hello", 3])
    assert False
except TypeError:
    pass


# Addition of vectors with different dimensions

try:
    Vec([1, 2]) + Vec([1, 2, 3])
    assert False
except TypeError:
    pass


# zeros() with invalid size

try:
    Vec.zeros(0)
    assert False
except ValueError:
    pass


# ones() with invalid size

try:
    Vec.ones(-1)
    assert False
except ValueError:
    pass


# uniform() with invalid size

try:
    Vec.uniform(0)
    assert False
except ValueError:
    pass


print("All tests passed successfully!")