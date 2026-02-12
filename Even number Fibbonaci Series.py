total= 2 
a = 1 
b = 2 
while a + b < 4000000:
    c = a + b
    if c % 2 == 0:
        total = total+ c 
    a = b
    b = c
print(total)
