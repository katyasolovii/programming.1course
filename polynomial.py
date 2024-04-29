from rational_num import RationalNumber

class Polynomial(dict):
    """
    Клас Polynomial представляє многочлен як словник <степінь: коефіцієнт>
    """

    def __init__(self, arg, coeff_type=float):
        self.coeff_type = coeff_type
        if isinstance(arg, str):
            self._parse_string(arg)
        elif isinstance(arg, dict):
            for deg, coeff in arg.items():
                self[deg] = coeff
        elif isinstance(arg, list):
            i = 0
            for coeff in arg:
                self[i] = coeff
                i += 1
        elif isinstance(arg, (int, float, RationalNumber)):
            self[0] = coeff_type(arg)
        else:
            raise ValueError("Неправильний формат многочлена")
        self._reduce()
    
    def type_rational(self, number):
        if "x^" in number:
            coeff, deg = number.split("x^")
            coeff = RationalNumber.from_string(coeff)
            if not deg:
                coeff = 0
                deg = 0
        elif "x" in number:
            coeff, deg = number.split("x")
            coeff = RationalNumber.from_string(coeff)
            deg = 1
        else:
            coeff = RationalNumber.from_string(number)
            deg = 0
        return coeff, deg

    def _parse_monomial(self, string):
        if "/" in string:
            coeff, deg = self.type_rational(string)
        elif "x^" in string:
            coeff, deg = string.split("x^")
            if not coeff:
                coeff = 1
            else:
                coeff = float(coeff) 
            if not deg:
                coeff = 0
                deg = 0
        elif "x" in string:
            coeff, deg = string.split("x")
            deg = 1
            if not coeff:
                coeff = 1
            else:
                coeff = float(coeff)
        else:
            coeff = float(string)
            deg = 0
        return coeff, deg
            
    def _parse_string(self, string):
        line = string.split("+")
        for el in line:
            el = el.strip()
            if not el:
                raise ValueError("Пустий рядок")
            coeff, deg = self._parse_monomial(el)
            try:
                self[int(deg)] = coeff
            except ValueError:
                raise ValueError("Неправильний формат многочлена")
            
    def copy(self):
        return Polynomial(self, self.coeff_type)

    def as_type(self, coeff_type):
        new_coeffs = {}
        for deg, coeff in self.items():
            # coeff_type  - новий тип даних, на який треба замінити (наприклад int(coeff))
            new_coeffs[deg] = coeff_type(coeff)
        return Polynomial(new_coeffs, coeff_type)

    def __str__(self):
        polynomial = []
        for deg, coeff in sorted(self.items()):
            if deg == 0:
                polynomial.append(str(coeff))
            elif deg == 1:
                polynomial.append(f"{coeff}x")
            else:
                polynomial.append(f"{coeff}x^{deg}")
        return " + ".join(polynomial)

    def __repr__(self):
        return f"Polynomial({dict(self)})"

    def __add__(self, other):
        res = {}
        if isinstance(other, Polynomial):
            for deg, coeff in self.items():
                if deg in other:
                    res[deg] = coeff + other[deg]
                else:
                    res[deg] = coeff
            for deg, coeff in other.items():
                if deg not in res:
                    res[deg] = coeff
            return Polynomial(res)
        elif isinstance(other, (int, float)):
            for deg, coeff in self.items():
                res.setdefault(deg , 0)
                res[deg] += coeff + other
            return Polynomial(res)
        try:
            other_poly = Polynomial(other)
            return self + other_poly
        except:
            raise ValueError("Заданий тип не можна перевести у поліном")
    
    def inverse(self):
        """
        Метод повертає негативний поліном, змінюючи знак всіх коефіцієнтів на протилежний.
        Це знадобиться для метода __sub__, щоб скороти та облегшити код.
        """
        inv_poly = {}
        for deg, coeff in self.items():
            inv_poly[deg] = -coeff
        return Polynomial(inv_poly)

    def __sub__(self, other):
        """
        Віднімання многочленів == додавання оберненого полінома.
        """
        if isinstance(other, Polynomial):
            return self + other.inverse()
        else:
            raise ValueError("Заданий тип не можна перевести у поліном")
        
    def __mul__(self, other):
        if isinstance(other, Polynomial):
            res = {}
            for degi, coeffi in self.items():
                for degj, coeffj in other.items():
                    res.setdefault(degi + degj, 0)
                    res[degi + degj] += coeffi * coeffj
                    # new_deg = degi +degj
                    # if new_deg in res:
                    #     res[new_deg] += coeffi * coeffj
                    # else:
                    #     res[new_deg] = coeffi * coeffj
            return Polynomial(res)
        else: 
            raise ValueError("Заданий тип не можна перевести у поліном")

    def __call__(self, value):
        """
        Метод рахує значення многочлена у заданій точці.
        """
        res = 0
        for deg, coeff in self.items():
            res += coeff * (value ** deg)
        return res

    def __truediv__(self, value):
        """
        Ділення сногочлена на число.
        """
        if isinstance(value, Polynomial):
            raise NotImplementedError("Ділення многочлена на многочлен не підтримується у цьому класі.")
        res = {}
        for deg, coeff in self.items():
            res[deg] = coeff / value
        return Polynomial(res)

    def derivative(self):
        """
        Похідна многочлена
        """
        res = {}
        for deg, coeff in self.items():
            if deg == 0:
                # випадок, якщо поліном складається тільки з числа
                if len(self.items()) == 1:
                    return 0
                continue
            res[deg - 1] = coeff * deg
        return Polynomial(res)

    def primitive(self):
        """
        Первісна многочлена (ігнорувати +С)
        """
        res = {}
        for deg, coeff in self.items():
            if deg == 0:
                res[1] = coeff
            res[deg + 1] = coeff / (deg + 1)
        return Polynomial(res)

    def _reduce(self):
        """
        Метод "чистить" многочлен, видаляючи степені з нульовими коефіцієнтами
        """
        keys_to_delete = []
        for deg, coeff in self.items():
            if coeff == 0:
                keys_to_delete.append(deg)
        for deg in keys_to_delete:
            del self[deg]

    def div(self, other):
        """
        Ділення многочленів. Повертає частку і остачу.
        quotient - частка
        remainder(отримуємо від self, змінюючи кожен раз, поки max степінь self не буде меншою за max other) - остача 
        """
        if not isinstance(other, Polynomial):
            other = Polynomial(other)
        if not isinstance(other, Polynomial):
            raise ValueError("Дільник має бути об'єктом класу Polynomial")
        # порожній поліном для частки
        quotient = Polynomial({})
        remainder = self.copy()
        while max(remainder.keys()) >= max(other.keys()):
            r_deg = max(remainder.keys())
            o_deg = max(other.keys())
            d = r_deg - o_deg
            # коефіцієнт у quotient - частка між коефіцієнтами max deg (keys) у remainder і other
            coeff = remainder[r_deg] / other[o_deg]
            quotient[d] = coeff
            # треба змінити self(remainder, остача)
            # sub з остачі множення other на коефіцієнт
            for deg in other:
                remainder[deg + d] -= coeff * other[deg]
            remainder._reduce()
        return quotient, remainder

    def euclidean(self, other):
        a = self.copy()
        b = other.copy()
        while max(b.keys()) != 0:
            noneed, remainder = a.div(b)
            a = b
            b = remainder
        return a


