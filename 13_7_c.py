# вилучення з файла зайвих пропусків та всіх слів, що складаються з однієї букви


with open("/Users/katyasolovii/Desktop/programming/lab10/words.txt", "rt") as my_file:
    content = my_file.readlines()
    new_content = []
    new_words = []
    for line in content:
        line = line.lstrip() # видаляємо зайві пропуски
        words = line.split() # розділяємо слова і утворюємо список
        for el in words: 
            if len(el) > 1:
                new_words.append(el)
    words_with_space = '\n'.join(new_words) 
    new_content.append(words_with_space)

with open("/Users/katyasolovii/Desktop/programming/lab10/new_content_c.txt", "w") as my_file:
    my_file.writelines(new_content)
