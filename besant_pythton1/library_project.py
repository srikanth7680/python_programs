##
class library:
    def showing_books(self):
        a = ["1.the book\n","2.It ends\n","3.It starts\n","4.Destination\n"]
        print("These are the books")
    def withdraw_books(self):
        print("withdraw books is the book")
    def credit_books(self):
        print("These books are the credited")
    def user_accounts(self):
        print("These are the users")
a1 = library()
a1.showing_books()
a1.withdraw_books()
a1.credit_books()
a1.user_accounts()
class readers(library):
    def login(self):
        print("The login time is 9'o clock")
    def logout(self):
        print("The logout time is 12'o clock")
    def return_book(self):
        print("This is the return book")
    def lending_book(self):
        print("This is the lending book")
b1 = readers()
b1.login()
b1.logout()
b1.return_book()
b1.lending_book()