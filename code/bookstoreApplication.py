import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

import queryFunctions as qf
import dmFunctions as dmf

# I couldn't remember how to setup the initial window so I used the tutorial from this site: https://www.pythonguis.com/tutorials/pyqt6-first-steps-qt-designer/
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__() 
        self.userEmail = ""
        self.cart = []
        self.nextOrder = qf.getMaxOrderNum() + 1

        self.ui = uic.loadUi('mainWindow.ui', self)

        self.ui.userViewButt.toggled.connect(self.disableOwnerView)
        self.ui.ownerViewButt.toggled.connect(self.disableUserView)

        self.ui.loginButt.clicked.connect(self.login)
        self.ui.registerButt.clicked.connect(self.register)

        self.ui.isbnButt.clicked.connect(self.searchISBN)
        self.ui.titleButt.clicked.connect(self.searchTitle)
        self.ui.authorButt.clicked.connect(self.searchAuthor)
        self.ui.publisherButt.clicked.connect(self.searchPublisher)
        self.ui.genreButt.clicked.connect(self.searchGenre)

        self.ui.viewButt.clicked.connect(self.viewBook)

        self.ui.cartButt.clicked.connect(self.addToCart)
        self.ui.viewCartButt.clicked.connect(self.viewCart)
        self.ui.checkoutButt.clicked.connect(self.checkout)
        self.ui.viewOrdersButt.clicked.connect(self.viewOrders)

        self.disableOwnerView()
        self.ui.checkoutButt.setEnabled(False)
        self.ui.quantitySpin.setMaximum(0)
        self.ui.quantitySpin.setMinimum(0)

        self.show()

    def disableOwnerView(self):
        self.ui.ownerViewButt.setChecked(False)

        self.ui.ownerViewFrame.hide()
        self.ui.ownerViewFrame.setEnabled(False)

        self.ui.userViewFrame.show()
        self.ui.userViewFrame.setEnabled(True)

    def disableUserView(self):
        self.ui.userViewButt.setChecked(False)

        self.ui.ownerViewFrame.show()
        self.ui.ownerViewFrame.setEnabled(True)


        self.ui.userViewFrame.hide()
        self.ui.userViewFrame.setEnabled(False)

    def login(self):
        t = qf.findUser(self.ui.emailLogin.text())
        if(t):
            self.userEmail = t[0]
            self.ui.addressCheckout.setText(t[1])
            self.ui.bankCheckout.setText(t[2])

            if(len(self.cart) > 0):
                self.ui.checkoutButt.setEnabled(True)

            print("logged in")
        else:
            print("user does not exist")

    def register(self):
        e = self.ui.emailReg.text()
        fn = self.ui.fnameReg.text()
        ln = self.ui.lnameReg.text()
        a = self.ui.addressReg.text()
        b = self.ui.bankReg.text()

        dmf.registerUser(e, fn, ln, a, b)
        self.ui.emailLogin.setText(e)
        self.login()

    def searchISBN(self):
        q = self.ui.inSearch.text()
        self.ui.qResults.setText(qf.bookByISBN(q))

    def searchTitle(self):
        q = self.ui.inSearch.text()
        self.ui.qResults.setText(qf.bookByTitle(q))

    def searchAuthor(self):
        q = self.ui.inSearch.text()
        temp = q.split()
        self.ui.qResults.setText(qf.bookByAuthor(temp[0], temp[1]))

    def searchPublisher(self):
        q = self.ui.inSearch.text()
        temp = q.split()
        self.ui.qResults.setText(qf.bookByPublisher(temp[0], temp[1]))

    def searchGenre(self):
        q = self.ui.inSearch.text()
        self.ui.qResults.setText(qf.bookByGenre(q))

    def viewBook(self):
        q = self.ui.inISBN.text()
        self.ui.qResults.setText(qf.viewBook(q))

        max = qf.getQuantity(q)
        self.ui.quantitySpin.setMaximum(max)
        self.ui.quantitySpin.setMinimum(1)

    def addToCart(self):
        b = self.ui.inISBN.text()
        q = self.ui.quantitySpin.value()
        self.cart.append((b, q))

        if(self.userEmail != ""):
            self.ui.checkoutButt.setEnabled(True)

    def viewCart(self):        
        text = "isbn | title | quantity\n"
        for c in self.cart:
            text += f"{c[0]} | {qf.getTitle(c[0])} | {c[1]}\n"

        self.ui.qResults.setText(text)

    def checkout(self):
        a = self.ui.addressCheckout.text()
        b = self.ui.bankCheckout.text()

        dmf.makeBookOrder(self.nextOrder, self.userEmail, a, b, self.cart)

        self.ui.qResults.setText(f"Your order number is: {self.nextOrder}")
        self.nextOrder += 1

        q = self.ui.inISBN.text()

        max = qf.getQuantity(q)
        self.ui.quantitySpin.setMaximum(max)
        self.ui.quantitySpin.setMinimum(1)

        self.cart = []

    def viewOrders(self):
        n = int(self.ui.orderNum.text())
        self.ui.qResults.setText(qf.viewOrder(n))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

main()