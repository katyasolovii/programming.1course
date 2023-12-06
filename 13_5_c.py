# різниці між найбільшим парним і найменшим непарним числами з компонент


with open("/Users/katyasolovii/Desktop/programming/lab10/numbers.txt", "rt") as my_file:
    content = my_file.read()
    even_num = []
    odd_num = []
    for el in content:
        if el.isdigit():
            num = int(el)
            if num % 2 == 0:
                even_num.append(num)
            if num % 2 != 0:
                odd_num.append(num)
print(max(even_num) - min(odd_num))