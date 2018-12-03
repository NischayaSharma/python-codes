
def createFile(fo,numOfRecords,data,counterFile):
    #Getting the value of counter
    frc = open(counterFile,"r");
    counter = int(frc.read());
    initCounter = counter;
    frc.close();

    #Taking input and writing to the file
    for i in range(counter,numOfRecords+counter):
        string = str(i)+"|"+data[i-initCounter];
        fo.write(string);
        counter += 1;

    #Writing back to counter the updated value.
    fwc = open(counterFile,"w");
    fwc.write(str(counter)+"\n");
    fwc.close();


def readFile(fo,searchStr,criteria):
    fo.seek(0);
    line = fo.readline();
    string = [];
    while line:
        entries = line.split('|');
        if(searchStr == entries[criteria]):
            string.append(line);
        line = fo.readline();
    return string;


def printFile(fo):
    lines = fo.readlines();
    print "The File: "
    for line in lines:
        print line;


def updateRecord(fo,fileLoc,updateStr,lineNum):

    #Replacing the given record with he updated record and writing back to file
    lines = fo.readlines();
    fwu = open(fileLoc, "w");
    lines[lineNum]= updateStr;
    for line in lines:
        fwu.write(line);
    fwu.close();


def deleteRecord(fo,fileLoc,lineNum,counterFile):
    #Deleting the record
    lines = fo.readlines();
    fwu = open(fileLoc, "w");
    lines.pop(lineNum);

    #Correcting the Employee Ids and Writing Back to File
    for line in lines:
        entry1, entry2, entry3, entry4, entry5 = line.split('|');
        entry1 = str(lines.index(line));
        line = entry1+"|"+entry2+"|"+entry3+"|"+entry4+"|"+entry5;
        fwu.write(line);
    fwu.close();

    #Reducing Counter value
    frc = open(counterFile,"r");
    counter = int(frc.read());
    frc.close();
    fwc = open(counterFile,"w");
    fwc.write(str(counter-1)+"\n");
    fwc.close();
