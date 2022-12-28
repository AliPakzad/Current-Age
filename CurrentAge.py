from datetime import date

try:
    my_birth_date = input().split('/')
    my_birth_date = list(map(int, my_birth_date))
    birth_date = date(my_birth_date[0], my_birth_date[1], my_birth_date[2])
    age = date.today().year - birth_date.year
    print(age)
    
except ValueError:
    print('WRONG')

except TypeError:
    print('WRONG')

"""
if my_birth_date[1] >12 or my_birth_date[2] >31:
    print('WRONG')
else:
    birth_date = date(my_birth_date[0], my_birth_date[1], my_birth_date[2])
    age = date.today().year - birth_date.year
    print(age)
"""
