# Описати підпрограму, яка за заданою послідовністю символів формує 
# текстовий файл із рядками по 40 літер (в останньому рядку літер може 
# бути й менше).


def write_let(alphabet):
    with open("/Users/katyasolovii/Desktop/programming/lab10/file_40_letter.txt", "w") as my_file:
        for i in range(0, len(alphabet), 40):
            line = alphabet[i:i+40]
            my_file.write(f"{line}\n")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
write_let(alphabet)