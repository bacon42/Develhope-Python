print('\nfunctions 1.')

def byebye():
    print('goodbye')

byebye()

print('\nfunctions 2.')

def goodbye(name):
    print(f"Good bye {name}")

name= 'Adam'
goodbye(name)

print('\nfunctions 3.')

import os

user=os.getlogin()
print(user)


print('\nfunctions 4.')


name = ["Pete", "Sarah", "Hik","Cenk"]
surname = ["Peters", "Lindsay", "Huk","Seren"]

def greeting(name, surname):
    print(f"\nHello {name} {surname}!")

x=0
for i in name:
#   print(i)
    greeting(name[x], surname[x])
    x +=1

print('\nfunctions 5.')

import random

def random_list_summer():
    random_number=random.randint(-100,100)
    return random_number


randomList=[]
#x=0
for i in range(0,15):
   randomList.append(random_list_summer())
   total=sum(randomList)
print(f' {randomList}')
print(f'the sum is {total} ')






