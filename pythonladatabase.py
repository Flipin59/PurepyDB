#Imports a new library
import pickle

#Creates a new entry(appending)
def addnew():
    stu ={}
    fh = open("Stu.dat", 'ab')
    noint = int(input("How many entries would you like to add :"))
    for i in range(noint):
        rollno = int(input("Enter roll number of student : "))
        name = input("Enter Name of student : ")
        marks = float(input("Enter marks of student : "))
        stu['Roll No.'] = rollno
        stu['Name'] = name
        stu['Marks']= marks
        pickle.dump(stu, fh)
    fh.close()

#Select to view entire Database
def view():
    fh = open("Stu.dat", 'rb')
    stu={}
    try:
        while True:
            stu = pickle.load(fh)
            print(stu)
    except EOFError:
        print("All data Successfully Printed")
        fh.close()

#Search for a single entry
def search():
    fh = open("Stu.dat", 'rb')
    stu={}
    squery = int(input("Enter the roll no. you want to search for : "))
    scsmtr = False
    try:
        while True:
            stu = pickle.load(fh)
            if stu['Roll No.'] == squery:
                print("The following details are present")
                print(stu)
                scsmtr = True
    except EOFError:
        if scsmtr == True:    
            print("Search Complete..")
        else:
            print("Student data not present")
    fh.close()  

#update db
def update():
    fh = open("Stu.dat", 'rb+')
    stu={}
    squery = int(input("Enter the roll no. you want to search for : "))
    scsmtr = False
    try:
        while True:
            ppos = fh.tell()
            stu = pickle.load(fh)
            if stu['Roll No.'] == squery:
                print("The following details are present")
                print(stu)
                print("What do You want to update??")
                print(r"1. Roll No., 2. Name, 3. Marks (1,2,3)")
                choice=int(input())
                if choice == 1:
                    temp = int(input("Enter new Roll No."))
                    stu['Roll No.'] = temp
                    fh.seek(ppos)
                    pickle.dump(stu,fh)
                    scsmtr = True
                elif choice == 2:
                    temp = input("Enter new name")
                    stu['Name'] = temp
                    fh.seek(ppos)
                    pickle.dump(stu,fh)
                    scsmtr = True
                elif choice == 3:
                    temp = float(input("Enter new Marks"))
                    stu['Marks'] = temp
                    fh.seek(ppos)
                    pickle.dump(stu,fh)
                    scsmtr = True
                else:
                    scsmtr = False
    except EOFError:
        if scsmtr == True:    
            print("DB updated")
        else:
            print("Something went wrong")
    fh.close()  
view()

