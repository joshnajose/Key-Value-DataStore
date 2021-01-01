#importing the main file as a library 
import code as c

c.create("Oberoi",15)
#creating a key with key_name,value given and with no time-to-live property

c.create("Radisson",60,2600) 
#creating a key with key_name,value given and with time-to-live property value given in number of seconds

c.read("Oberoi")
#for returning the value of the respective key in Jasonobject format 'key_name:value'

c.read("Radisson")
#for returning the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR

c.create("Radisson",40)
#returns an ERROR since the key_name already exists in the database

#To overcome this error 
#either use modify operation to change the value of a key
c.modify("Radisson",50)
#it replaces the initial value of the respective key with new value 

#or use delete operation and recreate it
c.delete("Radisson")
#it deletes the respective key and its value from the database

#to access these using multiple threads like
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()
#until tn

#the code also returns the rest errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB
