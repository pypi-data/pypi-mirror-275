# fraction.py

from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self._reduce()
    
    def _reduce(self):
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor
    
    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Can only add Fraction with Fraction")
    
    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Can only subtract Fraction with Fraction")
    
    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Can only multiply Fraction with Fraction")
    
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            if new_denominator == 0:
                raise ZeroDivisionError("Division by zero")
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Can only divide Fraction with Fraction")
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"
