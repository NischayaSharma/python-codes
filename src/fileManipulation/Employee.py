import FileHandeling as fh;
import os;
class Employee:


    def createEmployee(self):
        numOfEmployees = int(input("Enter number of employees: "));
        empDetails = [];
        for i in range(numOfEmployees):
            empFName, empLName, empSalary,  empEmailId = raw_input("Enter employee first name: "), raw_input("Enter employee last name: "), raw_input("Enter employee salary: "), raw_input("Enter employee Email ID: ");
            string = str(i)+" "+empFName+" "+empLName+" "+empSalary+" "+empEmailId+"\n";
            empDetails.append(string);
        with open(FilePath,"a+") as fo:
            fo.seek(0);
            fh.createFile(fo,numOfEmployees,empDetails,CounterFilePath);


    def searchEmployee(self):
        choice = int(input("Press:\n1 to search by First Name\n2 to search by Last Name\n3 to search by Salary\n4 to search by Email ID\n"));
        print "Enter the",;
        if(choice == 1):
            print "First Name:",;
        elif(choice == 2):
            print "Last Name:",;
        elif(choice == 3):
            print "Salary:",;
        elif(choice == 4):
            print "Email ID:",;
        searchStr = raw_input();
        with open(FilePath,"r") as fo:
            string = fh.readFile(fo,searchStr,choice-1);
        while line in string:
            print line;


    def updateEmployee(self):
        print "Leave the entries empty if you dont want to update that entry.";
        lineNum = input("Enter the line number of the entry you want to update: ");
        with open(FilePath,"r") as fo:
            empFName, empLName, empSalary,  empEmailId = raw_input("Enter employee first name: "), raw_input("Enter employee last name: "), raw_input("Enter employee salary: "), raw_input("Enter employee Email ID: ");
            if(empFName == ""):
                record = fh.readFile(fo,lineNum-1,0);
                empDetails = record[0].split();
                empFName = empDetails[1];
            if(empLName == ""):
                record = fh.readFile(fo,lineNum-1,0);
                empDetails = record[0].split();
                empLName = empDetails[2];
            if(empSalary == ""):
                record = fh.readFile(fo,lineNum-1,0);
                empDetails = record[0].split();
                empSalary = empDetails[3];
            if(empEmailId == ""):
                record = fh.readFile(fo,lineNum-1,0);
                empDetails = record[0].split();
                empEmailId = empDetails[4];
            updateStr = str(lineNum-1)+" "+empFName+" "+empLName+" "+empSalary+" "+empEmailId+"\n";
            fh.updateRecord(fo,FilePath,updateStr,lineNum-1);


    def deleteEmployee(self):
        lineNum = input("Enter the line number of the entry you want to delete: ");
        with open(FilePath,"r") as fo:
            fh.deleteRecord(fo,FilePath,lineNum-1);


    def main(self):
        goOn = True;
        employee = Employee();
        while goOn:
            choice = input("Press:\n1 to enter a new employee\n2 to search employee\n3 to update employee\n4 to delete employee\n0 to exit\n");
            if(choice == 1):
                employee.createEmployee();
            elif(choice == 2):
                employee.searchEmployee();
            elif(choice == 3):
                employee.updateEmployee();
            elif(choice == 4):
                employee.deleteEmployee();
            elif(choice == 0):
                goOn = False;
            else:
                print "Wrong Choice!!!";


CounterFilePath = os.path.dirname(os.path.realpath(__file__))+"/counter.txt";
FilePath = os.path.dirname(os.path.realpath(__file__))+"/FileIO.txt";
emp = Employee();
emp.main();
