#Author __vap0r__
#PasswordGenerator

import random
import string

def randomPassword():
    randomCriteria = string.ascii_letters + string.digits + string.punctuation

    password = random.sample(randomCriteria,16)
    password += random.sample(string.ascii_uppercase,2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ' '.join(passwordList)
    return password

print('Password gen:',randomPassword())
