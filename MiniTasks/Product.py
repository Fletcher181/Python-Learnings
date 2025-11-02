class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def addProduct(self, product_list):
        product_list.append(self)

    def removeProduct(self, product_list):
        product_list.remove(self)

    def updateProduct(self, product_list):
        product_list.remove(self)


if __name__ == "__main__":

    product_list = []
