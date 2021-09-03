def fact(sub):
    f_su = 1
    for i in range(sub + 1):
        yield f'{i}! = {f_su}'
        f_su *= i + 1

for subj in fact(int(input("Factorial = "))):
    print(subj)
