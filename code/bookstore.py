import queryFunctions as qf

'''qf.bookByGenre("Thriller")

qf.c.close()
qf.conn.close()'''
def searchView():
    opt = 0
    opt = int(input("\n----Search View---- \n1. ISBN \n2. Title \n3. Author \n4. Publisher \n5. Genre \nEnter the listed number to select an option: "))

def ownerView():
    opt = 0
    opt = int(input("\n----Owner View---- \n1. Add a new book \n2. Delete a book \n3. Sales Report \n4. Expenses Report \n5. Back to main menu \nEnter the listed number to select an option: "))

def customerView():
    opt = 0
    opt = int(input("\n----Customer View---- \n1. Login \n2. Register \n3. View Cart \n4. Search \n5. Back to main menu \nEnter the listed number to select an option: "))

def registeredUserView():
    opt = 0
    opt = int(input("\n----Registered User View---- \n1. View Cart \n2. Search \n3. Checkout \n4. View order tracking \n5. Back to main menu \nEnter the listed number to select an option: "))

def main():
    view = 0
    close = 0   

    view = int(input("\nWelcome to Look Inna Book online bookstore! \n1. Owner view\n2. Customer view \n3. Close program \nEnter the listed number to select an option: "))   

    while close == 0:
        while view != 1 and view != 2 and view != 3:
            view = int(input("\n1. Owner view\n2. Customer view \n3. Quit \nEnter the listed number to select an option: "))   

        if(view == 1):
            ownerView()
            view = 0
        elif(view == 2):
            customerView()
            view = 0
        else:
            close = 1
            break
main()