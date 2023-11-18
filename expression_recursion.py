def expressions_rec(n):
# перевірка на дужки
    open_p = n.find("(") # перший пріорітет - дужки
    if open_p != -1: # розташування "("
        close_p = n.find(")")
        if close_p != -1: # розташування ")"
            inside_n = expressions_rec(n[open_p + 1:close_p]) # беремо тільки той вираз, який в дужках і знову на початок рекурсії
            n = n[:open_p] + str(inside_n) + n[close_p + 1:] # видаляємо все що було в дужках, замість цього вставляємо результат обчисленого виразу
            return expressions_rec(n)
    tokens = n.split() # розділяємо вираз ['8.2', '-', '12', '/', '3'], ['8.2', '-', '4.0'], ['2', '+', '4.2', '*', '4.199999999999999'], ['2', '+', '17.639999999999997']
    for num, token in enumerate(tokens): # другий праорітет на дію * та /
        if token == "*":
            res = float(tokens[num - 1]) * float(tokens[num + 1])
            tokens = tokens[:num - 1] + [str(res)] + tokens[num + 2:] # замінюємо в tokens дію множення на результат цієї дії 
            return expressions_rec(' '.join(tokens))
        elif token == "/":
            res = float(tokens[num - 1]) / float(tokens[num + 1])
            tokens = tokens[:num - 1] + [str(res)] + tokens[num + 2:] # замінюємо в tokens дію ділення на результат цієї дії 
            return expressions_rec(' '.join(tokens)) # новим вираз йде на початок рекурсії
    res = float(tokens[0]) # третій пріорітет на дію + та -
    for num in range(1, len(tokens)): 
        if tokens[num] == "+":
            res += float(tokens[num + 1])
        elif tokens[num] == "-":
            res -= float(tokens[num + 1])
    return res 


n = input()
try:
    print(expressions_rec(n)) 
except ZeroDivisionError as e:
    print(f"ZeroDivisionError")
except Exception as e:
    print(f"помилка")