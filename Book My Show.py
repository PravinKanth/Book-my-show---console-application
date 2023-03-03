from colorama import Fore
admin_confidentials={"PRAVIN":"PRAVIN123","NIGUN":"NIGUN123","HARI":"HARI123"}
user_confidentials={"MADHAN":"MADHAN123","NAGULAN":"NAGULAN123","SURIYA":"SURIYA123","SRI":"SRI123"}
shows=[]
bookings=[]
admin_movies=set()
def admin_storage():
    b = input(Fore.BLUE+"Enter your username:")
    if b not in admin_confidentials:
        print(Fore.RED+"Username not found.!")
        admin_storage()
    else:
        c = input(Fore.BLUE+"Enter your password:")
        print("\n")
        if (admin_confidentials[b] == c):
            admin(b)
        else:
            print(Fore.RED+"Invalid password\n")
            admin_storage()

def admin(username):
    print(Fore.LIGHTBLUE_EX + "Welcome Admin!\n")
    print(Fore.LIGHTWHITE_EX + "1. Add Movie\n2. Remove Movie\n3. Logout\n")
    admin_option = int(input(Fore.BLUE + "Enter your option: "))
    print("\n")
    if admin_option == 1:
        name = input(Fore.BLUE + "Enter movie name: ")
        timings = input(Fore.BLUE + "Enter show timings separated by commas: ").split(",")
        theater = input(Fore.BLUE + "Enter theater name: ")
        location=input(Fore.BLUE + "Enter the location: ")
        col_seats = int(input(Fore.BLUE+ "Enter the column seats: "))
        row_seats = int(input(Fore.BLUE + "Enter the row seats: "))
        print("\n")
        time_seat={}
        for i in timings:
            time_seat[i]=[0]*(col_seats*row_seats)
        shows.append([username,name,timings,theater,location,col_seats,row_seats,time_seat])

    elif admin_option==2:
        for i in shows:
            if i[0]==username:
                admin_movies.add(i[1])
        for j in admin_movies:
            print(Fore.LIGHTWHITE_EX+str(j)+"\n")
        movie_name=input(Fore.BLUE + "Enter the movie you wanna remove: ")
        for i in shows:
            if movie_name and username in i:
                try:
                    shows.remove(i)
                except:
                    print(Fore.LIGHTRED_EX+"INVALID")
                    admin(username)


    elif admin_option==3:
        main()
    else:
        print(Fore.LIGHTRED_EX+"INVALID")
        admin(username)


def user_storage():
    b = input(Fore.BLUE + "Enter your username:")
    if b not in user_confidentials:
        print(Fore.RED + "Username not found.!")
        user_storage()
    else:
        c = input(Fore.BLUE + "Enter your password:")
        print("\n")
        if (user_confidentials[b] == c):
            user(b)
        else:
            print(Fore.RED + "Invalid password\n")
            user_storage()

def user(username):
    print(Fore.LIGHTRED_EX + "Welcome User!\n")
    print(Fore.LIGHTWHITE_EX + "1.Book Tickets\n2.Cancel tickets\n3.Log out\n")
    q=int(input(Fore.BLUE+"Enter the option: "))
    print("\n")
    if q==1:
        movie_list=set()
        for i in shows:
            movie_list.add(i[1])
        for movie in movie_list:
            print(movie+"\n")
        choice=input(Fore.BLUE+"Enter the movie: ")
        print("\n")
        if choice not in movie_list:
            print(Fore.MAGENTA+"Movie not available.!\n")
            user(username)
        else:
            total_list=[]
            for i in shows:
                if i[1]==choice:
                    total_list.append(i)
            for j,dum in enumerate(total_list,1):
                print(str(j)+".",str(dum[3])+"-"+str(dum[4]),"\n")
            opt=int(input(Fore.BLUE+"Enter the option(IF YOU DON'T FIND YOUR DESIRED THEATER, Type 0 ): "))
            print("\n")
            if opt==0:
                print(Fore.MAGENTA+"Sorry to see you go.!\n")
                main()
            elif opt>len(total_list) or opt<0:
                print(Fore.RED+"INVALID\n")
                user(username)
            else:
                for i in total_list[opt-1][2]:
                    print(Fore.LIGHTWHITE_EX+i+"\n")
                tim=input(Fore.BLUE+"Enter the timing: ")
                print("\n")
                if sum(total_list[opt-1][7][tim])==total_list[opt-1][5]*total_list[opt-1][6]:
                    print(Fore.MAGENTA+"Sorry, Seats are booked\n")
                else:
                    s=total_list[opt-1][7][tim]
                    no=0
                    count=1
                    for i in range(total_list[opt-1][5]):
                        for k in range(total_list[opt-1][6]):
                            print(str(s[no]),end="  ")
                            no += 1
                        print("\n")
                        for j in range(total_list[opt-1][6]):
                            print(str(count),end="  ")
                            count+=1
                        print("\n")
                    no_tickets=list(map(int,input(Fore.BLUE+"Enter the seats separated by comma: ").split(",")))
                    print("\n")
                    flag=True
                    for i in no_tickets:
                        if total_list[opt-1][7][tim][i-1]!=0:
                            flag=False
                    if flag:
                        for i in no_tickets:
                            total_list[opt - 1][7][tim][i - 1]=1
                        for ind,j in enumerate(shows,0):
                            if j[1]==choice and j[3]==total_list[opt - 1][3] and j[4]==total_list[opt - 1][4] :

                                shows[ind][7][tim]=total_list[opt - 1][7][tim]
                        print(Fore.MAGENTA+"Whoa.! Booked the tickets\n")
                        bookings.append([username,choice,total_list[opt - 1][3],total_list[opt - 1][4],tim,no_tickets])
                    else:
                        print(Fore.MAGENTA+"Sorry, those seats are already booked.!\n")
        user(username)
    elif q==2:
        your_movies= set()
        for y in bookings:
            if y[0]==username:
                your_movies.add(y[1])
        for c,mo in enumerate(your_movies,0):
            print(mo)
        cancel_movie=input(Fore.BLUE+"Enter the movie to cancel: \n")


        for ind,i in enumerate(shows):
            for j in bookings:
                if j[0]==username and j[1]==cancel_movie and j[2] in i and j[3] in i :
                    for k in j[5]:
                        shows[ind][7][j[4]][k-1]=0
        print(Fore.MAGENTA + "Successfully cancelled.!\n")
        user(username)

    elif q==3:
        print(Fore.MAGENTA+"Thanks for using this app.!\nEnjoy the cinemas 😉\n")
    else:
        print(Fore.LIGHTRED_EX+"INVALID\n")
        user(username)



def main():
    while True:
        print(Fore.LIGHTRED_EX+"\n---------------BOOK MY SHOW---------------\n")
        print(Fore.LIGHTWHITE_EX+"1.Admin\n2.User\n")
        option=int(input(Fore.BLUE+"Enter who you are: "))
        print("\n")
        if option==1:
            admin_storage()
        elif option==2:
            user_storage()
        else:
            print(Fore.LIGHTRED_EX+"INVALID OPTION\n")
            main()

if __name__=="__main__":
    main()

