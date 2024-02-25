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
    def __init__(self, a, b, c, d) -> None:
        """
        Нехай,
        base_a, base_b - основи
        lateral_c,lateral_d - бічні сторони   
        """
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
    

files = ["/Users/katyasolovii/Documents/programming/oop/input01.txt"]
max_area = None
max_perimeter = None
for file in files:
    geom_shapes = []
    with open(file, 'r') as file:
        for line in file:
            data = line.split()
            shapes_type = data[0]
            p = list(map(int, data[1:]))
            # розпакуємо парметри для кожної геометричної фігури
            try:
                if shapes_type == "Triangle":
                    shapes = Triangle(*p)
                elif shapes_type == "Rectangle":
                    shapes = Rectangle(*p)
                elif shapes_type == "Trapeze":
                    shapes = Trapeze(*p)
                elif shapes_type == "Parallelogram":
                    shapes = Parallelogram(*p)
                elif shapes_type == "Circle":
                    shapes = Circle(*p)
                else:
                    raise ValueError("Невідома геометрична фігура.") 
                if shapes_type != "Circle":
                    geom_shapes.append((shapes, shapes.area(), shapes.perimeter()))
                else:
                    geom_shapes.append((shapes, None, shapes.circumference()))
            except ValueError as e:
                print(f"Error: {e}")
        for shapes, area, perimeter in geom_shapes:
            # порівнюємо кожну площу/периметр з попередніми, якщо поточне не є нульовими;
            # за умовою 80-81 кортеж max пустий, то перше поточне значення буде першим
            if area is not None:
                if max_area is None or area > max_area[1]:
                    max_area = (shapes, area)
            if perimeter is not None:
                if max_perimeter is None or perimeter > max_perimeter[1]:
                    max_perimeter = (shapes, perimeter)

print("Геометрична фігура з найбільшою площею:", max_area[0]) # як вивести тільки назву?
print("Геометрична фігура з найбільшим периметром:", max_perimeter[0])