a=int(input())
b=int(input())
c=int(input())
s=a+b+c
print(max(a,b,c))
print(min(a,b,c))
print(s-max(a,b,c)-min(a,b,c))



a=int(input())
b=int(input())
c=int(input())
if c<a<b:
   print(b)
   print(c)
   print(a)
if b<c<a:
   print(a)
   print(b)
   print(c)
if a<b<c:
   print(c)
   print(a)
   print(b)
if a<c<b:
   print(b)
   print(a)
   print(c)
if b<a<c:
   print(c)
   print(b)
   print(a)
if c<b<a:
   print(a)
   print(c)
   print(b)
if a==b<c:
   print(c)
   print(b)
   print(a)
if a==b==c:
   print(a)
   print(b)
   print(c)
if c==b<a:
   print(a)
   print(b)
   print(c)
if c==a<b:
   print(b)
   print(a)
   print(c)
if c<a==b:
   print(b)
   print(c)
   print(a)
if b<a==c:
   print(c)
   print(b)
   print(a)
if a<c==b:
   print(b)
   print(a)
   print(c)