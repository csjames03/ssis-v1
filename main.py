import eel
import csv 
filename = "StudentInformation.csv"


eel.init("gui")  

@eel.expose
def GetStudentsInfo():
    students = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            students.append(row)
    return students

@eel.expose
def AddStudent(studentData):
    with open(filename, "a", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(studentData)



@eel.expose 
def getSpecificStudent(lrn):
     rows = []
     with open(filename, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if str(row[0]) == str(lrn): 
                rows.append(row)
     return rows

@eel.expose
def DeleteStudent(lrn):
    lines = []
    with open(filename, "r") as file:
        for line in file:
            if not line.startswith(str(lrn) + ","):
                lines.append(line)

    with open(filename, "w") as file:
        file.writelines(lines)


@eel.expose
def UpdateStudent(lrn, studentData):
    rows = []
    print(studentData)
    with open(filename, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if str(row[0]) == str(lrn): 
                row = studentData 
            rows.append(row)

    with open(filename, "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(rows)




@eel.expose
def lrnSearch(value):
    items = []
    with open(filename, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0].startswith(
                value
            ):  # Assuming the LRN is in the first column
                items.append(row)
    return items

@eel.expose
def nameSearch(value):
    items = []
    with open(filename, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[1].upper().startswith(
                value
            ):  # Assuming the name is in the first column
                items.append(row)
    return items

eel.start("index.html")  