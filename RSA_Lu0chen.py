#2016.11.8 22:48
#By Lu0chen

import  random


def IsPrime():
    #Create and confirm prime number
    global p
    global q
    p = random.randint(2**10, 2**11)
    flag = 0
    while (flag == 0):
        for i in range(2, p):
            if (p % i) == 0:
                flag = 0
                p = random.randint(2**10, 2**11)
                break
            else:
                flag = 1
    print '\n'
    print "Create the first prime number that between 2^10~2^11"
    print "Use",p," % ",181," = ",
    flag = p % 181
    print flag
    if (flag != 0):
        print "The result is not 0 :)"
    else:
        print "The result is 0 :("

    print "Use Miller-Rabin-Test to check"
    for i in range (0, 5):
        b = random.randint(1, p-1)
        print b,"^",p-1,"-1 % ",p," = ",(b**(p-1)-1) % p
    print "So the first number is:",
    print p

    q = random.randint(2**16, 2**17)
    flag = 0
    while (flag == 0):
        for i in range(2, q):
            if (q % i) == 0:
                flag = 0
                q = random.randint(2**16, 2**17)
                break
            else:
                flag = 1
    print '\n'
    print 'Create the second prime number 2^16~2^17,is: '
    print "Use",q," % ",181," = ",
    flag = q % 181
    print flag
    if (flag != 0):
        print "The result is not 0 :)"
    else:
        print "The result is 0 :("

    print "Use Miller-Rabin-Test to check"
    for i in range (0, 5):
        b = random.randint(1, q-1)
        print b,"^",q-1,"-1 % ",q," = ",(b**(q-1)-1) % q

    print "So the second number is:",
    print q
    return p
    return q
'''
def gcd(e, N):
    d = N
    b = e
    d = (-N + (N**2 - 4*b)**(1/2))/(2*b)
    #d = (-N - (N**2 - 4*b)**(1/2))/(2*b)
    if d < 0:
        d = d + N

    else:
        d = d
    while(d % b != 0):
        temp = d % b
        d = b
        b = temp
        print b
    return b

    print "The value of d is: ",d
    return d
'''

def gcd(e, N):
    #a = e % N
    a = e
    b = N
    a = e % N
    b = N

    x = 0
    y = 1
    x0 = 1
    y0 = 0
    q = temp = 0
    while (a != 0):
        q = b / a
        temp = b % a
        b = a
        a = temp
        temp = x
        x = x0 - q * x
        x0 = temp
        temp = y
        y = y0 - q * y
        y0 = temp

    if (y0 < 0):
	    y0 += N

    print "The value of d is: ",y0
    return y0


def mo_chongfu (a,m,n):
    # type: (object, object, object) -> object

    mo_er = [1]
    mo_weishu = 0
    while m != 0:
        mo_er[mo_weishu] = m % 2
        m = m / 2
        mo_weishu = mo_weishu + 1
        mo_er.append(1)
    mo_er.pop()

    print mo_er;
    y = 1
    for i in mo_er:
        if i == 1:
            a = a * m % n
        m = m * m % n
        print('i = ' + str(i) + ' | ' + 'a = ' + str(a) + ' ' + 'm = ' + str(m))

    print 'The result of mochongfu is:%d(mod%d)' %(y,n)
    return y

def jinzhi(n):
    jinzhi = [1]
    flag = 0
    while n:
        jinzhi[flag] = n % 2
        n = n / 2
        flag = flag + 1
        jinzhi.append(1)
    flag = flag - 1
    return flag, jinzhi

def mo_pingfang(x, n, m, flag, jinzhi):
    a = 1
    i = 0        
        
    while flag >= 0:
        if jinzhi[i] > 0:
            a = a * a % m
            a = a * x % m
        else:
            a = a * a % m
        #print "i = %d, n[i] = %d, s = %d" % (jinzhi[i],n%2,a)
        print jinzhi[i]
        i += 1
        flag -= 1
    return a


if __name__ == '__main__':
    print "RSA signature algorithm"
    print "By  Lu0chen"
    print "-----------------------------"
    print "Step1: Create Prime number"
    global p, q
    IsPrime()
    e = 17
    N = (p - 1) * (q - 1)
    print "The value of N is: ", N
    print "Step2: Get value of d"
    d = gcd(e, N)
    print "Step3: RSA encode"
    m = 32655
    n = (p * q)
    c = mo_chongfu(m, e, n)
    print "Step4: RSA decode"
    flag,zhuanhuan = jinzhi(d)
    print flag
    print zhuanhuan
    print mo_pingfang(c, d, n, flag, zhuanhuan)
