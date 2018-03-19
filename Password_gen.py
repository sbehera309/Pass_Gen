import random
import string

def password_gen (size = 8, chars = string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))
                   
print(password_gen(int(input('How many characters are in your password?'))))