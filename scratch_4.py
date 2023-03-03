from colorama import Fore
expenses = {}
payments = {}

def add_expense():
    description = input(Fore.BLUE+"Enter a description of the expense: ")
    amount = float(input(Fore.BLUE+"Enter the total amount of the expense: "))
    payer = input(Fore.BLUE+"Enter the name of the payer: ")
    num_friends = int(input(Fore.BLUE+"Enter the number of friends who shared the expense: "))
    split_type = input(Fore.BLUE+"Enter the split type (equal or custom): ")
    print("\n")


    if split_type == 'equal':
        split_amount = amount / (num_friends + 1)
        for i in range(num_friends):
            friend = input(Fore.BLUE+"Enter the name of a friend who shared the expense: ")
            if friend != payer:
                if friend in expenses:
                    expenses[friend].append((description, split_amount))
                else:
                    expenses[friend] = [(description, split_amount)]
    elif split_type == 'custom':
        for i in range(num_friends):
            friend = input(Fore.BLUE+"Enter the name of a friend who shared the expense: ")
            if friend != payer:
                split_amount = float(input(Fore.BLUE+"Enter " + friend + "'s split amount: "))
                if friend in expenses:
                    expenses[friend].append((description, split_amount))
                else:
                    expenses[friend] = [(description, split_amount)]
    else:
        print(Fore.RED+"Invalid split type.")
        add_expense()

def record_payment():
    payer = input(Fore.BLUE+"Enter the name of the payer: ")
    payee = input(Fore.BLUE+"Enter the name of the payee: ")
    amount = float(input(Fore.BLUE+"Enter the amount of the payment: "))

    if payer in payments:
        payments[payer] -= amount
    else:
        payments[payer] = -amount
    if payee in payments:
        payments[payee] += amount
    else:
        payments[payee] = amount

def display_balances():
    for friend, expenses_list in expenses.items():
        total_expenses = sum([expense[1] for expense in expenses_list])
        total_payments = payments.get(friend, 0)
        balance = total_payments - total_expenses
        if balance > 0:
            print(Fore.MAGENTA+friend + " is owed ₹" + str(balance))
        elif balance < 0:
            print(Fore.MAGENTA+friend + " owes ₹" + str(-balance))
        else:
            print(Fore.MAGENTA+friend + " is settled up.")

print(Fore.LIGHTRED_EX+"Splitwise Console App")
def get_input():
    while True:
        print(Fore.LIGHTWHITE_EX + "\n1. Add a new expense")
        print(Fore.LIGHTWHITE_EX + "2. Record a payment")
        print(Fore.LIGHTWHITE_EX + "3. Display balances")
        print(Fore.LIGHTWHITE_EX + "4. Quit\n")
        choice = input(Fore.BLUE+"Enter your choice: ")
        print("\n")
        if choice == '1':
            try:
                add_expense()
            except:
                print(Fore.LIGHTRED_EX+"Invalid\n")
        elif choice == '2':
            record_payment()
        elif choice == '3':
            display_balances()
        elif choice == '4':
            break
        else:
            print(Fore.RED+"Invalid choice. Try again.\n")

if __name__ == '__main__':
    get_input()
