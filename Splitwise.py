from colorama import Fore
import math

def add_expense(expenses, payer, payees, amount):
    split_amount = round(amount/len(payees), 2)
    for payee in payees:
        if payee not in expenses:
            expenses[payee] = 0
        expenses[payee] += split_amount
    if payer not in expenses:
        expenses[payer] = 0
    expenses[payer] -= amount
    return expenses

# def delete_expense(expenses, payer, payees, amount):
#     split_amount = round(amount/len(payees), 2)
#     for payee in payees:
#         expenses[payee] -= split_amount
#     expenses[payer] += amount
#     return expenses

def view_balances(expenses):
    for person, balance in expenses.items():
        if balance > 0:
            print(Fore.MAGENTA+person, "owes", abs(balance))
        elif balance < 0:
            print(Fore.MAGENTA+person, "is owed", abs(balance))
        else:
            print(Fore.MAGENTA+person, "is settled")

def settle_expense(expenses, payer, payee, amount):
    # split_amount = round(amount/len(payees), 2)
    # for payee in payees:
    #     expenses[payee] -= split_amount
    # expenses[payer] += amount
    # # del expenses[payer]
    # return expenses

    expenses[payer] -= amount
    expenses[payee] += amount
    # del expenses[payer]
    return expenses

def view_history(history):
    for i, expense in enumerate(history):
        print(Fore.MAGENTA+f"Expense {i+1}: {expense['amount']} paid by {expense['payer']} for {expense['description']} split among {expense['payees']}")



def main():
    expenses = {}
    history = []
    while True:
        print(Fore.LIGHTRED_EX+"\nSplitwise Menu:")
        print(Fore.LIGHTWHITE_EX+"1. Add expense")
        # print(Fore.LIGHTWHITE_EX+"2. Delete expense")
        print(Fore.LIGHTWHITE_EX+"2. View balances")
        print(Fore.LIGHTWHITE_EX+"3. Settle up")
        print(Fore.LIGHTWHITE_EX+"4. View expense history")
        print(Fore.LIGHTWHITE_EX+"5. Quit")
        choice = int(input(Fore.BLUE+"Enter your choice: "))
        print("\n")

        if choice == 1:
            payer = input(Fore.BLUE+"Enter the name of the person who paid: ")
            payees = input(Fore.BLUE+"Enter the names of the people who should split the cost (separated by commas): ").split(",")
            amount = float(input(Fore.BLUE+"Enter the expense amount: "))
            description = input(Fore.BLUE+"Enter a description for the expense: ")
            expenses = add_expense(expenses, payer, payees, amount)
            history.append({"payer":payer, "payees":payees, "amount":amount, "description":description})

        # elif choice == 2:
        #     payer = input(Fore.BLUE+"Enter the name of the person who paid: ")
        #     payees = input(Fore.BLUE+"Enter the names of the people who split the cost (separated by commas): ").split(",")
        #     amount = float(input(Fore.BLUE+"Enter the expense amount: "))
        #     expenses=delete_expense(expenses, payer, payees, amount)

        elif choice == 2:
            view_balances(expenses)

        elif choice == 3:
            '''payer = input(Fore.BLUE+"Enter the name of the person who paid: ")
            payees = input(Fore.BLUE+"Enter the names of the people who split the cost (separated by commas): ").split(",")
            amount = float(input(Fore.BLUE+"Enter the expense amount: "))
            expenses = settle_expense(expenses, payer, payees, amount)'''
            payer = input(Fore.BLUE+"Enter the name of the payer ")
            payee = input(Fore.BLUE+"Enter the name of the payee: ")
            amount = float(input(Fore.BLUE + "Enter the amount: "))
            expenses = settle_expense(expenses, payer, payee, amount)


        elif choice == 4:
            view_history(history)

        elif choice == 5:
            break

        else:
            print(Fore.LIGHTRED_EX+"Invalid choice. Please try again.")

main()
