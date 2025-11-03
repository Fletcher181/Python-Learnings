def viewProducts(product_list):
    for product in product_list:
        print(f"{product.id}. {product.name}(P{product.price})   Qty: {product.quantity}")
    

class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def addProduct(self, product_list):
        product_list.append(self)
        print("You have successfully added the product!")


    def removeProduct(self, product_list, target_id):
        for product in product_list:
            if product.id == target_id:
                product_list.remove(product)
                print("You have successfully removed the product!")

    def updateProduct(self, product_list, target_id, new_name, new_price, new_quantity):
        for product in product_list:
            if product.id == target_id:
                product.name = new_name
                product.price = new_price
                product.quantity = new_quantity
        print("You have succussfully updated the product!")
    



if __name__ == "__main__":

    product_id = 0
    product_list = []
    
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

                p1 = Product(product_id, product_name, product_price, product_quantity)
                p1.addProduct(product_list)
            case 2:
                print("\nProduct List")
                viewProducts(product_list)
                target_id = int(input("Enter id to delete: "))
                p1.removeProduct(product_list, target_id)
            case 3:
                print("\nProduct List")
                viewProducts(product_list)
                target_id = int(input("Enter id to update: "))
                product_name = input("Enter product name: ")
                product_price = float(input("Enter product price: "))
                product_quantity = int(input("Enter product quantity: "))
                p1.updateProduct(product_list, target_id, product_name, product_price, product_quantity)
            case 4:
                print("\nProduct List")
                viewProducts(product_list)
            case 5:
                print("\nThank you for using!")
                break
            case _:
                print("\nInvalid option!")
                continue




