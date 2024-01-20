"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15270272
"""


def permutations(n):
    # База
    if n == 1:
        return ["1"]
    count_perm = permutations(n - 1)
    res = []
    for el in count_perm:
        for i in range(n):
            new_perm = el[:i] + str(n) + el[i:]
            res.append(new_perm)
    return res


n = int(input())
result = permutations(n)
result.sort()
for lst in result:
    sort_lst = ' '.join(lst)
    print(sort_lst)