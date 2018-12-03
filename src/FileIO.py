import os;
import sys;

FileName='FileIO.txt'

def fileInput(fw,numOfEmployees):

    #Getting the value of counter
    frc = open(os.path.dirname(os.path.realpath(__file__))+"/counter.txt","r");
    counter = int(frc.read());
    frc.close();

    #Taking input and writing to the file
    for i in range(counter,numOfEmployees+counter):
        empFName, empLName, empSalary,  empEmailId = raw_input("Enter employee first name: "), raw_input("Enter employee last name: "), raw_input("Enter employee salary: "), raw_input("Enter employee Email ID: ");
        string = str(i)+" "+empFName+" "+empLName+" "+empSalary+" "+empEmailId+"\n";
        fw.write(string);
        counter += 1;

    #Writing back to counterthe updated value.
    fwc = open(os.path.dirname(os.path.realpath(__file__))+"/counter.txt","w");
    fwc.write(str(counter)+"\n");
    fwc.close();


def fileSearch(fw, searchStr):
    line = fw.readline();
    while line:
        empId, empFName, empLName, empSalary,  empEmailId = line.split();
        if(searchStr == empFName):
            print line;
        line = fw.readline();


def fileUpdate(fw,lineNum):

    #Taking the new record as input
    empFName, empLName, empSalary,  empEmailId = raw_input("Enter employee first name: "), raw_input("Enter employee last name: "), raw_input("Enter employee salary: "), raw_input("Enter employee Email ID: ");
    updateStr = str(lineNum)+" "+empFName+" "+empLName+" "+empSalary+" "+empEmailId+"\n";

    #Replacing the given record with he updated record and writing back to file
    lines = fw.readlines();
    fwu = open(string, "w");
    lines[lineNum]= updateStr;
    for line in lines:
        fwu.write(line);
    fwu.close();


def fileDelete(lineNum):

    #Deleting the record
    lines = fw.readlines();
    fwu = open(string, "w");
    lines.pop(lineNum);

    #Correcting the Employee Ids and Writing Back to File
    for line in lines:
        empId, empFName, empLName, empSalary,  empEmailId = line.split();
        empId = str(lines.index(line));
        line = empId+" "+empFName+" "+empLName+" "+empSalary+" "+empEmailId+"\n";
        fwu.write(line);
    fwu.close();

    #Reducing Counter value
    frc = open(os.path.dirname(os.path.realpath(__file__))+"/counter.txt","r");
    counter = int(frc.read());
    frc.close();
    fwc = open(os.path.dirname(os.path.realpath(__file__))+"/counter.txt","w");
    fwc.write(str(counter-1)+"\n");
    fwc.close();


def filePrint():
    fw.seek(0);
    lines = fw.readlines();
    print "The File: "
    for line in lines:
        print line;


def crud():

    #Creating and writing to file
    fw.seek(0);
    numOfEmployees = input("Enter the number of employees: ");
    fileInput(fw,numOfEmployees);
    filePrint();

    #Reading the file for an element
    fw.seek(0);
    searchStr = raw_input("Enter the name of the employee you want to search: ");
    fileSearch(fw,searchStr);
    filePrint();

    #Updating an entry in the file
    fw.seek(0);
    lineNum = int(input("Enter the entry you want to update(The entries start with 0 so the 1st entry is 0th entry and so on.): "));
    fileUpdate(fw,lineNum);
    filePrint();

    #Deleting an entry from the file
    fw.seek(0);
    lineNum = int(input("Enter the entry you want to delete(The entries start with 0 so the 1st entry is 0th entry and so on.): "));
    fileDelete(lineNum);
    filePrint();

    #Closing the file
    fw.close();


try:
    string = os.path.dirname(os.path.realpath(__file__))+'/'+FileName;
    fw = open(string, "a+");
    crud();
except Exception as e:
    print e;
    fw.close();
    sys.exit();
