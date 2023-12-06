# кількості квадратів непарних чисел серед компонент


with open("/Users/katyasolovii/Desktop/programming/lab10/numbers.txt", "rt") as my_file:
    content = my_file.read()
    square_odd = []
    for el in content:
        if el.isdigit():
            num = int(el)
            for k in range(0, 2):
                if num == pow((2 * k + 1), 2):
                    square_odd.append(num)
print(len(square_odd))
