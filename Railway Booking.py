from colorama import Fore
admin_confidentials={"pravin":"pravin123","nigun":"nigun123"}
train_details=[]
capacity={}
def admin_storage():
    b = input(Fore.BLUE+"Enter your username:")
    if b not in admin_confidentials:
        print(Fore.RED+"Username not found.!")
        admin_storage()
    else:
        c = input(Fore.BLUE+"Enter your password:")
        print("\n")
        if (admin_confidentials[b] == c):
            admin()
        else:
            print(Fore.RED+"Invalid password\n")
            admin_storage()
def admin():
    print(Fore.LIGHTWHITE_EX + "1.Train details\n2.Log out\n")
    option = int(input(Fore.BLUE + "Enter the option:"))
    print("\n")
    if option==1:
        train_number=int(input(Fore.BLUE+"Train number:"))
        train_route=input(Fore.BLUE+"Train Route:")
        train_capacity=int(input(Fore.BLUE+"Train Capacity:"))
        arrival_date=input(Fore.BLUE+"Arrival Date:")
        arrival_time=input(Fore.BLUE+"Arrival time:")
        print("\n")
        train_details.append(str(train_number)+"\t"+str(train_route)+"\t"+str(arrival_date)+"\t"+str(arrival_time))
        capacity[train_number]=train_capacity

    elif option==2:
        main()
    else:
        print(Fore.RED+"Invalid")
        admin()



def user_storage():
    print(Fore.LIGHTWHITE_EX + "Train Details\n")
    # print(Fore.RED+"TRAIN NUMBER\tTRAIN ROUTE\tARRIVAL DATE\tARRIVAL TIME\n")
    for i in range(len(train_details)):
        print(train_details[i]+"\n")
    a=int(input(Fore.BLUE+"If you don't find your desired train, kindly press 0 or Enter the train number you'd like to go with:"))
    if a==0:
        main()
    elif a in capacity:
        seats=int(input(Fore.BLUE+"Enter the total number of seats:"))
        print("\n")
        if capacity[a]-seats>=0:
            print(Fore.MAGENTA+"Whoah.! Successfully Booked.!\n")
            capacity[a]-=seats
        else:
            print(Fore.MAGENTA+"Seats not available.!\n")
        main()
    else:
        print(Fore.RED+"Invalid\n")
        user_storage()


def main():
    while True:
        print(Fore.LIGHTWHITE_EX+"1.Admin\n2.User\n")
        a=int(input(Fore.BLUE+"Enter the option:"))
        print("\n")
        if a==1:
            admin_storage()
        elif a==2:
            user_storage()
        else:
            print(Fore.RED+"Invalid option\n")
            main()
main()
