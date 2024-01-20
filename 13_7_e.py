#  вставки пропусків у рядки рівномірно між словами так, щоб довжина всіх рядків (якщо в них більше 1 слова) була 80 символів 
# та кількість пропусків між словами в одному рядку відрізнялась не більше, ніж на 1 (вважати, що рядки файла мають не більше, 
# ніж 80 символів). Результат записати у файл H.


with open("/Users/katyasolovii/Desktop/programming/lab10/words.txt", "rt") as my_file:
    content = my_file.readlines() 
    res = []
    needed_len = 80
    for line in content:
        line_strip = line.strip() # видаляє пробіли на початку та в кінці
        words = line_strip.split()
        new_line = len(" ".join(words))
        needed_skip = needed_len - new_line
        words_amount = len(line)
        min_amount = needed_skip // (words_amount + 1) # мінімальна кількість пробілів, які треба вставити на кожне місце
        leftovers = needed_skip % (words_amount + 1) # зайві пробіли, які треба розподілити 
        res_line = words[0] # щоб не було пробіла перед першим словом
        if leftovers:
            res_line += " "
            leftovers -= 1
        for word in words[1:]:
            res_line += " " * min_amount
            if leftovers:
                res_line += " "
                leftovers -= 1
            res_line += word
        res.append(res_line)
with open("/Users/katyasolovii/Desktop/programming/lab10/H.txt", "w") as res_file:
    res_file.writelines("\n".join(res))