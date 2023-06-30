print("Enter your choice according to operations given below")
print("* - Multiplication, + = Addition, - = Subtraction / = Division")
print("pwr = x^y, root = x root y, end = finish")


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def pwr(x, y):
    return x ** y


def root(x, y):
    return x ** (1 / y)


prevIn = 0
num = int(input("Enter your numbers. If you'd like to stop calculating, type end: "))
num2 = int(input())
total = 0
ch = input('Enter your choice')
if ch == '+':
    total = add(num, num2)
if ch == '-':
    total = sub(num, num2)
if ch == '*':
    total = mul(num, num2)
if ch == '/':
    total = div(num, num2)
if ch == 'pwr':
    total = pwr(num, num2)
if ch == 'root':
    total = root(num, num2)
prevIn = total

while True:
    print(prevIn)
    ch = input('Enter next operation: ')
    if ch == 'end':
        break
    newnum = int(input('Enter next number: '))
    if ch == '+':
        total = add(prevIn,newnum)
    if ch == '-':
        total = sub(prevIn,newnum)
    if ch == '*':
        total = mul(prevIn,newnum)
    if ch == '/':
        total = div(prevIn,newnum)
    if ch == 'pwr':
        total = pwr(prevIn,newnum)
    if ch == 'root':
        total = root(prevIn,newnum)
    prevIn = total

print('Final Output:',total)
