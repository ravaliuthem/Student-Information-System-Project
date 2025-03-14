import pickle
class InvalidNameError(Exception):pass
class ZerolengthError(BaseException):pass
class SpaceNameError(Exception):pass
#code for validation of name
def validation(name):
    if(len(name)==0):
        raise ZerolengthError
    elif(name.isspace()):
        raise SpaceNameError
    else:
        Words=name.split()
        res=True
        for word in Words:
            if(not word.isalpha()):
                res=False
                break
            if(res):
                 return name
            else:
                raise InvalidNameError
def SaveStuddata():
    with open("NIT.data","ab")as fp:
        try:
            #read the student Data from kbd
            print("__________________")
            sno=int(input("Enter Student Number:"))
            sname=validation(input("Enter Student Name:"))
            marks = float(input("Enter Student Marks:"))
            print("______________________")
            #create an empty list for placing student values
            lst=[]
            lst.append(sno)
            lst.append(sname)
            lst.append(marks)
            #save lst data to student.pick file
            pickle.dump(lst,fp)
            print("student Data saved in afile Successfully")
        except ValueError:
            print("Dont enter Alnums,strand symbols for stno and marks")
        except InvalidNameError:
            print("InvalidName--try again")
        except ZerolengthError:
            print("Try to enter ur name")
        except SpaceNameError:
            print("Dont enter space for ur Name---try again:")
















