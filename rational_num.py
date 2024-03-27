from math import gcd

class Rational_numbers:
    
    __slots__ = ["_n", "_d"]

    def __init__(self, n, d) -> None:
        """
        Конструктор для створення нескоротного дробу за допомогою виклику приватного статичного методу _reduce().
        Дріб m/n, де n - numerator, d - denominator.
        За умовою завдання n > 0.
        """
        if d == 0:
            raise ValueError("Знаменник не може бути 0.")
        self._n, self._d = self._reduce(n, d)


    @staticmethod
    def _reduce(n, d):
        while gcd(n, d) != 1:
            common_divisor = gcd(n, d)
            n //= common_divisor
            d //= common_divisor
        return n, d
    

    @property
    def numerator(self):
        return self._n


    @property
    def denominator(self):
        return self._d
    

    @classmethod
    def from_string(cls, string):
        f = string.strip().split("/")
        if len(f) == 2:
            numerator = f[0]
            denominator = f[1]
        else:
            numerator = f[0]
            denominator = "1"
        numerator = int(numerator)
        denominator = int(denominator)
        return cls(numerator, denominator)


    def __add__(self, other):
        if isinstance(other, int):
            other = Rational_numbers(other)
        return Rational_numbers(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)


    def __radd__(self, other):
        return other.__add__(self)


    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational_numbers(other)
        return Rational_numbers(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)


    def __rsub__(self, other):
        return other.__sub__(self) 


    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational_numbers(other)
        return Rational_numbers(self.numerator * other.numerator, self.denominator * other.denominator)


    def __rmul__(self, other):
        return other.__mul__(self)


    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational_numbers(other)
        if other.numerator == 0:
            raise ValueError("Ділення на 0.")
        return Rational_numbers(self.numerator * other.denominator, self.denominator * other.numerator)
    

    def __rtruediv__(self, other):
        if self.numerator == 0:
            raise ValueError("Ділення на 0.")
        return other.__truediv__(self)
    

    def __abs__(self):
        return Rational_numbers(abs(self.numerator), abs(self.denominator))
    

    def sign(self):
        """
        Повертає знак дробу:
        якщо додатній дріб == 1,
        якщо від'ємний дріб == -1.
        """
        if self.numerator > 0 and self.denominator > 0:
            return 1
        if self.numerator < 0 or self.denominator < 0:
            return -1


    def integer(self):
        """
        Перевірка на те, чи є раціональне число цілим.
        """
        if self.denominator == 1:
            return True
        else:
            return False


    def __eq__(self, other):
        if isinstance(other, int):
            other = Rational_numbers(other)
        return self.numerator == other.numerator and self.denominator == other.denominator


    def inverse(self):
        """
        Рахує (1 / rational number).
        """
        if self.numerator == 0:
            raise ValueError("Знаменник оберненого дробу 0.")
        return Rational_numbers(self.denominator, self.numerator)


    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return str(self.numerator / self.denominator)


    def __repr__(self):
        return f"Rational_numbers(numerator = {self.numerator}, denominator = {self.denominator})"