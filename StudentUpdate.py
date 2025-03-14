import pickle
from StudentAdd import validation,InvalidNameError,ZerolengthError,SpaceNameError
def updaterecord():
    try:
        with open("NIT.data","rb")as rp:
            records=list()
            while(True):
                try:
                    record=pickle.load(rp)
                    records.append(record)
                except EOFError:
                            break
    except FileNotFoundError:
        print("File Does not Exist")
        #accept the student Number for updating sname and marks
    try:
        sno=int(input("Enter student Number to update the Record:"))
        found=False
        for i in range(len(records)):
            if(records[i][0]==sno):
                 recno=i
                 #record[i][1]=input("Enter New name for updating its old name:")
                #records[i][2]=float(input("Enter New Marks for updating its old Marks:"))
                 found=True
                 break
        if(found):
            records[recno][1]=validation(input("Enter New Name for Updating its old Name:"))
            records[recno][2]=float(input("Enter New marks for Updating its old marks:"))
            with open("NIT.data","wb")as fp:
                for record in records:
                    pickle.dump(record,fp)
            print("Student Record updated successfully")
        else:
            print("student Record does not exist")
    except ValueError:
        print("Dont enter alnums,strs and Symbols for sno,marks")
    except InvalidNameError:
        print("Invalid Name-->Try again:")
    except ZerolengthError:
        print("try to enter ur name")
    except SpaceNameError:
        print("Don' enter space for ur Name--->try again:")





