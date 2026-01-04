
"""
polymorphism_demo.py

Demonstrates polymorphism with a Shape base class and Rectangle/Circle subclasses.
Each subclass overrides the area() method.
"""
from __future__ import annotations
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape.

        Subclasses must implement this method.
        """
        raise NotImplementedError("Subclasses must override area()")


class Rectangle(Shape):
    """Rectangle defined by length and width."""

    def __init__(self, length: float, width: float) -> None:
        self.length = float(length)
        self.width = float(width)

    def area(self) -> float:
        """Area = length × width."""
        return self.length * self.width


class Circle(Shape):
    """Circle defined by its radius."""

    def __init__(self, radius: float) -> None:
        self.radius = float(radius)

    def area(self) -> float:
        """Area = π × r²."""
        return math.pi * (self.radius ** 2)


# Optional: simple self-test when run directly
if __name__ == "__main__":
    shapes: list[Shape] = [Rectangle(10, 5), Circle(7)]
    for s in shapes:
        print(f"The area of the {s.__class__.__name__} is: {s.area()}")