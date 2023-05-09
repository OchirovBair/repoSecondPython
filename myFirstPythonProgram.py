x = int(input())
y = int(input())
str = input()
result = 0
if y == 0 and str == '/':
    print('На ноль делить нельзя!')
elif str == '/' or str == '*' or str == '+' or str == '-':
    if str == '*':
        result = x * y
        print(result)
    elif str == '/':
        result = x / y
        print(result)
    elif str == '+':
        result = x + y
        print(result)
    elif str == '-':
        result = x - y
        print(result)
else:
    print('Неверная операция')
