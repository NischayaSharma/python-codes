import numpy as np;
#Q1: WAP to print the integer part of float number
def Ques1():
    num = input("Enter a Decimal Number: ");
    print "The integer part of ",num," is ",int(num);

#Q2: WAP to accept two num and display their and or not and exor results
def Ques2():
    num1 = input("Enter a number: ");
    num2 = input("Enter a number: ");
    print "1. ",num1," and ",num2," is ",num1&num2;
    print "2. ",num1," or ",num2," is ",num1|num2;
    print "3. ",num1," xor ",num2," is ",num1^num2;
    print "4. Not ",num1," is ",~num1
    print "5. Not ",num2," is ",~num2

#Q3: WAP to find the largest of 3 nums using conditional operator
def Ques3():
    num1, num2, num3 = input("Enter a number: "), input("Enter a number: "), input("Enter a number: ");
    max = num1 if(num1>num2 and num1>num3) else num2 if(num2>num1 and num2>num3) else num3;
    print "The maximum of",num1,",",num2,"and",num3,"is",max;

#Q4: WAP to input marks and differentiate them on the basis of nmarks out of 100
def Ques4(studentCount, subjectCount):
    distinction = 4;
    firstDivision = 3;
    secondDivision = 2;
    passClass = 1;
    fail = 0;
    arr = np.zeros((studentCount,subjectCount,2));
    for i in range(studentCount):
        for j in range(subjectCount):
            arr[i][j][0]=input("Enter marks of student %d subject %d: " % (i+1, j+1));
            arr[i][j][1]= 4 if(arr[i][j][0] >= 70) else 3 if(arr[i][j][0] >= 60) else 2 if(arr[i][j][0] >= 50) else 1 if(arr[i][j][0] >= 40) else 0;
    print "\nStudent\tSubject\tMarks\tDivision"
    for i in range(studentCount):
        for j in range(subjectCount):
            print i+1,"\t",j+1,"\t",arr[i][j][0],"\t","Distinction" if(arr[i][j][1]==4) else "First Division" if(arr[i][j][1]==3) else "Second Division" if(arr[i][j][1]==2) else "Just Pass" if(arr[i][j][1]==1) else "Fail";

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
        studentCount, subjectCount = input("Enter the number of students: "), input("Enter the number of subjects: ");
        Ques4(studentCount, subjectCount);
    elif(quesChoice==0):
        iterate=False;
    else:
        print "Enter a correct choice!!!"
