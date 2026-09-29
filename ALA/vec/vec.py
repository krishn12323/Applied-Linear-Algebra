
import sys
from typing import Self
import random
import math


"""
A custom vector class implementation for educational purposes.
"""

class Vec:
    def __init__(self, src=None) -> Self:
        if src is None:
            self.elements = []
        else:
            elements = list(src)
            for x in elements:
                if not isinstance(x, (int, float)):
                    raise TypeError(f"Scalar must be a number: {type(x)}")
            self.elements = elements

    def __add__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")
        if len(self.elements) != len(t):
            raise TypeError(f"Type error - vectors must be of same dimensions")

        return Vec([round(x + y, 5) for x, y in zip(self.elements, t.elements)])


    def __rmul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")
        #
        return Vec([round(x * scalar, 5) for x in self.elements])

    def __imul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")

        for i, val in enumerate(self.elements):
            self.elements[i] = round(val * scalar, 5)
        #
        return self

    def __repr__(self) -> str:
        return repr(self.elements)

    def __len__(self) -> int:
        return len(self.elements)

    def __sub__(self, t: Self) -> Self:
        if not isinstance(t,Vec):
            raise TypeError(f"Wrong type: {type(t)} ")
        if len(self.elements)!= len(t.elements):
            raise TypeError(f"Vectors shud be of same length")

        return Vec([round(x-y, 5) for x,y in zip(self.elements,t.elements)])

    def __neg__(self) -> Self:
        return Vec([-x for x in self.elements])

    def __radd__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError(f"Expected a number: {type(other)}")
        return Vec([round(other + x, 5) for x in self.elements])

    def __iadd__(self, other):
        if not isinstance(other, Vec):
            raise TypeError(f"Expected Vec: {type(other)}")

        if len(self.elements) != len(other.elements):
            raise TypeError("Vectors should be of same length")

        for i in range(len(self.elements)):
            self.elements[i] = round(
            self.elements[i] + other.elements[i], 5
        )
        return self

    # return a vector of @n zeroes. precondition: @n > 0
    @staticmethod
    def zeros(n: int) -> Self:
        if n <= 0:
            raise ValueError("n must be greater than 0")
        return Vec([0] * n)

    # return a vector of @n. precondition: @n > 0
    @staticmethod
    def ones(n: int) -> Self:
        if n<=0:
            raise ValueError("N must be greater then 0")
        return Vec([1]*n)

    # return a vector of @n uniformly distributed numbers in [0, 1]. precondition: @n > 0
    @staticmethod
    def uniform(n: int) -> Self:
        if n <= 0:
            raise ValueError("n must be greater than 0")

        return Vec([random.uniform(0, 1) for _ in range(n)])
    

        # return the norm (magnitude) of the vector
    def norm(self) -> float:
        return math.sqrt(sum(x * x for x in self.elements))


    # return the mean of the vector elements
    def mean(self) -> float:
        if len(self.elements) == 0:
            raise ValueError("Vector cannot be empty")

        return sum(self.elements) / len(self.elements)


    # return a new de-meaned vector
    def demean(self) -> Self:
        if len(self.elements) == 0:
            raise ValueError("Vector cannot be empty")

        m = self.mean()

        return Vec([round(x - m, 5) for x in self.elements])


    # return the standard deviation of the vector elements
    def std(self) -> float:
        if len(self.elements) == 0:
            raise ValueError("Vector cannot be empty")

        d = self.demean()

        squared_sum = sum(x * x for x in d.elements)

        return math.sqrt(squared_sum / len(self.elements))


