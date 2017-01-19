# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(796, 892)
        MainWindow.setMaximumSize(QtCore.QSize(796, 16777215))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(9, 9, 771, 51))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 221, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 71, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 71, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(100, 120, 161, 31))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(100, 160, 161, 31))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 80, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 181, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 250, 41, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.textBrowser_4 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(100, 250, 161, 31))
        self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 300, 51, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.textBrowser_5 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(100, 300, 161, 31))
        self.textBrowser_5.setObjectName(_fromUtf8("textBrowser_5"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 350, 101, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 390, 51, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.textBrowser_6 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(100, 380, 161, 31))
        self.textBrowser_6.setObjectName(_fromUtf8("textBrowser_6"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 220, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 440, 211, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 540, 221, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 590, 61, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.textBrowser_7 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_7.setGeometry(QtCore.QRect(110, 580, 161, 31))
        self.textBrowser_7.setObjectName(_fromUtf8("textBrowser_7"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 450, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 620, 241, 31))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 670, 181, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 710, 61, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.textBrowser_8 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_8.setGeometry(QtCore.QRect(100, 710, 161, 31))
        self.textBrowser_8.setObjectName(_fromUtf8("textBrowser_8"))
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(220, 630, 75, 23))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.textBrowser_9 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_9.setGeometry(QtCore.QRect(330, 80, 451, 761))
        self.textBrowser_9.setObjectName(_fromUtf8("textBrowser_9"))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(40, 500, 81, 21))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.textBrowser_10 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_10.setGeometry(QtCore.QRect(110, 500, 101, 31))
        self.textBrowser_10.setObjectName(_fromUtf8("textBrowser_10"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 500, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600;\">         RSA签名算法实现</span><span style=\" font-size:26pt; vertical-align:sub;\">--by Lu0chen</span></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">第一步：生成大素数</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">第一个素数：</span></p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">第二个素数：</span></p><p><span style=\" font-size:10pt;\"><br/></span></p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "生成", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">第二步：得到参数值</span></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">n:</span></p></body></html>", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:11pt; color:#333333; background-color:#ffffff;\">φ(n)：</span></p></body></html>", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">公钥 </span><span style=\" font-size:11pt; font-weight:600;\">e</span><span style=\" font-size:11pt;\"> = 17</span></p></body></html>", None))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>私钥 <span style=\" font-weight:600;\">d：</span></p></body></html>", None))
        self.pushButton_3.setText(_translate("MainWindow", "Get it ", None))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">第三步：加密（签名）</span></p></body></html>", None))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">经过复杂的运算后。。。。。</span></p></body></html>", None))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">得到密文：</span></p></body></html>", None))
        self.pushButton_5.setText(_translate("MainWindow", "签名", None))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">第四步：解密</span></p></body></html>", None))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">经过繁琐的运算后。。。。。</span></p></body></html>", None))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">得到明文：</span></p></body></html>", None))
        self.pushButton_7.setText(_translate("MainWindow", "解密", None))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p>输入明文：</p></body></html>", None))
        self.pushButton_2.setText(_translate("MainWindow", "输入", None))
'''
import rsa2_rc
import rsa3_rc
import rsa_rc
'''
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

