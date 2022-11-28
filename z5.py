n = int (input ())
if (n % 100>=11 and n%100<= 19) or (n%10==0 or n%10>=5 and n%10<=9):
    print (n, " программистов")
elif n%10==2 or n%10==3 or n%10==4:
    print (n, " программиста")
else:
    print (n, " программист")




