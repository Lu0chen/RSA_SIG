mo_er = [1,0,1,1,1]
flag = [1,0,1,0,1,1,0,1]
e = 29
d = 173
n = 299
m = 9

a = 1
for i in mo_er:
    if i == 1:
        a = a * m % n
    m = m * m % n

x = a
print x

a = 1
for i in flag:
    if i:
        a = a * a % n
        a = a * x % n
    else:
        a = a * a % n

print a
