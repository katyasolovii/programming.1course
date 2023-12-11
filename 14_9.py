# У папці з програмою міститься набір текстових файлів, кожен з яких містить набір дійсних чисел. Крім цього, у цій же папці міститься файл content.txt, що містить перелік імен файлів.
# Реалізуйте програму, що: 1) підсумовує дані, з файлів, що вказані у файлі content.txt;
# 2)коректно опрацьовує ситуацію, у випадку якщо файл content.txt не існує за вказаним розташуванням або не доступний для читання та виводить на екран відповідне повідомлення;
# 3) коректно опрацьовує ситуацію, у випадку якщо файл з переліку зазначеного у файлі content.txt не існує за вказаним розташуванням або не доступний для читання;
# 4) коректно опрацьовує ситуацію, якщо файл з переліку зазначеного у файлі content.txt містить не лише дійсні числа.


try:
    with open("/Users/katyasolovii/Desktop/programming/lab11/14_9/content.txt", 'r') as file:
        content = file.readlines()
except FileNotFoundError:
    print("FileNotFoundError: файл не знайдено!")
except PermissionError:
    print("PermissionError: файл не доступний для читання!")
total_sum = 0
for line in content:
    file_name = line.strip()
    try:
        with open("/Users/katyasolovii/Desktop/programming/lab11/14_9/" + file_name, 'r') as another_file:
            content_another_file = another_file.read()
            summ = 0
            for el in content_another_file:
                if el.isdigit():
                    summ += int(el)
                elif not el.isspace(): # не враховує пробіли між цифрами
                    raise ValueError()
            total_sum += summ
    except ValueError as e:
        print(f"ValueError: файл {file_name} містить не лише дійсні числа!")
    except FileNotFoundError:
        print(f"FileNotFoundError: файл {file_name} не знайдено!")
    except PermissionError:
        print(f"PermissionError: файл {file_name} не доступний для читання!")
print(total_sum)
