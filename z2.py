a=float(input())
b=float(input())
c=str(input())
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='pow':
    print(a**b)
elif c=='mod':
    if b != 0:
        print(a%b)
    else:
        print('Деление на 0!')
elif c=='/':
    if b != 0:
        print(a/b)
    else:
        print('Деление на 0!')
elif c=='div':
    if b != 0:
        print(a//b)
    else:
        print('Деление на 0!')




a = float(input())
b = float(input())
act = input()

if (act=="/" or act=="mod" or act=="div") and b==0:
    c = "Деление на 0!"
elif act=="+":    c = a + b
elif act=="-":    c = a - b
elif act=="/":    c = a / b
elif act=="*":    c = a * b
elif act=="mod":  c = a % b
elif act=="pow":  c = a ** b
elif act=="div":  c = a // b

print (c)