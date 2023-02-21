import math
from colorama import Fore
import sys
flag=True
denominations={"100":0,"200":0,"500":0,"2000":0}
admin_confidentials={"pravin":"pravin123","nigun":"nigun123"}
user_confidentials={3233:2000,3237:1500,3234:6000,3235:600,3236:7000}
mini_statement={3233:[],3234:[],3235:[],3236:[],3237:[]}
total_atm_balance=0

# Admin
def admin_storage():
    b = input(Fore.BLUE+"Enter your username:")
    if b not in admin_confidentials:
        print(Fore.RED+"Username not found.!")
        admin_storage()
    else:
        c = input(Fore.BLUE+"Enter your password:")
        if (admin_confidentials[b] == c):
            admin()
        else:
            print(Fore.RED+"Invalid password\n")
            admin_storage()

def admin():
    print(Fore.LIGHTWHITE_EX+"\n1.Load Amount\n2.ATM Balance\n3.Log out\n")
    option=int(input(Fore.BLUE+"Enter the option:"))
    print("\n")
    if option==1:
        load_amount()
        admin()
    elif option==2:
        atm_balance()
        admin()
    elif option==3:
        pass

    else:
        print(Fore.RED+"Invalid")
        admin()

def load_amount():
    denominations["100"]+=int(input(Fore.BLUE+"Total number of 100's:"))
    denominations["200"] += int(input(Fore.BLUE+"Total number of 200's:"))
    denominations["500"] += int(input(Fore.BLUE+"Total number of 500's:"))
    denominations["2000"] += int(input(Fore.BLUE+"Total number of 2000's:"))


def atm_balance():
    max=0
    for i in denominations:
        max+=denominations[i]*int(i)
    print(Fore.MAGENTA+f"ATM Balance:{max}")


# User
def user_storage():
    b = int(input(Fore.BLUE+"Enter your pin:"))
    if b in user_confidentials:
        user(b)
    else:
        print(Fore.RED+"Invalid PIN\n")
        user_storage()

def user(b):
    print(Fore.LIGHTWHITE_EX+"\n1.Withdrawal\n2.Balance\n3.PIN Change\n4.Mini Statement\n5.Deposit\n6.Exit\n")
    option=int(input(Fore.BLUE+"Enter the option:"))
    print("\n")
    if option==1:
        withdrawal(b)
        user(b)
    elif option==2:
        user_balance(b)
        user(b)
    elif option==3:
        pin=int(input(Fore.BLUE+"Enter your new PIN:"))
        user_confidentials[pin]=user_confidentials[b]
        del user_confidentials[b]
        mini_statement[pin]=mini_statement[b]
        del mini_statement[b]
        user(pin)
    elif option==4:
        statement(b)
        user(b)
    elif option==5:
        deposit(b)
        user(b)
    elif option==6:
        func()
    else:
        print(Fore.RED+"Invalid")
        user(b)

def withdrawal(b):
    withdrawal_amount=int(input(Fore.BLUE+"Enter the amount you'd like to withdraw:"))
    if withdrawal_amount<=0:
        print(Fore.RED+"Insufficient amount or denominations not available")
        user(b)
    rem = withdrawal_amount

    den_2000 = min(denominations["2000"], math.floor(rem / 2000))
    value_den_2000 = den_2000 * 2000
    rem -= value_den_2000

    den_500 = min(denominations["500"], math.floor(rem / 500))
    value_den_500 = den_500 * 500
    rem -= value_den_500

    den_200 = min(denominations["200"], math.floor(rem / 200))
    value_den_200 = den_200 * 200
    rem -= value_den_200

    den_100 = min(denominations["100"], math.floor(rem / 100))
    value_den_100 = den_100 * 100
    rem -= value_den_100
    if rem == 0 and withdrawal_amount <= user_confidentials[b]:
        denominations["2000"] -= den_2000
        denominations["500"] -= den_500
        denominations["200"] -= den_200
        denominations["100"] -= den_100
        user_confidentials[b] -= withdrawal_amount
        print(Fore.MAGENTA+"Collect your cash.!")
        mini_statement[b].append("-"+str(withdrawal_amount)+"\t\t\t\t\t\t"+str(user_confidentials[b]))
    else:
        print(Fore.RED+"Insufficient amount or denominations not available")

    # print(Fore.LIGHTWHITE_EX+str(denominations))
    user(b)

def statement(b):
    print(Fore.MAGENTA+"Mini Statement:\n")
    print(Fore.MAGENTA+"Credit/Debit" + "\t\t\t\t" + "Balance")
    for i in mini_statement[b]:
        print(Fore.LIGHTWHITE_EX+i)
    user(b)

def user_balance(bal):
    print(Fore.MAGENTA+f"Your Balance:{user_confidentials[bal]}")

def deposit(b):
    tot_100=int(input(Fore.BLUE+"Total number of 100's:"))
    denominations["100"]+=tot_100
    tot_200=int(input(Fore.BLUE+"Total number of 200's:"))
    denominations["200"]+=tot_200
    tot_500=int(input(Fore.BLUE+"Total number of 500's:"))
    denominations["500"]+=tot_500
    tot_2000=int(input(Fore.BLUE+"Total number of 2000's:"))
    denominations["2000"]+=tot_2000
    amount=(tot_100*100)+(tot_200*200)+(tot_500*500)+(tot_2000*2000)
    user_confidentials[b]+=amount
    mini_statement[b].append("+" + str(amount) + "\t\t\t\t\t\t" + str(user_confidentials[b]))
    user(b)

def func():
    while flag:
        print(Fore.LIGHTWHITE_EX+"\n1.Admin\n2.User\n")
        a=int(input(Fore.BLUE+"Enter the option:"))
        print("\n")
        if a==1:
            admin_storage()
        elif a==2:
            user_storage()
        else:
            print(Fore.RED+"Invalid..! Enter again:")
func()
