TVK=0
DMK=0
AIADMK=0
BJP=0
INC=0
PMK=0
NOTA=0
def check_TVK():
    global TVK
    print("total vote of TVK=",TVK)
def check_DMK():
    global DMK
    print("total vote of DMK=",DMK)
def check_AIADMK():
    global AIADMK
    print("total vote of AIADMK=",AIADMK)
def check_BJP():
    global BJP
    print("total vote of BJP=",BJP)
def check_INC():
    global INC
    print("total vote of INC=",INC)
def check_PMK():
    global PMK
    print("total vote of PMK=",PMK)
def check_NOTA():
    global NOTA
    print("total vote of NOTA=",NOTA)
pin=9090
while True:
    choice=int(input("enter the number:"))
    if choice==1:
        TVK+=1
        check_TVK()
    elif choice==2:
        DMK+=1
        check_DMK()
    elif choice==3:
        AIADMK+=1
        check_AIADMK()
    elif choice==4:
        BJP+=1
        check_BJP()
    elif choice==5:
        INC+=1
        check_INC()
    elif choice==6:
        PMK+=1
        check_PMK()
    elif choice==7:
        NOTA+=1
        check_NOTA()
    else:
        vote_pin=int(input("enter the pin:"))
        if pin==vote_pin:
            print("closed")
        break

        

