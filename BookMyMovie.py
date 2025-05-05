print("Hi, welcome to movie ticket booking:")
def city():
    print("where you want to watch movie?:\n 1,Kolkata \n 2,Barasat \n 3,Kakdwip \n 4,Dumdum")
    c=int(input())
    if c==1:
        print("you are selected Kolkata")
    elif c==2:
        print("you are selected Barasat")
    elif c==3:
        print("you are selected Kakdwip")
    elif c==4:
        print("you are selected Dumdum")
    else:
        print("choice a valid number") 
        

def t_movie():
    print("please select the movie which you want to see :\n 1,Dilwale Dulhania Le Jayenge \n 2,Om Shanti Om \n 3,Dilwale \n 4,Devdas")
    t=int(input())
    if t==1:
        print("you are selected Dilwale Dulhania Le Jayenge")
    elif t==2:
        print("you are selected Om Shanti Om")
    elif t==3:
        print("you are selected Dilwale")
    elif t==4:
        print("you are selected Devdas")
    else:
        print("choice a valid number") 
        

def theater():
    print("please select the theater:\n 1,Inox \n 2,PVR \n 3,Ashoka cinema Hall \n 4,Rajlakhmi Cinema Hall \n 5,Back")
    th=int(input())
    if th==1:
        print("you are selected Inox")
    elif th==2:
        print("you are selected PVR")
    elif th==3:
        print("you are selected Ashoka cinema Hall")
    elif th==4:
        print("you are selected ajlakhmi Cinema Hall")
    elif th==5:
        t_movie()
    else:
        print("choice a valid number") 
       

def screen():
    print("choose your screen:\n 1,Screen1 \n 2,Screen2 \n 3,Screen3 \n 4,back")
    s=int(input())
    if s==1:
        print("you are selected Screen1")
    elif s==2:
        print("you are selected Screen2")
    elif s==3:
        print("you are selected Screen3")
    elif s==4:
        theater()
    else:
        print("choice a valid number") 
        

def timing():
    print("slot1=1:10.00-1.00,2:1.10-4.10,3:4.20-7.20,4:7.30-10.30,\n slot2=1:10.15-1.15,2:1.25-4.25,3:4.35-7.35,4:7.45-10.45,\n slot3=1:10.30-1.30,2:1.40-4.40,3:4.50-7.50,4:8.00-11.00")
    slot1={"1":"10.00-1.00","2":"1.10-4.10","3":"4.20-7.20","4":"7.30-10.30"}
    slot2={"1":"10.15-1.15","2":"1.25-4.25","3":"4.35-7.35","4":"7.45-10.45"}
    slot3={"1":"10.30-1.30","2":"1.40-4.40","3":"4.50-7.50","4":"8.00-11.00"}
    sl=int(input())
    if sl==1:
        print("please select the timing 1. slot")
        time=input()
        print("selected time is",slot1[time])
    elif sl==2:
        print("please select the timing 2. slot")
        time=input()
        print("selected time is",slot2[time])
    elif sl==3:
        print("please select the timing 3. slot")
        time=input()
        print("selected time is",slot3[time])
    else:
        print("invalied number")
             
def member():
    mem=print(int(input("number of ticket you want:")))
    print("booking confirm")
city()
t_movie()
theater()
screen()
timing()
member()
