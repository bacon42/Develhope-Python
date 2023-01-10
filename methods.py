print('methods 1.')

print(type("Hello World"))
print(type(True))
print(type(False))
print(type(33))
print(type(24.5))
print(type(4+1j))
print(type(4j))
print(type(["lion", "monkey", "dog","fish"]))
print(type(("lion", "monkey", "dog","fish")))
print(type({"name" : "John", "surname" : "Doe", "age":22}))
print(type({"lion", "monkey", "dog","fish"}))

print('methods 2.')

num1 = float(1.3)
print('floating point number',num1)

num2 = int(2.3)
print('integer',num2)

num3 = complex(1j)
print('complex number',num3)

num4 =round(1.4)
print('rounded number',num4)

num5 = 1.5
num5 =round(num5)
print('rounded number',num5)

print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))
print(type(num5))

print('methods 3.')
num1 = 1122334455666
num1_str = str(num1)    #convert int to string
print(num1_str)         #print string
print(len(num1_str))    #string length
print(num1_str[2])      #string element
print(num1_str[2:5])    #string slicing
print(str(num2) in num1_str)   #is 2 in the string, convert num2 to string first
print(str(num3) in num1_str)   #is complex number 1j in the string, convert num3 to string first

string_with_0 ='0'+num1_str
print(string_with_0)        #left concatenate
print(string_with_0[0:4])        # print first 4 elements
print(string_with_0[4:])        #elements after first 4
print(string_with_0[-4:-2])     #negative indexing to '56'





