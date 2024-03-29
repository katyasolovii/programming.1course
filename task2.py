from rational_num import Rational_numbers
from math import sqrt

with open("/Users/katyasolovii/Documents/programming/oop/lab2/input2.txt", "r") as file:
    with open("/Users/katyasolovii/Documents/programming/oop/lab2/result3.txt", "w") as rec_file:
        for line in file:
            ls = []
            for num in line.split(","):  
                coef = Rational_numbers.from_string(num.strip())  
                ls.append(coef)
            deg = len(ls) - 1
            point_value_1 = Rational_numbers(0, 1) 
            point = Rational_numbers(1, 1)
            for i in ls:
                x = Rational_numbers.__mul__(i, point)
                point_value_1 = Rational_numbers.__add__(x, point_value_1)
            rec_file.write(f"Значення многочлена в точці x = 1: {point_value_1}\n")
            if deg <= 2:
                if deg == 1:
                    a = ls[0].numerator / ls[0].denominator
                    b = ls[1].numerator / ls[1].denominator
                    if a == 0 or b / a:
                        rec_file.write(f"Корені многочлена степеня 1 є не дійсними числами. \n")
                    else:
                        x1 = - b / a
                        rec_file.write(f"Корені многочлена степеня 1: {x1}\n")
                if deg == 2:
                    a = ls[0].numerator / ls[0].denominator
                    b = ls[1].numerator / ls[1].denominator
                    c = ls[2].numerator / ls[2].denominator
                    discriminant = pow(b, 2) - 4 * a * c
                    if discriminant > 0:
                        if 2 * a == 0:
                            rec_file.write(f"Корені многочлена степеня 2 є не дійсними числами. \n")
                        else:
                            x1 = (-b + sqrt(discriminant)) / (2 * a)
                            x2 = (-b - sqrt(discriminant)) / (2 * a)
                            rec_file.write(f"Корені многочлена степеня 2: {x1}, {x2} \n")
                    elif discriminant == 0:
                        x1 = - b / a
                        rec_file.write(f"Корені многочлена степеня 2: {x1} \n")
                    else:
                        rec_file.write(f"Корені многочлена степеня 2 є не дійсними числами. \n")
            elif deg > 2:
                res = True
                for num in ls:
                    if not isinstance(Rational_numbers.__str__(num), int):
                        rec_file.write(f"Коефіцієнти многочлена степеня {deg} не цілі. \n")
                        break
                    else:
                        f_n = Rational_numbers.__str__(abs(ls[-1]) + Rational_numbers(1, 1))
                        s_n = Rational_numbers.__str__(abs(ls[0]) + Rational_numbers(1, 1))
                        div_free = range(1, int(float(f_n)))
                        div_sen = range(1, int(float(s_n)))
                        x = []
                        for p in div_free:
                            for q in div_sen:
                                possible_x = float(Rational_numbers.__str__(Rational_numbers(p,q)))
                                value = 0
                                for i, j in zip(range(deg, -1, -1), range(deg + 1)):
                                    z = float(Rational_numbers.__str__(ls[j]))
                                    value += z * pow(possible_x, i)
                                if value == 0:
                                    x.append(possible_x)
                        if x:   
                            rec_file.write(f"Корені многочлена степеня {deg}: {x}\n")
                        else:
                            rec_file.write(f"Коренів многочлена степеня {deg} немає.\n")
    print("The happy end!")