if __name__ == "__main__":
    p = Polynomial("x^2 + 3x + 4")
    p1 = Polynomial("x + 1")
    print(Polynomial.__repr__(p))
    q, r = Polynomial.div(p, p1)
    print("Частка:", q)
    print("Остача:", r)
    w = Polynomial.euclidean(p, p1)
    print(Polynomial.__str__(w))
    print("-----------------------")
    print("Виведення многочленів вигляду str\n")
    d = Polynomial("x^2 + 4x + 4")
    print(d)
    p0 = Polynomial({0: 2+3j, 1: 1-2j, 2: 4})
    p = Polynomial({0: 5+1j, 1: 9-5j, 2: 0})
    p1 = Polynomial("7 + 4x + 2x^2 + 1x^3")
    p2 = Polynomial({0: 2, 1: 1, 3: 0, 4:0})
    p3 = Polynomial([1, 1, 0, 4, 7])
    p4 = Polynomial(5.0)
    p6 = Polynomial("5x^3 + 2x^2 + 6x + 9")
    print(p1 + p6)
    point1 = 2.0
    point2 = 1.4
    point3 = 0.5
    # застосування _reduce
    print(p2)
    print(p3)
    print("-----------------------\n")
    # комлексні числа
    print(p0)
    print(p)
    print(p0 + p)
    print(p / point1)
    print(p0 - p)
    print(p * p0)
    print("-----------------------")
    print("Первірка на правильність формату многочлена\n")
    d1 = ""
    d2 = "sdfijdf"
    try:
        polynomial1 = Polynomial(d1)
    except ValueError as e:
        print(f"{e}: {d1}")

    try:
        polynomial2 = Polynomial(d2)
    except ValueError as e:
        print(f"{e}: {d2}")
    # перевірка на додавання, віднімання, множення та ділення на число
    print("-----------------------")
    print("Додавання, віднімання, множення та ділення на число\n")
    print(p1 + point1)
    print(p1 + p3)
    print(p4 - p1)
    print(p1 * p6)
    print(p1 / point3)
    print("-----------------------")
    print("Копія многочлена, де коефіцієнти мають новий заданий тип\n")
    # перевірка роботи з різними типами, переведення з одного типа на інший
    poly_int = Polynomial({0: 2, 1: 3, 2: 9}, coeff_type=dict)
    print("Многочлен з int коефіцієнтами:", repr(poly_int))
    poly_float = poly_int.as_type(float)
    print("Многочлен з float коефіцієнтами:", poly_float)
    print("-----------------------")
    print("Значення у точці та взяття похідної, первісної\n")
    # перевірка на значення у точці та взяття похідної, первісної
    print(p1(point2))
    print(Polynomial.derivative(p6))
    print(Polynomial.primitive(p1))
    print(Polynomial.primitive(p))
    print(Polynomial.derivative(p))
    print("-----------------------")
