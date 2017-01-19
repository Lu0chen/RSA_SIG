import random
import time
import sys
sys.path.append("F:\codes\RSA_SIG")
from PyQt4 import QtCore, QtGui
from untitled import Ui_MainWindow
'''
class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)
    def write(self, text):
        self.textWritten.emit(str(text))
'''

class Main(QtGui.QMainWindow):
    p = q = 0
    n = e = N = c = 0
    def __init__(self):
        super(Main, self).__init__()

        # build ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #def isPrime(self):

        self.ui.pushButton.clicked.connect(self.createPrime)
        self.ui.pushButton_3.clicked.connect(self.gcd)
        self.ui.pushButton_5.clicked.connect(self.mo_chongfu)
        self.ui.pushButton_7.clicked.connect(self.mo_pingfang)
        self.ui.pushButton_2.clicked.connect(self.getCode)

        #p, q = isPrime(self)

        #while (p != 0):
        # connect signals
        #self.ui.some_button.connect(self.on_button)
        '''
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        sys.stderr = EmittingStream(textWritten=self.normalOutputWritten)
    def __del__(self):
        # Restore sys.stdout
        sys.stdout = sys.__stdout__
    def normalOutputWritten(self, text):
        cursor = self.textBrowser_9.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser_9.setTextCursor(cursor)
        self.textBrowser_9.ensureCursorVisible()
'''
    def createPrime (self):
        # Create and confirm prime number
        self.ui.textBrowser_9.append('----------------------------------')
        self.ui.textBrowser_9.append ("Step1: Create Prime number")
        thousand_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                            97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
                            191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
                            283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
                            401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
                            509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619,
                            631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743,
                            751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
                            877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
        p = self.p
        q = self.q
        p = random.randint(2 ** 10, 2 ** 11)
        flag = 0
        while (flag == 0):
            for i in range(2, p):
                if (p % i) == 0:
                    flag = 0
                    p = random.randint(2 ** 10, 2 ** 11)
                    break
                else:
                    flag = 1
        print '\n'
        #print "Create the first prime number that between 2^10~2^11"
        self.ui.textBrowser_9.append('Create the first prime number that between 2^10~2^11,is:' + str(p))
        #print "Use", p, " % ", 181, " = ",
        self.ui.textBrowser_9.append('Use primes that < 1000 to / it')
        for  i in thousand_prime:
            flag = p % i
            self.ui.textBrowser_9.append ("Use " + str(p) +  " % " + str(i) +  " = " + str(flag))
        if (flag != 0):
            self.ui.textBrowser_9.append( "The result is not 0 :)")
        else:
            self.ui.textBrowser_9.append( "The result is 0 :(")
        self.ui.textBrowser_9.append("\n")
        self.ui.textBrowser_9.append( "Use Miller-Rabin-Test to check")
        for i in range(0, 5):
            b = random.randint(1, p - 1)
            self.ui.textBrowser_9.append( str(b) +  "^" + str(p - 1) +  "-1 % " + str(p) +  " = " +  str((b ** (p - 1) - 1) % p))
        #print "So the first number is:",
        self.ui.textBrowser_9.append("So the first number is: "+ str(p))

        q = random.randint(2 ** 16, 2 ** 17)
        flag = 0
        while (flag == 0):
            for i in range(2, q):
                if (q % i) == 0:
                    flag = 0
                    q = random.randint(2 ** 16, 2 ** 17)
                    break
                else:
                    flag = 1
        print '\n'
        self.ui.textBrowser_9.append ('Create the second prime number 2^16~2^17,is: ' + str(q))
        self.ui.textBrowser_9.append('Use primes that < 1000 to / it')
        for i in thousand_prime:
            flag = p % i
            self.ui.textBrowser_9.append("Use " + str(p) + " % " + str(i) + " = " + str(flag))
        if (flag != 0):
            self.ui.textBrowser_9.append ("The result is not 0 :)")
        else:
            self.ui.textBrowser_9.append ("The result is 0 :(")

        self.ui.textBrowser_9.append ("Use Miller-Rabin-Test to check")
        for i in range(0, 5):
            b = random.randint(1, q - 1)
            self.ui.textBrowser_9.append (str(b) +  "^" +  str(q - 1) +  "-1 % " +  str(q) +  " = " +  str((b ** (q - 1) - 1) % q))

        self.ui.textBrowser_9.append ("So the second number is:" + str(q))
        self.ui.textBrowser.append(str(p))
        self.ui.textBrowser_3.append(str(q))
        self.q = q
        self.p = p
        return self.q, self.p

    def gcd(self):
        # a = e % N
        self.ui.textBrowser_9.append('----------------------------------')
        self.ui.textBrowser_9.append ("Step2: Get value of d")
        self.n = self.p * self.q
        n = self.n
        self.ui.textBrowser_9.append('n = firstPrime * secondPrime = ' + str(self.p) + '*' + str(self.q) + '=' + str(n))
        self.ui.textBrowser_4.append (str(n))
        e = 17
        N = (self.p - 1) * (self.q - 1)
        self.N = N
        self.ui.textBrowser_9.append('N = (firstPrime-1) * (secondPrime-1) = '+ str(self.p)+ '-1' + '*' + str(self.q) + '-1' + '=' + str(N))
        self.ui.textBrowser_5.append(str(N))
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
        self.ui.textBrowser_9.append ("The value of d is: " +  str(y0))
        self.ui.textBrowser_6.append(str(y0))
        self.d = y0
        return self.d,self.n,self.N

    def getCode(self):
        self.code = self.ui.lineEdit.text()
        return self.code

    def mo_chongfu(self):
        # type: (object, object, object) -> object
        m = self.m = int(self.code)
        e = self.e = 17
        n = self.n
        self.ui.textBrowser_9.append ('----------------------------------')
        self.ui.textBrowser_9.append ("Step3: RSA encode")

        mo_er = [1]
        flag = 0
        while e != 0:
            mo_er[flag] = e % 2
            flag += 1
            e = e / 2
            mo_er.append(1)
        mo_er.pop()
        print mo_er


        #10001
        #111111110001111
        self.ui.textBrowser_9.append ("The Binary number of expressly:" + str(mo_er));

        a = 1
        for i in mo_er:
            if i == 1:
                a = a * m % n
            m = m * m % n
            self.ui.textBrowser_9.append ('i = ' + str(i) + ' | ' + 'a = ' + str(a) + ' ' + 'm = ' + str(m))
        self.ui.textBrowser_9.append ('The result of mochongfu is:%s(mod%s)' % (str(a), str(n)))
        self.ui.textBrowser_7.append (str(a))
        self.c = a
        return self.c

    def mo_pingfang(self):
        #x, n, m, flag, jinzhi
        print self.p,self.q,self.e, self.d, self.n, self.N, self.code, self.c
        self.ui.textBrowser_9.append('----------------------------------')
        self.ui.textBrowser_9.append ("Step4: RSA decode")

        c = self.c
        d = self.d
        n = self.n

        #jinzhi = [1]
        flag = 0
        '''
        while n:
            jinzhi[flag] = n % 2
            n = n / 2
            flag = flag + 1
            jinzhi.append(1)
        # flag = flag - 1
        jinzhi.pop()
        '''
        flag = bin(d)
        flag = flag[2:]
        self.ui.textBrowser_9.append (str(flag))

        a = 1

        for i in flag:
            i = int(i)
            if i:
                a = a * a % n
                a = a * c % n
            else:
                a = a * a % n

            self.ui.textBrowser_9.append ("i = %s, s = %s" %(str(i), str(a)))
        self.ui.textBrowser_8.append (str(a))
        self.a = a
        return self.a

'''
    def mo_pingfang(self):
        self.ui.textBrowser_9.append('----------------------------------')
        self.ui.textBrowser_9.append("Step4: RSA decode")

        x = self.c
        n = self.n
        m = self.N
        self.ui.textBrowser_9.append (str(x))

        a = 1
        b = x
        i = 0
        while n > 0:
            if n == 0:
                return a
            if n % 2 == 1:
                a = a * b % m
            b = b * b % m
            n /= 2
            self.ui.textBrowser_9.append ("i = %s, n[i] = %s, s = %s" % (str(i), str(n % 2), str(a)))
            i += 1
        self.ui.textBrowser_8.append (str(a))
        self.a = a
        return self.a
'''



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())