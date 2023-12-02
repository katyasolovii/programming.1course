# знаходження найдовшого слова у файлі


with open("/Users/katyasolovii/Desktop/programming/lab10/words.txt", "rt") as my_file:
    content = my_file.read()
    words = content.split()
print(max(words, key = len)) # максимальне слово за довжиною 