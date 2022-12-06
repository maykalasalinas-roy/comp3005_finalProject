import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
import queryFunctions as qf

# I couldn't remember how to setup the initial window so I used this site: https://www.pythonguis.com/tutorials/pyqt6-first-steps-qt-designer/
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__() 
        self.userEmail = ""
        self.cart = []

        self.ui = uic.loadUi('mainWindow.ui', self)

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

        self.show()

    def login(self):
        if(qf.findUser(self.ui.emailLogin.text())):
            self.userEmail = self.ui.emailLogin.text()
            print("logged in")
        else:
            print("user does not exist")

    def register(self):
        print("register")

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

    def addToCart(self):
        b = self.ui.inISBN.text()

    def viewCart(self):
        print("view cart")

    def checkout(self):
        print("checkout")

    def viewOrders(self):
        print("view orders")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

main()