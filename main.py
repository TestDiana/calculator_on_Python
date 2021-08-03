a = float(input())
b = float(input())
z = input()

if z == '+':
    print(a + b)
elif z == '-':
    print(a - b)
elif z == '/' and b != 0:
    print(a / b)
elif b == 0 and z == '/':
    print('Деление на 0!')
elif z == '*':
    print(a * b)
elif z == 'mod' and b != 0:
    print(a % b)
elif b == 0 and z == 'mod':
    print('Деление на 0!')
elif z == 'pow':
    print(a ** b)
elif z == 'div' and b != 0:
    print(a // b)
elif b == 0 and z == 'div':
    print('Деление на 0!')
else: print("Unknown operator")

