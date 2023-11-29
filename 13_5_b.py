# кількості квадратів непарних чисел серед компонент


with open("/Users/katyasolovii/Desktop/programming/lab10/numbers.txt", "rt") as my_file:
    content = my_file.read()
    square_odd = []
    for el in content:
        if el.isdigit():
            num = int(el)
            square = num ** 2
            if num % 2 != 0:
                square_odd.append(square)
print(len(square_odd))