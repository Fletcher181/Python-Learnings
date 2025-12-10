import tkinter as tk

root = tk.Tk()

root.geometry("1080x1920")

landingPage = tk.Frame(root)
orderPage = tk.Frame(root)

orderTypePage = tk.Frame(root)
orderRamenPage = tk.Frame(root)
orderDonburiPage = tk.Frame(root)
orderOthersPage = tk.Frame(root)

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

def show_ramen_items():
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

def go_to_order():
    orderTypePage.pack_forget()
    orderPage.pack(fill="both", expand=True)

    sections = ['Ramen', 'Donburi', 'Others']

    btnRamen = tk.Button(orderPage, text="RAMEN", font=('Baloo Tammudu', 45), command=show_ramen_items)
    btnDonburi = tk.Button(orderPage, text="DONBURI", font=('Baloo Tammudu', 45))
    btnOthers = tk.Button(orderPage, text="OTHERS", font=('Baloo Tammudu', 45))

    btnRamen.pack()
    btnDonburi.pack()
    btnOthers.pack()

    


root.mainloop()