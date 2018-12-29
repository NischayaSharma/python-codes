import FileHandeling as fh;
import os;

CounterFilePath = "Users/nischaya/Documents/python-codes/files/counter.txt";
FilePath = "Users/nischaya/Documents/python-codes/files/Employee.txt";

def createEmployee(empFName, empLName, empSalary,  empEmailId):
    string = empFName+"|"+empLName+"|"+empSalary+"|"+empEmailId+"\n";
    fh.createFile(FilePath,string,CounterFilePath);


def searchEmployee(searchStr,choice):
    string = fh.readFile(FilePath,searchStr,choice);
    return string;


def updateEmployee(lineNum, empFName, empLName, empSalary,  empEmailId):
    if(empFName == ""):
        record = fh.readFile(FilePath,str(lineNum-1),0);
        empDetails = record[0].split('|');
        empFName = empDetails[1];
    if(empLName == ""):
        record = fh.readFile(FilePath,str(lineNum-1),0);
        empDetails = record[0].split('|');
        empLName = empDetails[2];
    if(empSalary == ""):
        record = fh.readFile(FilePath,str(lineNum-1),0);
        empDetails = record[0].split('|');
        empSalary = empDetails[3];
    if(empEmailId == ""):
        record = fh.readFile(FilePath,str(lineNum-1),0);
        empDetails = record[0].split('|');
        empEmailId = empDetails[4];
    updateStr = str(lineNum-1)+"|"+empFName+"|"+empLName+"|"+empSalary+"|"+empEmailId+"\n";
    fh.updateRecord(FilePath,FilePath,updateStr,lineNum-1);


def deleteEmployee(lineNum):
    fh.deleteRecord(FilePath,FilePath,lineNum-1,CounterFilePath);


def main():
    goOn = True;

    while goOn:
        choice = input("Press:\n1 to enter a new employee\n2 to search employee\n3 to update employee\n4 to delete employee\n5 to view the file\n0 to exit\n");

        #Creating employees
        if(choice == 1):
            numOfEmployees = int(input("Enter number of employees: "));
            for i in range(numOfEmployees):
                empFName, empLName, empSalary,  empEmailId = raw_input("Enter employee first name: "), raw_input("Enter employee last name: "), raw_input("Enter employee salary: "), raw_input("Enter employee Email ID: ");
                createEmployee(empFName, empLName, empSalary,  empEmailId);

        #Searching for an employee
        elif(choice == 2):
            choice = int(input("Press:\n1 to search by First Name\n2 to search by Last Name\n3 to search by Salary\n4 to search by Email ID\n"));

            #Searching by parameters
            if(choice == 1):
                print "First Name:",;
            elif(choice == 2):
                print "Last Name:",;
            elif(choice == 3):
                print "Salary:",;
            elif(choice == 4):
                print "Email ID:",;
            else:
                print "Wrong Choice!!!";

            searchStr = raw_input();
            string = searchEmployee(searchStr,choice);
            print('\n'.join(string));

        #Updating the Employee
        #WARNING: Throws Error when updating a non-existent Employee
        elif(choice == 3):
            fh.printFile(FilePath);
            print "Leave the entries empty if you dont want to update that entry.";
            lineNum = input("Enter the line number of the entry you want to update: ");
            empFName, empLName, empSalary,  empEmailId = raw_input("Enter employee first name: "), raw_input("Enter employee last name: "), raw_input("Enter employee salary: "), raw_input("Enter employee Email ID: ");
            updateEmployee(lineNum, empFName, empLName, empSalary,  empEmailId);
            fh.printFile(FilePath);

        #Deleting an Employee
        #WARNING: Throws Error when deleting a non-existent Employee
        elif(choice == 4):
            fh.printFile(FilePath);
            lineNum = input("Enter the line number of the entry you want to delete: ");
            deleteEmployee(lineNum);
            fh.printFile(FilePath);

        elif(choice == 0):
            goOn = False;

        elif(choice == 5):
            fh.printFile(FilePath);
        else:
            print "Wrong Choice!!!";


main();
