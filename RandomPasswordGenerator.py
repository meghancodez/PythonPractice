# Random Password Generator 10/13/2022

import random, string

def password(length, num=False, strength='weak'):
    """length of password, num if you want a number,
    and strength (weak, strong, very)"""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    letter = lower + upper
    dig = string.digits
    punct = string.punctuation
    pwd = ''
    if strength == 'weak':
        if num:
            length -= 2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(lower)

    elif strength == 'strong':
        if num:
            length -=2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(letter)
    elif strength == 'very':
        ran = random.randint(2,4)
        if num:
            
        
    pwd = list(pwd)   
    random.shuffle(pwd)
    return ''.join(pwd)
            

print(password(5,num=True))

print(password(10,num=True, strength = 'strong'))

