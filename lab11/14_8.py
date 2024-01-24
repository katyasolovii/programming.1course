# До програми з клавіатури надходить послідовність цифр. Послідовність задається доти, щоки користувач не введе слово «досить». 
# Слід зауважити, що користувач не є дисциплінованим і може заміть цифр вводити будь-що. 
# Якщо користувач вводить з клавіатури число більше за 9, то програма ініціює виключення RuntimeError.
# Якщо користувач вводить число менше за 0, то програма ініціює виключення TypeError. Якщо користувач вводить дійсне значення з діапазону 
# від 0 до 9, то програма ініціює виключення ValueError. Підрахувати кількість виключень кожного типу, що виникають у програмі.


count_RuntimeError = 0
count_TypeError = 0
count_ValueError = 0
while True:
    try:
        x = input()
        if x == "досить!!!":
            break
        x = int(x)
        if x > 9:
            count_RuntimeError += 1
            raise RuntimeError
        elif x < 0:
            count_TypeError += 1
            raise TypeError
        elif x >= 0 and x <= 9:
            count_ValueError += 1
            raise ValueError
    except RuntimeError:
        print("Число більше 9!")
    except TypeError as e:
        print("TypeError: Число менше 0!")
    except ValueError:
        print("Число від 0 до 9!")
print(":) Кінець! :)")
print(f"Кількість помилок RuntimeError: {count_RuntimeError}")
print(f"Кількість помилок TypeError: {count_RuntimeError}")
print(f"Кількість помилок ValueError: {count_ValueError}")