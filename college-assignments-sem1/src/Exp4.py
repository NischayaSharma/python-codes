#Q1: WAP to check if the entered character is a vowel or a consonant
def Ques1():
    ch = raw_input("Enter a letter: ");
    if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
        print ch,"is a vowel";
    else:
        print ch,"is a consonant";

#Q2: WAP to check the validity of triangle and then classify it on the basis of its sides
def Ques2():
    side1, side2, side3 = input("Enter the length of side 1: "), input("Enter the length of side 2: "), input("Enter the length of side 3: ");
    print "The Triangle exists" if (side1+side2>side3 and side2+side3>side1 and side3+side1>side2) else "The Triangle doesn't exist.",;
    if(side1==side2 and side2==side3):
        print "and is equilateral.";
    elif(side1==side2 or side2==side3 or side3==side1):
        print "and is isosceles.";
    elif(side1!=side2 and side2!=side3 and side3!=side1 and side1+side2>side3 and side2+side3>side1 and side3+side1>side2):
        print "and is scalene.";

#Q3: WAP to find the minimum number of notes or coins of different denominition
#    required for the give amount(Rs. 2000, 500, 200, 100, 50, 20, 10, 5, 2, 1)
def Ques3():
    amt = input("Enter the amount: ");
    totalNumOfNotes=0
    denominitions = [2000,500,200,100,50,20,10,5,2,1];
    for i in range (0,10):
        if(amt >= denominitions[i]):
            numOfNotes = amt//denominitions[i];
            print denominitions[i],":",numOfNotes;
            amt = amt-(numOfNotes*denominitions[i]);
            totalNumOfNotes+=numOfNotes;
    print "The total number of notes needed are",totalNumOfNotes;

#O4: WAP to perform operations such as multiply divide add subtract and modulus as per user's choice
def Ques4():
    num1, num2 = input("Enter a number: "), input("Enter a number: ");
    choice = input("Enter:\n1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Division\n5 for Remainder\n");
    if choice == 1:
        print num1,"+",num2,"=",num1+num2;
    elif choice == 2:
        print num1,"-",num2,"=",num1-num2;
    elif choice == 3:
        print num1,"X",num2,"=",num1*num2;
    elif choice == 4:
        print num1,"/",num2,"=",num1/num2;
    elif choice == 5:
        print num1,"mod",num2,"=",num1%num2;
    else:
        print("Wrong Choice!!");

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
