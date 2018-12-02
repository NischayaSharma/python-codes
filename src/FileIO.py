import os;
import sys;

FileName='FileIO.txt'

def fileInput(fw,numOfEmployees):
    frc = open(os.path.dirname(os.path.realpath(__file__))+"/counter.txt","r");
    counter = int(frc.read());
    frc.close();
    for i in range(counter,numOfEmployees+counter):
        empFName, empLName, empSalary,  empEmailId = raw_input("Enter employee first name: "), raw_input("Enter employee last name: "), raw_input("Enter employee salary: "), raw_input("Enter employee Email ID: ");
        string = str(i)+" "+empFName+" "+empLName+" "+empSalary+" "+empEmailId+"\n";
        fw.write(string);
        counter += 1;
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

def fileUpdate(lineNum):
    empFName, empLName, empSalary,  empEmailId = raw_input("Enter employee first name: "), raw_input("Enter employee last name: "), raw_input("Enter employee salary: "), raw_input("Enter employee Email ID: ");
    fr = open(string, "r");
    lines = fw.readlines();
    fr.close();
    fwu = open(string, "w");
    lines[lineNum]= str(lineNum)+" "+empFName+" "+empLName+" "+empSalary+" "+empEmailId+"\n";
    for line in lines:
        fwu.write(line);
    fwu.close();

def filePrint():
    fw.seek(0);
    lines = fw.readlines();
    print "The File: "
    for line in lines:
        print line;
def main():
    fw.seek(0);
    numOfEmployees = input("Enter the number of employees: ");
    fileInput(fw,numOfEmployees);
    filePrint();
    fw.seek(0);
    searchStr = raw_input("Enter the name of the employee you want to search: ");
    fileSearch(fw,searchStr);
    filePrint();
    fw.seek(0);
    lineNum = int(input("Enter the entry you want to update(The entries start with 0 so the 1st entry is 0th entry and so on.): "));
    fileUpdate(lineNum);
    filePrint();
    fw.close();

try:
    string = os.path.dirname(os.path.realpath(__file__))+'/'+FileName;
    fw = open(string, "a+");
    main();
except Exception as e:
    print e;
    fw.close();
    sys.exit();
