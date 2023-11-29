# кількості парних чисел серед компонент
# змушна писати поснітю шлях до файла, бо так чогось не працює


with open("/Users/katyasolovii/Desktop/programming/lab10/numbers.txt", "rt") as my_file:
    content = my_file.read()
    even_num = []
    for el in content:
        if el.isdigit():
            num = int(el)
            if num % 2 == 0:
                even_num.append(num)
print(len(even_num))