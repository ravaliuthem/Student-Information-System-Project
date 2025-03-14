import pickle
def deleterecord():
    try:
        with open("NIT.data","rb")as rp:
            records=list()
            while(True):
                try:
                    record=pickle.load(rp)
                    records.append(record)
                except EOFError:
                            break
#accept the Student number and remove
        sno=int(input("Enter student Number to Remove the Record:"))
        found=False
        for record in records:
            if(record[0]==sno):
             found=True
             delrec=record
             break
        if(found):
            records.remove(delrec)
            print("student Record Delete Successfully")
            with open("NIT.data","wb")as wp:
                for record in records:
                    pickle.dump(record,wp)
        else:
            print("Record Does not Exist")
    except FileNotFoundError:
        print("File Does not exist")