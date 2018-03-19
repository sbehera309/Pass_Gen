import random
import string

def password_gen (size = 8, chars = string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))
                   
print(password_gen(int(input('How many characters are in your password?'))))







from array import *

decimalarray = array('i', [12,13,14])
    
decimalarray.insert(3, 25)


for x in decimalarray:
    if x == 14 :
        print("the data in this index is 14")
    else:
        print("The data is not 14")