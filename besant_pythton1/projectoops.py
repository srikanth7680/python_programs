class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.cart = Cart()

    def view_products(self, products):
        for product in products:
            print(product.display_details())

    def add_to_cart(self, product):
        self.cart.add_product(product)

    def remove_from_cart(self, product):
        self.cart.remove_product(product)

    def checkout(self):
        self.cart.checkout()


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def checkout(self):
        total_price = sum(product.price for product in self.products)
        print(f"Total price: ${total_price}")
        print("Checkout completed!")


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display_details(self):
        return f"{self.name} - ${self.price}"


class FlipkartWebsite:
    def __init__(self):
        self.users = []
        self.products = []

    def create_user(self, username, email):
        user = User(username, email)
        self.users.append(user)
        return user

    def create_product(self, name, price, category):
        product = Product(name, price, category)
        self.products.append(product)
        return product

flipkart = FlipkartWebsite()

user1 = flipkart.create_user("user123", "user123@example.com")
user2 = flipkart.create_user("user456", "user456@example.com")

product1 = flipkart.create_product("Laptop", 800, "Electronics")
product2 = flipkart.create_product("T-shirt", 20, "Clothing")

user1.view_products(flipkart.products)
user1.add_to_cart(product1)
user1.add_to_cart(product2)
user1.checkout()

user2.view_products(flipkart.products)
user2.add_to_cart(product2)
user2.remove_from_cart(product2)
user2.checkout()
