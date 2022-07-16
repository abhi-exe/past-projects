import random
import time
import sqlalchemy as sql
from sqlalchemy.orm import scoped_session, sessionmaker


engine=sql.create_engine('postgresql://postgres:veronica31@localhost:5432/bank')
db = scoped_session(sessionmaker(bind=engine))


print("Hi there! \n Welcome to THE MASTERMIND \n \t -Command Line Exclusive!")
print("Default Profile (Lunar) Loaded....")


instr=input("Do you want to read the instructions first? (y/n): ")
if instr=="y":
    print("The rules of mastermind are simple to learn,... but is playing the game? \n  Ok,so let's discuss the rules.. \n 1. The computer will write a general number based on your difficulty ratings. \n 2. You just have to guess the number by seeing the hints \n 3. Whenever you give computer a number, the computer will only tell you how many of them numbers are in the real number and placed correctly. \n 4. The number of \u2585 represents the number of digits placed orderly, while \u25a1 represents the number of digits already present in the number but not placed correctly. \n So simple or struggling to understand? \n Try the game and find it yourself!")
else:
    pass


print("Choose a Difficulty Rating: ")
print("1. Have 4 numbers with each digit lying between 1 to 6, both included, with 10 tries")
print("2. Have 4 numbers with each digit lying between 0 to 9, both included, with 10 tries")
print("3. Have 4 numbers with each digit lying between 1 to 6, both included, with 6 tries")
print("4. Have 4 numbers with each digit lying between 0 to 9, both included, with 6 tries")

def menu():
    choice=input("So, (1/2/3/4): ")
    if choice=="1":
        key="a"                                                  #find a way to continuosly repeat the menu and send the value of ll,ul and looplen
        ll=1
        ul=6
        looplen=10
    elif choice=="2":
        key="b"
        ll=0
        ul=9
        looplen=10
    elif choice=="3":
        key="c"
        ll=1
        ul=6
        looplen=6
    elif choice=="4":
        key="d"
        ll=0
        ul=9
        looplen=6
    else:
        menu()
    return key

key=menu()
if key=="a":
    ll=1
    ul=6
    looplen=10
elif key=="b":
    ll=0
    ul=9
    looplen=10
elif key=="c":
    ll=1
    ul=6
    looplen=6
elif key=="d":
    ll=0
    ul=9
    looplen=6
else:
    pass



start=time.time()


def game():
    p=random.randint(ll,ul)
    q=random.randint(ll,ul)
    r=random.randint(ll,ul)
    s=random.randint(ll,ul)
    lis=[p,q,r,s]
    for a in range(looplen):
        print("This is your try number: ",a+1)
        b=input(": ")
        try:
            convert=int(b)
        except:
            print("Enter a valid number")
            continue
        if len(b)!=len(lis):
            print("The number of digits are ",len(lis))
            continue
        ls=[]
        for obj in b:
            ls.append(int(obj))
        limitcheck=0
        for indnum in ls:
            if indnum<ll or indnum>ul:
                limitcheck=limitcheck+1
            else:
                pass
        if limitcheck!=0:
            print("Consider the digit limits again! ")
            continue
        else:
            pass
        listy=[p,q,r,s]
        count=0
        k=0
        countw=0
        for i in lis:
            if int(b[k])==i:
                count=count+1
                listy.remove(i)
                ls.remove(i)
            else:
                pass
            k=k+1
        if count==4:
            print("Congratulations! You got it...")
            endtime=time.time()
            timetake=endtime-start
            timetaken=round(timetake,2)
            print("You elapsed about ",int(timetaken//60)," minutes", int(timetaken%60)," seconds")
            break
        else:
            print("\u2585 "*count)
        for m in ls:
            for n in listy:
                if m==n:
                    countw=countw+1
                    listy.remove(n)
                    break
                else:
                    pass
        print("\u25a1 "*countw)
    else:
        print("Oh! Better luck next time!")
        num=""
        for hhin in lis:
            num=num+str(hhin)
        print("The number was ",num)
game()
#ADD 2 fEAtures
# stopping program to end and asking for if player to play once again
# accept only 4 numbers
# add more difficultiy levels
# add the table from class 11 th project to make it visually more appearing
# allow time keeping
#telling a layer's score by making an algorithm of seeing difficulty rating. time used, no. of tries and map the score to sql
# make a gui
