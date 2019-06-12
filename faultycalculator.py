while 5>3:
    print("enter the no.1")
    a = int(input())
    print("enter the no.2")
    b = int(input())
    print('which operation do you want to perform-: +,-,*,/ ')
    c=input()
    if a == 56 and b == 9 and c == '+':
        print("77")
    elif a == 56 and b == 6 and c == '/':
        print("4")
    elif a == 45 and b == 3 and c == '*':
        print("555")
    elif c == '+':
        sum = a + b
        print(sum)

    elif c == '*':
        multiply=a*b
        print(multiply)
    elif c == '-':
        sub = a-b
        print(sub)
    elif c == '/':
        div = a/b
        print(div)
    s=input((print('press "Y" or "N"...')))
    if s == "N":
        break













