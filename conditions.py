print('conditions 1.')

num1 = 335
num2 = 66

if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num1} is not greater than {num2}")

print('\nconditions 2.')
number1 = 66
number2 = 66

if number1 > number2:
    print(f"{number1} is greater than {number2}")
elif number2 > number1:
    print(f"{number2} is greater than {number1}")
else:
    print(f"{number1} equals to {number2}")             #qn had wrong variables in condition

print('\nconditions 3.')

import random

number1 = random.randint(1,100)
number2 = random.randint(1,100)
print(f'number 1 is {number1}')
print(f'number 2 is {number2}')
if number1 > number2:
    print(f"{number1} is greater than {number2}")
elif number2 > number1:
    print(f"{number2} is greater than {number1}")
else:
    print(f"{number1} equals to {number2}")

# Compare the numbers to eachother

print('\nconditions 4.')
import random

x = random.randint(-100, 100)
print(f'x is {x}')
y = random.randint(-100, 100)
print(f'y is {y}')
if abs(x) > abs(y):
    print(f"The absolute value of {x} is greater than the absolute value  {y}")
elif abs(y) > abs(x):
        print(f"The absolute value of {y} is greater than the absolute value of {x}")
else:
    print(f"{x} equals to {y}")
                                            #compare absolute values

