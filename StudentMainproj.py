from studentMenu import menu
from StudentAdd import SaveStuddata
from StudentView import getallrecords,getrecord
from StudentDelete import deleterecord
from StudentUpdate import updaterecord
from StudentSearch import searchrecord
while(True):
    menu()
    try:
        ch=int(input("enter ur choice:"))
        match(ch):
            case 1:
                SaveStuddata()
            case 2:
                getallrecords()
            case 3:
                getrecord()
            case 4:
                deleterecord()
            case 5:
                 updaterecord()
            case 6:
                searchrecord()
            case 7:
                print("Thanks for using this App")
                break
            case _:
                print("ur selection of operation Wrong---->try again")
    except ValueError:
        print("Don't Enter alnums,strs and symbols for choice---try again")








