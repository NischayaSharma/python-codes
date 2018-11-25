#Q1: WAP to print the powers of 2 table upto 10
def Ques1():
    for i in range(0,10):
        print "2 to the power",i,"is",2**i;

#Q2: WAP to read the number of students in a PPS lecture and take their quiz 1 marks as input and calculate the average
def Ques2():
    numOfStud = input("Enter the number of students: ");
    min = maxPoss = input("Enter the maximum marks possible: ");
    sum = max = 0;
    i=1;
    while(True):
        marks = input("Enter the marks of student");
        if marks>maxPoss:
            print "Invalid input!!";
            continue;
        max = max if(max>marks) else marks;
        min = min if(min<marks) else marks;
        sum += marks;
        if(i>=numOfStud):
            break;
        i+=1;
    avg = sum/numOfStud;
    print "The maximum marks are",max,"and the minimum are",min,"with an average of",avg;

#Q3: WAP for the working of an ATM
def Ques3():
    balance = 500000;
    pin = input("Enter your pin: ");
    if(pin==1703):
        print "Your current balance is",balance;
        choice = input("Enter your choice:\n1. Check Your Balance\n2. Withdraw Money\n3. Deposit money\n4. Quit\n");
        if(choice==1):
            print "The balance left in your account is",balance;
        elif(choice==2):
            cashWithdrawn=input("Enter the amount you want to withdraw: ");
            if(balance - cashWithdrawn>=500):
                print "Your transaction was successful.\nYour previous balance was ",balance;
                balance = balance-cashWithdrawn;
                print "Your current balance is",balance;
            else:
                print "You have to maintain a minimum of Rs.500 in your account.\nThe maximum you can withdraw right now is",balance-500;
        elif(choice==3):
            cashDeposited = input("Enter the amount of cash you want to deposit: ");
            print "Your transaction was successful.\nYour previous balance was",balance;
            balance+=cashDeposited;
            print "Your current balance is",balance;
        else:
            print "Invalid Choice!!";
    else:
        print "Wrong PIN !!!";

#Q4: WAP to print triangles with * straight and inverted
def Ques4():
    numOfRows = input("Enter the number of rows of the triangle: ");
    choiceOfDirection = input("Enter 0 for a straight triangle and 1 for an inverted triangle: ");
    if choiceOfDirection==0:
        for i in range(1,numOfRows+1):
            for j in range(0,i):
                print "*",;
            print "";
    elif choiceOfDirection==1:
        for i in range(numOfRows,0,-1):
            for j in range(0,i):
                print "*",;
            print "";
    else:
        print "Wrong choice !!!!";

#PSV main()
iterate = True;
while(iterate):
    quesChoice = input("Enter the question number (1 to 4) you want to view(Press 0 to terminate): ");
    if(quesChoice==1):
        Ques1();
    elif(quesChoice==2):
        Ques2();
    elif(quesChoice==3):
        Ques3();
    elif(quesChoice==4):
        Ques4();
    elif(quesChoice==0):
        iterate=False;
    else:
        print "Enter a correct choice!!!"
