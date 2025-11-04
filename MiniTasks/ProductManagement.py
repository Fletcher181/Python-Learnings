class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

class ProductManager:
    def __init__(self):
        self.product_list = []

    def addProduct(self, product):
        self.product_list.append(product)
        print("You have successfully added the product!")

    def removeProduct(self, target_id):
        for product in self.product_list:
            if product.id == target_id:
                self.product_list.remove(product)
        print("You have successfully removed the product!")
    
    def updateProduct(self, target_id, new_name, new_price, new_quantity):
        for product in self.product_list:
            if product.id == target_id:
                product.name = new_name
                product.price = new_price
                product.quantity = new_quantity
        print("You have successfully updated the product!")

    def viewProducts(self):
        for product in self.product_list:
            print(f"{product.id}. {product.name} (P{product.price}) Qty: {product.quantity}")

if __name__ == "__main__":
    product_id = 0
    manager = ProductManager()
    print("Fletchy's Product Management")

    while True:
        print("\n1. Add Product")
        print("2. Remove Product")
        print("3. Update Product")
        print("4. View Products")
        print("5. Exit")
        option = int(input("Select option: "))

        match option:
            case 1:
                product_id += 1
                product_name = input("\nEnter product name: ")
                product_price = float(input("Enter product price: "))
                product_quantity = int(input("Enter product quantity: "))

                new_product = Product(product_id, product_name, product_price, product_quantity)
                manager.addProduct(new_product)
            case 2:
                print("\nProduct List")
                manager.viewProducts()
                target_id = int(input("Enter id to delete: "))
                manager.removeProduct(target_id)
            case 3:
                print("\nProduct List")
                manager.viewProducts()
                target_id = int(input("Enter id to update: "))
                new_name = input("Enter product name: ")
                new_price = float(input("Enter product price: "))
                new_quantity = int(input("Enter product quantity: "))
                manager.updateProduct(target_id, new_name, new_price, new_quantity)
            case 4:
                print("\nProduct List")
                manager.viewProducts()
            case 5:
                print("\nThank you for using!")
                break
            case _:
                print("\nInvalid option!")
                continue

