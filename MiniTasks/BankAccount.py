
def validateAmount(amount):
    if amount <= 0:
        print("Invalid amount!")
        return False
    return True

def continueTransaction():
    while True:
        choice = input("Continue transacting? (y/n): ")
        choice = choice.lower()

        if choice == "y":
            return True
        elif choice ==  "n":
            return False
        else:
            print("Invalid input!")


class BankAccount:
    def __init__(self, name, balance_amount):
        self.name = name
        self.balance_amount = balance_amount

    def withdraw(self, withdraw_amount):
        if not validateAmount(withdraw_amount):
            return
        
        if self.balance_amount >= withdraw_amount:
            self.balance_amount -= withdraw_amount
            return f"You have successfully withdrew {withdraw_amount} from your account!\nUpdated Balance: {self.balance_amount}\n"
        else:
            return "Insufficient balance!"

    def deposit(self, deposit_amount):
        if not validateAmount(deposit_amount):
            return
        
        self.balance_amount += deposit_amount
        return f"You have successfully deposited {deposit_amount} to your account!\nUpdated Balance: {self.balance_amount}\n"
        
    def viewBalance(self):
        return f"Balance: {self.balance_amount}\n"

if __name__ == "__main__":
    customer = BankAccount("Raul", 0)

    print("Welcome to Bank of Fletchy's!")

    while True:
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Exit")
        transaction = int(input("Select transaction: "))

        match transaction:
            case 1:
                withdraw_amount = float(input("Enter amount to withdraw: "))
                print(customer.withdraw(withdraw_amount))
            case 2:
                deposit_amount = float(input("Enter amount to deposit: "))
                print(customer.deposit(deposit_amount))
            case 3:
                print(customer.viewBalance())
            case 4:
                print("Thank you and come again!")
                break
            case _:
                print("Invalid input!")
                continue
            
        if continueTransaction():
            print("")
            continue
        else:
            print("Thank you and come again!")
            break

    


        


