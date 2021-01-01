from threading import*
import time

d={} #d is the dictionary to store data

#for create operation
def create(key,value,timeout=0):
    if key in d:
        print("Error: this KEY already exists") #1st error message
    else:
        if(key.isalpha()):
            if len(d)<(1024*1024*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input keyname capped at 32chars
                    d[key]=l
            else:
                print("Error: Memory limit has Exceeded!")#2nd error message
        else:
            print("Error: key_name is Invalid! key_name must contain only alphabets and no special characters or numbers")#3rd error message

#for read operation        
def read(key):
    if key not in d:
        print("Error: Given KEY does not exist in database. Please enter a valid KEY") #4th error message
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #compare the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject 
                return stri
            else:
                print("Error: Time-to-Live of",key,"has Expired") #5th error message
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#for delete operation
def delete(key):
    if key not in d:
        print("Error: Given KEY does not exist in database. Please enter a valid KEY") #6th error message
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #compare the current time with expiry time
                del d[key]
                print("KEY is successfully Deleted")
            else:
                print("Error: Time-to-Live of",key,"has Expired") #7th error message
        else:
            del d[key]
            print("KEY is successfully Deleted")

#for modify operation 
def modify(key,value):
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("Error: Given KEY does not exist in database. Please enter a valid KEY") #8th error message
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("Error: Time-to-Live of",key,"has Expired") #9th error message
    else:
        if key not in d:
            print("Error: Given KEY does not exist in database. Please enter a valid KEY") #10th error message
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l
