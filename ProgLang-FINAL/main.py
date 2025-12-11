import tkinter as tk

menu = {
    "Ramen": {
        "Shoyu": 349,
        "Spicy Miso": 369,
        "Tonkotsu": 399
    },
    "Donburi": {
        "Beef": 180,
        "Chicken": 170,
        "Vegetable": 150
    },
    "Others": {
        "Beef": 180,
        "Chicken": 170,
        "Vegetable": 150
    }
}

cart = {}


root = tk.Tk()

root.geometry("1080x1920")

landingPage = tk.Frame(root)
orderTypePage = tk.Frame(root)
orderPage = tk.Frame(root)


landingPage.pack(fill="both", expand=True)


def go_to_order_type():
    landingPage.pack_forget()
    orderTypePage.pack(fill="both", expand=True)

    btnDineIn = tk.Button(orderTypePage, text="DINE-IN", font=('Baloo Tammudu', 45), command=go_to_order)
    btnTakeOut = tk.Button(orderTypePage, text="TAKE OUT", font=('Baloo Tammudu', 45), command=go_to_order)

    btnDineIn.pack()
    btnTakeOut.pack()

btnStart = tk.Button(landingPage, text="TAP TO START", font=('Baloo Tammudu', 80), command=go_to_order_type)
btnStart.pack()

def add_to_cart(item, price):
    if item in cart:
        cart[item] += 1
    else:
        cart[item] = {
            "price": price,
            "quantity": 1
        }

def show_items(section):
    for widget in orderPage.winfo_children():
        widget.destroy()

    for item, price in menu[section].items():
        btn = tk.Button(orderPage, text=f"{item}\n{price}", font=('Baloo Tammudu', 45), command=lambda i=item, p=price: add_to_cart(i, p))
        btn.pack()
        


def go_to_order():
    orderTypePage.pack_forget()
    orderPage.pack(fill="both", expand=True)

    btnRamen = tk.Button(orderPage, text="RAMEN", font=('Baloo Tammudu', 45), command=lambda: show_items("Ramen"))
    btnDonburi = tk.Button(orderPage, text="DONBURI", font=('Baloo Tammudu', 45), command=lambda: show_items("Donburi"))
    btnOthers = tk.Button(orderPage, text="OTHERS", font=('Baloo Tammudu', 45), command=lambda: show_items("Others"))

    btnRamen.pack()
    btnDonburi.pack()
    btnOthers.pack()

    


root.mainloop()