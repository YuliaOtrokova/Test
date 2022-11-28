i = 0
count =''
while i < 5:
    count +='*'
    if i % 2 == 0:
        count +='**'
    if i > 2:
        count +='***'
    i = i + 1

print(len(count))
