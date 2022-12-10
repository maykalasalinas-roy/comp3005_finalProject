import sys
from PyQt5 import QtWidgets
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

        # User view signals/setup
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

        # Owner view signals/setup
        self.ui.salesVsExpensesButt.clicked.connect(self.viewSalesVsExpenses)
        self.ui.salesPerAuthorButt.clicked.connect(self.viewSalesPerAuthor)
        self.ui.salesPerGenreButt.clicked.connect(self.viewSalesPerGenre)
        self.ui.salesPerPubButt.clicked.connect(self.viewSalesPerPublisher)

        self.ui.orderBookButt.clicked.connect(self.orderBook)
        self.ui.addBookButt.clicked.connect(self.createBook)
        self.ui.deleteBookButt.clicked.connect(self.deleteBook)

        self.show()

    def disableOwnerView(self):
        '''When the radio button for the User View is checked, changes the ui from Owner to User'''
        self.populateISBN()
        self.ui.ownerViewButt.setChecked(False)

        self.ui.ownerViewFrame.hide()
        self.ui.ownerViewFrame.setEnabled(False)

        self.ui.userViewFrame.show()
        self.ui.userViewFrame.setEnabled(True)

    def disableUserView(self):
        '''When the radio button for the Owner View is checked, changes the ui from User to Owner'''
        self.ui.userViewButt.setChecked(False)

        self.ui.ownerViewFrame.show()
        self.ui.ownerViewFrame.setEnabled(True)
        self.populateDropDowns()

        self.ui.userViewFrame.hide()
        self.ui.userViewFrame.setEnabled(False)

    def populateISBN(self):
        '''Clears the dropdown for the isbn in User View and populates it with isbns from the database'''
        self.ui.inISBN.clear()
        self.ui.inISBN.addItems(qf.getISBN())

    def login(self):
        '''Logs a user in if they given email exists'''
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
        '''Registers a user given all the information inputted by adding it to the database'''
        e = self.ui.emailReg.text()
        fn = self.ui.fnameReg.text()
        ln = self.ui.lnameReg.text()
        a = self.ui.addressReg.text()
        b = self.ui.bankReg.text()

        dmf.registerUser(e, fn, ln, a, b)
        self.ui.emailLogin.setText(e)
        self.login()

    def searchISBN(self):
        '''Queries the database for the book given the isbn and displays the output'''
        q = self.ui.inSearch.text()
        self.ui.qResults.addItem(qf.bookByISBN(q))

    def searchTitle(self):
        '''Queries the database for the book given the title and displays the output'''
        q = self.ui.inSearch.text()
        self.ui.qResults.addItem(qf.bookByTitle(q))

    def searchAuthor(self):
        '''Queries the database for the book given the author and displays the output'''
        q = self.ui.inSearch.text()
        temp = q.split() # need author fname and lname

        if(len(temp) < 2):
            self.ui.qResults.addItem(qf.bookByAuthor(temp[0], ""))
        else:
            self.ui.qResults.addItem(qf.bookByAuthor(temp[0], temp[1]))

    def searchPublisher(self):
        '''Queries the database for the book given the publisher and displays the output'''
        q = self.ui.inSearch.text()
        temp = q.split() # need publisher fname and lname

        if(len(temp) < 2):
            self.ui.qResults.addItem(qf.bookByPublisher(temp[0], ""))
        else:
            self.ui.qResults.addItem(qf.bookByPublisher(temp[0], temp[1]))

    def searchGenre(self):
        '''Queries the database for the book given the genre and displays the output'''
        q = self.ui.inSearch.text()
        self.ui.qResults.addItem(qf.bookByGenre(q))

    def viewBook(self):
        '''Queries the database for the book given the isbn and displays the detailed output'''
        q = self.ui.inISBN.currentText()
        self.ui.qResults.addItem(qf.viewBook(q))

        # Makes the quantity dropdown have accurate information
        max = qf.getQuantity(q)
        self.ui.quantitySpin.setMaximum(max)
        self.ui.quantitySpin.setMinimum(1)

    def addToCart(self):
        '''Adds the isbn and quantity to the cart'''
        b = self.ui.inISBN.currentText()
        q = self.ui.quantitySpin.value()
        self.cart.append((b, q))

        if(self.userEmail != ""):
            self.ui.checkoutButt.setEnabled(True)

    def viewCart(self):
        '''Displays the contents of the cart'''     
        text = "isbn | title | quantity\n"
        for c in self.cart:
            text += f"{c[0]} | {qf.getTitle(c[0])} | {c[1]}\n"

        self.ui.qResults.addItem(text)

    def checkout(self):
        '''For when a user checks out, order gets added to the database and cart is cleared'''
        a = self.ui.addressCheckout.text()
        b = self.ui.bankCheckout.text()

        dmf.makeBookOrder(self.nextOrder, self.userEmail, a, b, self.cart)

        self.ui.qResults.addItem(f"Your order number is: {self.nextOrder}")
        self.nextOrder += 1

        q = self.ui.inISBN.currentText()

        if(q):
            max = qf.getQuantity(q)
            self.ui.quantitySpin.setMaximum(max)
            self.ui.quantitySpin.setMinimum(1)

        self.cart = []
        self.ui.checkoutButt.setEnabled(False)

    def viewOrders(self):
        '''Shows the books in the given order'''
        n = int(self.ui.orderNum.text())
        self.ui.qResults.addItem(qf.viewOrder(n))

    # Owner view
    def populateDropDowns(self):
        '''Clears and populates the publisher email, author name, and genre dropdowns'''
        self.ui.pubEmailNew.clear()
        self.ui.authorNew.clear()
        self.ui.genreNew.clear()

        self.ui.pubEmailNew.addItems(qf.getPublishers())
        self.ui.authorNew.addItems(qf.getAuthors())
        self.ui.genreNew.addItems(qf.getGenres())

    def viewSalesVsExpenses(self):
        '''Displays the sales vs expenses report'''
        t = qf.salesVsExpenses()
        self.ui.qResults_2.addItem(t)

    def viewSalesPerAuthor(self):
        '''Displays the sales per author report'''
        t = qf.getSalesPerAuthor()
        self.ui.qResults_2.addItem(t)

    def viewSalesPerGenre(self):
        '''Displays the sales per genre report'''
        t = qf.getSalesPerGenre()
        self.ui.qResults_2.addItem(t)

    def viewSalesPerPublisher(self):
        '''Displays the sales per publisher report'''
        t = qf.getSalesPerPublisher()
        self.ui.qResults_2.addItem(t)

    def orderBook(self):
        '''Orders book from publisher'''
        b = self.ui.isbnOrder.text()
        q = int(self.ui.quantityOrder.text())

        text = dmf.orderBook(b, q)
        self.ui.qResults_2.addItem(text)

        uViewBook = self.ui.inISBN.currentText()

        if(uViewBook == b):
            max = qf.getQuantity(b)
            self.ui.quantitySpin.setMaximum(max)
            self.ui.quantitySpin.setMinimum(1)

    def createBook(self):
        '''Creates new book in the database'''
        isbn = self.ui.isbnNew.text()
        pub = self.ui.pubEmailNew.currentText()
        title = self.ui.titleNew.text()
        pages = int(self.ui.pagesNew.text())
        price = float(self.ui.priceNew.text())
        pubPercent = float(self.ui.pubPercentNew.text())
        author = self.ui.authorNew.currentText()
        genre = self.ui.genreNew.currentText()

        author = author.split()

        dmf.newBook(isbn, pub, title, pages, price, pubPercent, author[0], author[1], genre)

        self.ui.qResults_2.addItem(f"Book added:\n{qf.viewBook(isbn)}")

    def deleteBook(self):
        '''Deletes book specified by isbn'''
        isbn = self.ui.isbnDelete.text()
        text = dmf.deleteBook(isbn)

        self.ui.qResults_2.addItem(text)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

main()