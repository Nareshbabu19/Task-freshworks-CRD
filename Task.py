import time
data = {}

def create(key, value, t_out = 0):
    if key in data:
        print("Key Already Exists")
    else:
        if(alpha(key)):
            if(len(data) < (1069547520) and value <= (16777216)):
                if (t_out == 0):
                    limit = [value, t_out]
                else:
                    limit = [value, (time.time() + t_out )]
                if (len(key) <= 32):
                    data[key] = limit
            else:
                print("Memory limit exceeded !!")
        else:
            print("Key name must contain only alphabets no number's and special charecter ")

def read(key):
    if key not in data:
        print("Given key dose not exist in database enter valid key")
    else:
        temp = data[key]
        if(temp[1] != 0):
            if (time.time() < temp[1]):
                srt = str(key) + ":" + str(temp[0])
                return(srt)
            else:
                print("Time to live in ",key,"has expired")
        else:
            srt = str(key) + ":" + str(temp[0])
            return(srt)
def delete(key):
    if key not in data:
        print("Given key does not exist in database. Please enter a valid key") 
    else:
        b=data[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del data[key]
                print("key is successfully deleted")
            else:
                print("Time to live in",key,"has expired") 
        else:
            del data[key]
            print("key is successfully deleted")


def update(key,value):
    temp = data[key]
    if temp[1]!= 0:
        if time.time()<temp[1]:
            if key not in data:
                print("Given key does not exist in database. Please enter a valid key")
            else:
                limit=[]
                limit.append(value)
                limit.append(temp[1])
                data[key]=limit
        else:
            print("Time to live in",key,"has expired")
    else:
        if key not in data:
            print("Given key does not exist in database. Please enter a valid key")
        else:
            limit=[]
            limit.append(value)
            limit.append(temp[1])
            data[key]=limit

def print_data():
    return("Database in file: ",data)
     
def alpha(key):
    a = "abcdefghijklmnopqrstuvwxyz"
    A = "QWERTYUIOPLKJHGFDSAZXCVBNM"
    for i in key:
        if((i not in a) and (i not in A) ):
            return(False)
    return(True)