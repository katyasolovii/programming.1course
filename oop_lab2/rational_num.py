from math import gcd

class RationalNumber:
    
    __slots__ = ["_n", "_d"]

    def __init__(self, n, d) -> None:
        """
        Конструктор для створення нескоротного дробу за допомогою виклику приватного статичного методу _reduce().
        Дріб m/n, де n - numerator, d - denominator.
        За умовою завдання n > 0. НЕ ЗА УМОВОЮ
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
        if d < 0:
            n = -n
            d = -d
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
            other = RationalNumber(other, 1)
        return RationalNumber(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            other = RationalNumber(other)
        return RationalNumber(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)

    def __rsub__(self, other):
        return other.__sub__(self) 

    def __mul__(self, other):
        if isinstance(other, int):
            other = RationalNumber(other)
        return RationalNumber(self.numerator * other.numerator, self.denominator * other.denominator)

    def __rmul__(self, other):
        return other.__mul__(self)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = RationalNumber(other, 1)
        if other.numerator == 0:
            raise ValueError("Ділення на 0.")
        return RationalNumber(self.numerator * other.denominator, self.denominator * other.numerator)
    
    def __rtruediv__(self, other):
        if self.numerator == 0:
            raise ValueError("Ділення на 0.")
        return self.__truediv__(other)

    def __abs__(self):
        return RationalNumber(abs(self.numerator), abs(self.denominator))

    def sign(self):
        """
        Повертає знак дробу:
        якщо чисельник додатній == 1,
        якщо чисельник від'ємний == -1,
        якщо чисельник 0 == 0.
        """
        if self.numerator > 0:
            return 1
        elif self.numerator < 0:
            return -1
        else:
            return 0 

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
            other = RationalNumber(other)
        return self.numerator == other.numerator and self.denominator == other.denominator

    def inverse(self):
        """
        Рахує (1 / rational number).
        """
        if self.numerator == 0:
            raise ValueError("Знаменник оберненого дробу 0.")
        return RationalNumber(self.denominator, self.numerator)

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __float__(self):
        return self.numerator / self.denominator

    def __repr__(self):
        return f"Rational_numbers(numerator = {self.numerator}, denominator = {self.denominator})"
    
    def __lt__(self, other):
        return (self.numerator * other.denominator) < (other.numerator * self.denominator)
    
    def __le__(self, other):
        return (self.numerator * other.denominator) <= (other.numerator * self.denominator)

    def __gt__(self, other):
        return (self.numerator * other.denominator) > (other.numerator * self.denominator)

    def __ge__(self, other):
        return (self.numerator * other.denominator) >= (other.numerator * self.denominator)