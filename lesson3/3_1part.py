print('Calculator')

try:
    a = float(input('a = '))
    b = float(input('b = '))
    print(a / b)
except ZeroDivisionError:
    print('division by zero')

print('Stopping the calculator.')