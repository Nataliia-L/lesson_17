# Переписать игру Угадай число с помощью механизма исключений. 
# В коде указан пример, как создавать собственные исключения

import random

class ValueTooBig(ValueError):
    pass

class ValueTooSmall(ValueError):
    pass

gener_number = random.randint (1,99)
print ('Gener: ', gener_number)
user_number = 0

    
while user_number!=gener_number:
    user_number = int(input ('Попробуйте еще: '))
    try:
        user_number = int(user_number)
        if user_number<gener_number:
            raise ValueTooSmall
    except:
        print ('Your number is too small. Try again.') 
    else:
        print ('Your number is too big. Try again.')

 
if user_number == gener_number:
    print ('Congrats!')
