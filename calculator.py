print("\t WELCOME \n")
print("\t BASIC CALCULATOR \n")
condition=True
while(condition==True):
    print(" 1. ADDITION \n 2. SUBTRACTION \n 3. MULTIPLICATION \n 4. DIVISION")
    ch=int(input("ENTER YOUR CHOICE: "))
    if (ch==1):
        num1=int(input("ENTER FIRST NUMBER "))
        num2=int(input("ENTER SECOND NUMBER "))
        add=num1+num2
        print("ADDITION OF GIVEN NUMBER IS ",add)
    elif(ch==2):
        num1=int(input("ENTER FIRST NUMBER "))
        num2=int(input("ENTER SECOND NUMBER "))
        sub=num1-num2
        print("SUBTRACTION OF GIVEN NUMBER IS ",sub)
    elif(ch==3):
        num1=int(input("ENTER FIRST NUMBER "))
        num2=int(input("ENTER SECOND NUMBER "))
        multi=num1*num2
        print("MULTIPLICATION OF GIVEN NUMBER IS ",multi)
    elif(ch==4):
        num1=int(input("ENTER FIRST NUMBER "))
        num2=int(input("ENTER SECOND NUMBER "))
        divi=num1/num2
        print("DIVISION OF GIVEN NUMBER IS ",divi)
    else:
        print("INVALID INPUT")
    do=input("DO YOU WANT TO TRY MORE('YES'/'NO'):" )
    if(do=="YES") or(do=="yes")or(do=="Yes"):
        condition=True
    else:
        condition=False
print("\t :) THANKYOU :)")
