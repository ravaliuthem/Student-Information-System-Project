import pickle
def getallrecords():
    try:
        with open("NIT.data","rb")as fp:
            print("_"*50)
            print("\tStudent Details")
            print("-"*50)
            while(True):
                try:
                    record=pickle.load(fp)
                    for val in record:
                        print("\t{}".format(val),end="\t")
                    print()
                except EOFError:
                    print("-"*50)
                    break
    except FileNotFoundError:
        print("File does not exist")
def getrecord():

    try:
         with open("NIT.data","rb")as fp:
             records=[]
             while(True):
                try:
                  record=pickle.load(fp)
                  records.append(record)
                except EOFError:
                           break
         try:
                sno=int(input("Enter Student Number to get other details:"))
                found=False
                for record in records:
                    if(sno==record[0]):
                         found=True
                         break
                if(found):
                    print("\t Student Number:{}".format(record[0]))
                    print("\t Student Name:{}".format(record[1]))
                    print("\t Student marks:{}".format(record[2]))
                else:
                    print("Student Record Does not Exist")
         except ValueError:
            print("Don't enter Alnums,strs and symbol for sno-->try again")
    except FileNotFoundError:
        print("File Does not Exist")















