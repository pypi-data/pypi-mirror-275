from __future__ import annotations


class Fraction:
    """
    Represents a fraction in the form i + n / d.

    Attributes:
    - i (int): The integer part of the fraction.
    - n (int): The numerator of the fraction.
    - d (int): The denominator of the fraction.
    """

    i: int
    n: int
    d: int

    def __init__(self, i: int, n: int, d: int):
        self.i = i
        self.n = n
        self.d = d

    def __repr__(self) -> str:
        return f"{self.i} + {self.n} / {self.d}"

    def __str__(self) -> str:
        return f"{self.i} + {self.n} / {self.d}"

    def reduce(self) -> Fraction:
        """
        Reduces the fraction to its simplest form. Makes the numerator and the denominator positive.

        Returns:
        - Fraction: The reduced fraction.
        """

        assert self.d != 0, "Denominator cannot be zero."

        if self.n == 0:
            return Fraction(self.i, 0, 1)

        if self.d < 0:
            self.n = -self.n
            self.d = -self.d

        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
        g = gcd(self.n, self.d)
        res = Fraction(self.i, self.n // g, self.d // g)
        if res.n >= res.d:
            res.i += res.n // res.d
            res.n %= res.d
        return res

    def __eq__(self, other: Fraction) -> bool:
        """
        Checks if two fractions are equal.

        Args:
        - other (Fraction): The fraction to compare with.

        Returns:
        - bool: True if the fractions are equal, False otherwise.
        """
        this = self.reduce()
        other = other.reduce()
        return (this.i * this.d + this.n) * other.d == (other.i * other.d + other.n) * this.d

    def __add__(self, other: Fraction) -> Fraction:
        """
        Adds two fractions.

        Args:
        - other (Fraction): The fraction to add.

        Returns:
        - Fraction: The sum of the two fractions.
        """
        return Fraction(self.i + other.i, self.n * other.d + other.n * self.d, self.d * other.d).reduce()

    def __sub__(self, other: Fraction) -> Fraction:
        """
        Subtracts two fractions.

        Args:
        - other (Fraction): The fraction to subtract.

        Returns:
        - Fraction: The difference between the two fractions.
        """
        return Fraction(self.i - other.i, self.n * other.d - other.n * self.d, self.d * other.d).reduce()

    def __neg__(self) -> Fraction:
        """
        Negates the fraction.

        Returns:
        - Fraction: The negated fraction.
        """
        return Fraction(-self.i, -self.n, self.d).reduce()

    def __gt__(self, other: Fraction) -> bool:
        """
        Checks if one fraction is greater than another.

        Args:
        - other (Fraction): The fraction to compare with.

        Returns:
        - bool: True if the first fraction is greater than the second, False otherwise.
        """
        return (self - other).is_positive

    def __ge__(self, other: Fraction) -> bool:
        """
        Checks if one fraction is greater than or equal to another.

        Args:
        - other (Fraction): The fraction to compare with.

        Returns:
        - bool: True if the first fraction is greater than or equal to the second, False otherwise.
        """
        return (self - other).is_positive or self == other

    def __lt__(self, other: Fraction) -> bool:
        """
        Checks if one fraction is less than another.

        Args:
        - other (Fraction): The fraction to compare with.

        Returns:
        - bool: True if the first fraction is less than the second, False otherwise.
        """
        return not self >= other

    def __le__(self, other: Fraction) -> bool:
        """
        Checks if one fraction is less than or equal to another.

        Args:
        - other (Fraction): The fraction to compare with.

        Returns:
        - bool: True if the first fraction is less than or equal to the second, False otherwise.
        """
        return not self > other

    @property
    def is_positive(self) -> bool:
        """
        Checks if the fraction is positive.

        Returns:
        - bool: True if the fraction is positive, False otherwise.
        """
        this = self.reduce()
        return this.i > 0 or (this.i ==0 and this.n > 0)

    def to_float(self) -> float:
        """
        Converts the fraction to a floating point number.

        Returns:
        - float: The floating point number.
        """
        return (self.i + self.n / self.d)
