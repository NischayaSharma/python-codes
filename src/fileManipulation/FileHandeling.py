
def createFile(FilePath,data,counterFile):
    #Getting the value of counter
    with open(counterFile,"r") as frc:
        counter = int(frc.read());
        initCounter = counter;

    #Taking input and writing to the file
    with open(FilePath,"a+") as fo:
        string = str(counter)+"|"+data;
        fo.write(string);
        counter += 1;

    #Writing back to counter the updated value.
    with open(counterFile,"w") as fwc:
        fwc.write(str(counter)+"\n");


def readFile(FilePath,searchStr,criteria):
    with open(FilePath,"r") as fo:
        fo.seek(0);
        line = fo.readline();
        string = [];
        while line:
            entries = line.split('|');
            if(searchStr == entries[criteria]):
                string.append(line);
            line = fo.readline();
    return string;


def printFile(FilePath):
    with open(FilePath,"r") as fo:
        fo.seek(0);
        lines = fo.readlines();
        print "The File: "
        for line in lines:
            print line;


def updateRecord(FilePath,fileLoc,updateStr,lineNum):

    #Replacing the given record with he updated record and writing back to file
    with open(FilePath,"r") as fo:
        fo.seek(0);
        lines = fo.readlines();
    with open(fileLoc, "w") as fwu:
        lines[lineNum]= updateStr;
        for line in lines:
            fwu.write(line);


def deleteRecord(FilePath,fileLoc,lineNum,counterFile):
    #Deleting the record
    with open(FilePath,"r") as fo:
        fo.seek(0);
        lines = fo.readlines();
    lines.pop(lineNum);

    #Correcting the Employee Ids and Writing Back to File
    with open(fileLoc, "w") as fwu:
        for line in lines:
            entry1, entry2, entry3, entry4, entry5 = line.split('|');
            entry1 = str(lines.index(line));
            line = entry1+"|"+entry2+"|"+entry3+"|"+entry4+"|"+entry5;
            fwu.write(line);

    #Reducing Counter value
    with open(counterFile,"r") as frc:
        counter = int(frc.read());
    frc.close();
    with open(counterFile,"w") as fwc:
        fwc.write(str(counter-1)+"\n");
