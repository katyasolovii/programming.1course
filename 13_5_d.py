# кількості компонент у найдовшій зростаючій послідовності компонент файла

with open("/Users/katyasolovii/Desktop/programming/lab10/numbers.txt", "rt") as my_file:
    content = my_file.read()
    numbers = []
    for num in content:
        if num.isdigit():
            numbers.append(num)
    long_sequence = []
    sequence = []
    for index in range(1, len(numbers)):
        if numbers[index] > numbers[index - 1]:
            sequence.append(numbers[index])
        else:
            if len(sequence) > len(long_sequence):
                long_sequence = sequence.copy()
            sequence = [numbers[index]] # зберігається індекс числа для наступного for
    if len(sequence) > len(long_sequence):
        long_sequence = sequence
print(len(long_sequence))