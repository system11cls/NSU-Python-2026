from argparse import ArgumentError


class Vector:
    size: int
    elements: list

    def __init__(self, elements):
        if len(elements) == 0:
            raise ArgumentError("dimension must positive")
        self.size = len(elements)
        self.elements = elements

    @staticmethod
    def null_vector(dim: int):
        if dim < 1:
            raise ArgumentError("dimension must positive")
        return Vector([0 for _ in range(1, dim + 1)])

    @staticmethod
    def iden_vector(dim: int):
        if dim < 1:
            raise ArgumentError("dimension must positive")
        return Vector([1 for _ in range(1, dim + 1)])

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector([x + y for (x, y) in zip(self.elements, other.elements)])

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector([x - y for (x, y) in zip(self.elements, other.elements)])

    def __mul__(self, other):
        if isinstance(other, Vector):
            return sum([x*y for (x, y) in zip(self.elements, other.elements)])
        elif isinstance(other, float):
            return Vector([other * x for x in self.elements])

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.size == other.elements and self.elements == other.elements