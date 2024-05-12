from math import sqrt, pow, pi


class Triangle:
    def __init__(self, a, b, c) -> None:
        if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Трикутника не існує.")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


class Rectangle:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b 
    
    def perimeter(self):
        return self.a * 2 + self.b * 2
    
    def area(self):
        return self.a * self.b 


class Trapeze:
    """
    Parameters
    ----------
    base_a : int 
        основа трапеції a
    base_b : int
        основа трапеції b
    lateral_c : int
        бічна сторона c
    lateral_d : int 
        бічна сторона c
    """
    def __init__(self, a, b, c, d) -> None:
        if a == b or c <= 0 or d <= 0 or abs(a - b) >= c + d:
            raise ValueError("Трапеції не існує.")
        self.base_a = a
        self.base_b = b
        self.lateral_c = c
        self.lateral_d = d

    def perimeter(self):
        return self.base_a + self.base_b + self.lateral_c + self.lateral_d

    def find_height(self):
        height = pow(self.lateral_d, 2) - pow((self.base_b - self.base_a + self.lateral_c - self.lateral_d) / 2, 2)
        if height < 0:
            raise ValueError("Трапеція не існує.")
        return sqrt(height)
        
    def area(self):
        return ((self.base_a + self.base_b) / 2) * self.find_height()


class Parallelogram:
    def __init__(self, a, b, h) -> None:
        self.a = a
        self.b = b
        self.ha = h 

    def perimeter(self):
        return self.a * 2 + self.b * 2
    
    def area(self):
        return self.a * self.ha


class Circle:
    def __init__(self, r) -> None:
        self.r = r

    def circumference(self):
        return 2 * pi * self.r


files = ["/Users/katyasolovii/Documents/programming/oop/lab1_1/input02.txt"]
max_area = None
max_perimeter = None
constructors = {
    'Triangle': Triangle, 
    'Rectangle': Rectangle, 
    'Trapeze': Trapeze, 
    'Parallelogram' : Parallelogram,
    'Circle' : Circle
}
for file in files:
    geom_shapes = []
    with open(file, 'r') as file:
        for line in file:
            try:
                data = line.split()
                shape_type = data[0]
                params = list(map(int, data[1:]))
                if shape_type not in constructors:
                    raise ValueError("Невідома геометрична фігура.")
                shape = constructors[shape_type](*params)
                if shape_type != "Circle":
                    geom_shapes.append((shape, shape.area(), shape.perimeter()))
                else:
                    geom_shapes.append((shape, None, shape.circumference()))
            except ValueError as e:
                print(f"Error: {e}")
    for shape, area, perimeter in geom_shapes:
        if area is not None:
            if max_area is None or area > max_area[1]:
                max_area = (shape, area)
        if perimeter is not None:
            if max_perimeter is None or perimeter > max_perimeter[1]:
                max_perimeter = (shape, perimeter)
if max_area is not None:
    print("Геометрична фігура з найбільшою площею:", max_area[0])
if max_perimeter is not None:
    print("Геометрична фігура з найбільшим периметром:", max_perimeter[0])
