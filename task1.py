from rational_num import Rational_numbers

with open("/Users/katyasolovii/Documents/programming/oop/lab2/input1.txt", "r") as file:
    numbers = []
    for line in file:
        l = line.strip()
        numbers.append(Rational_numbers.from_string(l))
max_num = None
max_abs_num = None
summ_num = 0
for num in numbers:
    # для порівняння дробів, зведемо їх до спільного дільника і порівняємо їхні чисельники
    if max_num is None or (num.denominator > 0 and num.numerator > 0 and num.numerator * max_num.denominator > max_num.numerator * num.denominator):
        max_num = num
    abs_num = Rational_numbers.__abs__(num)
    if max_abs_num is None:
        max_abs_num = num
    else:
        abs_ls_max = Rational_numbers.__abs__(max_abs_num)
        if abs_num.numerator * abs_ls_max.denominator > abs_ls_max.numerator * abs_num.denominator:
            max_abs_num = num
    summ_num = Rational_numbers.__add__(summ_num, num)

print("Максимальне число:", max_num)
print("Максимальне число за модулем:", max_abs_num)
arithmetic = Rational_numbers.__str__(Rational_numbers.__truediv__(summ_num, Rational_numbers(len(numbers), 1)))
print("Середнє арифметичне значення:", arithmetic)