from rational_num import RationalNumber

with open("/Users/katyasolovii/Documents/programming/oop/lab2/input1.txt", "r") as file:
    numbers = []
    for line in file:
        l = line.strip()
        numbers.append(RationalNumber.from_string(l))
max_num = None
max_abs_num = None
summ_num = 0
for num in numbers:
    # для порівняння дробів, зведемо їх до спільного дільника і порівняємо їхні чисельники
    if max_num is None or (num.denominator > 0 and num.numerator > 0 and num > max_num):
        max_num = num
    abs_num = abs(num)
    if max_abs_num is None:
        max_abs_num = num
    else:
        abs_ls_max = abs(max_abs_num)
        if abs_num > abs_ls_max:
            max_abs_num = num
    summ_num += num

print("Максимальне число:", max_num)
print("Максимальне число за модулем:", max_abs_num)
arithmetic = float(summ_num / len(numbers))
print("Середнє арифметичне значення:", arithmetic)
