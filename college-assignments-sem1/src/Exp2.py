#Q1: WAP to print employee details like employee number, name, address and phone number.
def Ques1():
    print "Employee Number: \t12345\nEmployee Name: \t\tNischaya\nEmployee address: \tJuhu\nEmployee Phone Number: \t8160332475";

#Q2: WAP to calculate the area of circle, rectangle and triangle.
def Ques2():
    choice = input("Enter: \n1 for Circle\n2 for Rectangle\n3 for Triangle\n");
    if(choice==1):
        radius = input("Enter the radius of the Circle: ");
        area = 3.14*radius*radius;
    elif(choice==2):
        length, breadth = input("Enter the length of the Rectangle: "), input("Enter the breadth of the Rectangle: ");
        area = length*breadth;
    elif(choice==3):
        height, base = input("Enter the height of the Triangle: "), input("Enter the length of the base of Triangle: ");
        area = 0.5*height*base;
    else:
        print "Enter correct choice next time !!!!!"
    print "The area is ",area

#Q3: WAP to calculate the following expressions:
#      1.  2x^3 + x^2 + 2x + 3
#      2.  x + y^2 + z^3
def Ques3():
    x, y, z = input("Enter the value of x: "), input("Enter the value of y: "), input("Enter the value of z: ")
    result1 = (2*x*x*x)+(x*x)+(2*x)+3
    result2 = x+(y*y)+(z*z*z)
    print "2x^3 + x^2 + 2x + 3 = ",result1,"\nx + y^2 + z^3 = ",result2

#Q4: WAP to swap two numbers
def Ques4():
    a, b = input("Enter the value of a: "), input("Enter the value of b: ");
    a = a+b;
    b = a-b;
    a = a-b;
    print "After Swapping:\na: ",a,"\nb: ",b;

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
