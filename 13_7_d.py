# вилучення всіх пропусків на початку рядків, у кінці рядків та
# між словами (окрім одного)


with open("/Users/katyasolovii/Desktop/programming/lab10/words.txt", "rt") as my_file:
    content = my_file.readlines() # по рядку
    content_new = []
    for line in content:
        line = line.lstrip() # на початку видаляє пробіли
        line = line.rstrip() # в кінці видаляє пробіли
        words = line.split() # розділяє на слова в рядку і повертає як список
        line = ' '.join(words) # вилучає зайві пропуски між словами
        content_new.append(line)
        
with open("/Users/katyasolovii/Desktop/programming/lab10/new_content_d.txt", "w") as res_file:
    res_file.writelines(content_new)