class User:
    username=''    
    card_pin=0
    account_balance=0.0
    def enter_pin(card_pin):
        p=input()
        if p==card_pin:
            pass
        else:
            print("Invalid Entry. Transaction Failed. Remove Card.\n")
            exit()
        return 0    
    def view_balance(account_balance):
        print(account_balance)
        return 0
    def deposit(account_balance):
        print("Enter amount to be deposited between Rs.5000 and Rs.500000.")
        amount=float(input())
        if amount < 5000 or amount > 500000:
            print("Invalid Entry. Transaction Failed. Remove Card.\n")
        else:
            account_balance+=amount
            print("Transaction Complete. Remove Card.\n")
        return account_balance
    def withdraw(account_balance):
        print("Enter amount to be withdrawn.")
        amount=float(input())
        if amount > account_balance:
            print("Not enough Account Balance. Transaction Failed. Remove Card.\n")
        else:
            account_balance-=amount
            print("Transaction Complete. Remove Card.\n")
        return account_balance        

print("CARD ENTERED")
print("If you are a new user, type 1 to create an account.")
print("If you already have an account, type 2 to sign in.")
print("Type 0 to exit procedure.")
n=int(input())
if n==0:
    print("Procedure Cancelled. Remove Card.\n")
    exit()
elif n==1:
    def invalid():
        print("Invalid Entry. Failed to create Account. Remove card.\n")
        return 0
    def digits(n):
        c=0
        while n!=0:
            n//=10
            c+=1
        return c
    def details(content):
        file=open('Details.txt','a')
        file.write(content)
        file.close()
        return 0
    print("Create User Name beginning with an alphabet, and containing alphabets, numbers or underscore.")
    s=input()
    file=open('Details.txt','a')
    file.close()
    file=open('Details.txt','r')
    var_read=file.read()
    statements=var_read.split("\n")
    for statement in statements:
        names=statement.split(" ")
        uname=names[0]
        if uname==s:
            print("Username Already Exists. Remove Card and Try Again.\n")
            file.close()
            exit()
    file.close()        
    if s[0].isalpha():
        pass
    else:
        invalid()
        exit()
    for c in s:
        if c.isalpha() or c.isdigit() or c=='_':
            pass 
        else:
            invalid()
            exit()        
    print("Create PIN of 6 digits, not beginning with 0")
    pin_s=input()
    for c in pin_s:
        if c.isdigit:
            pass 
        else:
            invalid()
            exit()
    if int(pin_s[0])==0:
        invalid()
        exit()
    pin=int(pin_s)
    if digits(pin)==6:
        pass
    else:
        invalid()
        exit()
    print("Enter Amount to be Deposited for the first time, between Rs.5000 and Rs.500000.")
    bal_s=input()
    for c in s:
        if c.isdigit:
            pass 
        else:
            invalid()
            exit()
    bal=float(bal_s)
    if bal < 5000 or bal > 500000:
        invalid()
        exit()
    details(s+' ')
    details(str(pin)+' ')
    details(str(bal)+' '+'\n')
    print("Account Created Successfully. Remove Card.\n")
    exit()
elif n==2:
    def complete():
        print("Transaction Complete. Remove Card.\n")
    U=User()
    def read_details(U):
        file=open('Details.txt','r')
        var=file.read()
        lines=var.split("\n")
        for line in lines:
            names=line.split(" ")
            uname=names[0]
            if uname==U.username:
                U.card_pin=int(names[1])
                U.account_balance=float(names[2])
                file.close()
                return 0
        file.close()        
        print("Username Not Found. Remove Card.\n")        
        exit()
        return 0
    def write_details(U):
        file=open('Details.txt','r')
        var=file.read()
        file.close()
        file=open('Details.txt','a')
        file.truncate(0)
        lines=var.split("\n")
        for line in lines:
            if line != (U.username+' '+str(U.card_pin)+' '+str(U.account_balance)+' '):
                 file.write(line+'\n')
        file.close()        
        return 0
    file=open('Details.txt','a')
    file.close()
    print("Put Card and Enter Username.")
    U.username=input()
    read_details(U)
    print("Enter PIN.")
    pn=int(input())
    if pn==U.card_pin:
        pass
    else:
        print("Incorrect PIN. Transaction Failed. Remove Card.\n")
        exit()
    print("To view Account Balance, type 1.")
    print("To Withdraw Amount, type 2.")
    print("To Deposit Amount, type 3.")
    print("To Cancel transaction, type 0.")
    i=int(input())
    if i==1:
        User.view_balance(U.account_balance)
        complete()
        exit()
    elif i==2:
        write_details(U)
        U.account_balance=User.withdraw(U.account_balance)
        file=open('Details.txt','a')
        file.write(U.username+' '+str(U.card_pin)+' '+str(U.account_balance)+' '+'\n')
        file.close()
        exit()
    elif i==3:
        write_details(U)
        U.account_balance=User.deposit(U.account_balance)
        file=open('Details.txt','a')
        file.write(U.username+' '+str(U.card_pin)+' '+str(U.account_balance)+' '+'\n')
        file.close()
        exit()
    elif i==0:
        print("Transaction Cancelled. Remove Card.\n")
        exit()
    else:
        print("Invalid Entry. Transaction Failed. Remove Card\n")
        exit()
else:
    print("Invalid Entry, Procedure Failed\n")
    exit()
