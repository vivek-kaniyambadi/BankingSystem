#Banking Application
accountNo=0
cusname=''
Bcode=""
Mobile=0
Bal=0
def createAccounts():
    global accountNo
    global cusname
    global Bcode
    global Mobile
    global Bal
    accountNo=int(input("Enter Account Number:"))
    cusname=input("Enter Name:")
    Bcode=input("Enter Branch Code:")
    Mobile=input("Enter Mobile Number:")
    Bal=int(input("Enter Current Balance:"))
def ShowAccountdetails():
    print("accountno:",accountNo)
    print("Customer Name:",cusname)
    print("Bcode:",Bcode)
    print("Mobile:",Mobile)

def Deposit(amount):
    global Bal
    Bal = Bal+amount
    checkbalance()
def Withdraw(amount):
    global Bal
    Bal = Bal-amount
    checkbalance()
def checkbalance():
    print("current Balance:",Bal)

#Main
ch1='y'
while (ch1=='y'):
    print("1.create account\n 2.Withdraw\n 3.Deposit\n 4.Check balance")
    ch=int(input("Select any option:"))
    if(ch==1):
        createAccounts()
    elif(ch==2):
        amnt=int(input("Enter amount to withdraw"))
        Withdraw(amnt)
    elif(ch==3):
        amnt=int(input("Enter amount to Deposit"))
        Deposit(amnt)
    elif(ch==4):
        checkbalance()
    else:
        print("Please select any 4 options available above")
    print("Do you want to continue...press y")
    ch1=input()