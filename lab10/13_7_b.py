# звизначення кількості слів у файлі


with open("/Users/katyasolovii/Desktop/programming/lab10/words.txt", "rt") as my_file:
    content = my_file.read()
    words = content.split()
print(len(words))