from math import sqrt, pow


class Vector:
    def __init__(self, components):
        if not isinstance(components, list):
            raise ValueError("Координати мають бути списком.")
        for i in components:
            if not isinstance(i, int or float):
                raise ValueError("Неправильний тип даних.")
        self.components = components
    
    def dim_vec(self):
        return len(self.components)
    
    def length(self):
        return sqrt(sum(pow(i, 2)for i in self.components))
    
    def average(self):
        return sum(self.components) / len(self.components)

    def show(self):
        return f"Vector: {self.components}"
    
    def max_value(self):
        # для випадку, якщо пустий рядок
        if len(self.components) == 0: 
            return 0
        return max(self.components) 

    def min_value(self):
        if len(self.components) == 0:
            return 0
        return min(self.components) 


files = ["/Users/katyasolovii/Documents/programming/oop/lab1_2/input01.txt"]
max_dim = 0
max_len = 0
num_vec = 0
vec_max_len = []
vec_max_dim = []
average_len = []
max_component = None 
min_component = None
for file in files:
    with open(file, 'r') as file:
        for line in file:
            data = line.split()
            p = list(map(int, data[0:]))
            vector = Vector(p)
            dim = vector.dim_vec()
            length = vector.length()
            num_vec += 1
            component = len(p)
            
            if dim > max_dim:
                max_dim = dim
                vec_max_dim = [vector]
            if dim == max_dim and length < vec_max_dim[0].length():
                vec_max_dim = [vector]

            if length > max_len:
                max_len = length
                vec_max_len = [vector]
            if length == max_len and dim < vec_max_len[0].dim_vec():
                vec_max_len = [vector]

            average_len.append(length)
           
            if max_component is None or component > max_component.dim_vec():
                max_component = vector
            if component == max_component.dim_vec() and vector.max_value() < max_component.dim_vec():
                max_component = vector
            if min_component is None or component < min_component.dim_vec():
                min_component = vector
            if component == min_component.dim_vec() and vector.min_value() > min_component.dim_vec():
                min_component = vector
    

print("Найбільша розмірність:", max_dim)
print("Вектор з найбільшою розмірністю:", vec_max_dim[0].show())
print("Найбільша довжина:", max_len)
print("Вектор з найбільшою довжиною:", vec_max_len[0].show())
print("Середня довжина вектора:", sum(average_len) / num_vec)
count_vec_len = 0
for length in average_len:
    if length > sum(average_len) / num_vec:
        count_vec_len += 1
print("Кількість векторів з довжиною більшою за середню довжину загального набору:", count_vec_len)
print("Вектор з максимальною найбільшою компонентою:", max_component.show())
print("Вектор з максимальною найменшою компонентою:", min_component.show())
