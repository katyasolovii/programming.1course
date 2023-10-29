"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14929278
"""
math_expression = input()
operations = "+-%/*"
summ_op = ""
for i in math_expression:
    if i in operations:
        summ_op += i
s1 = summ_op.count("*") - summ_op.count("**")
s2 = summ_op.count("/") - summ_op.count("//") 
summ = s1 + s2 + summ_op.count("-") + summ_op.count("%") + summ_op.count("+")
print(summ)