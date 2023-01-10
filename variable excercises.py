print('\nEx 1. ')
firstName = 'Mario'
print(firstName)

print('\nEx 2. ')
age = '25'
print(age)
# as formatted string literal
print(f'{age}')

print('\nEx 3. ')
sentence =('Hello, i\'m {}!'.format(firstName))
print (sentence)

print('\nEx 4. ')
amount = 63.772
print(amount)
print(type(amount))

print('\nEx 5. ')
a=True
b=True
c=True
print(type(a),type(b),type(c))
print(a and b)

print('\nEx 6. ')

#  1my-first2_Name = 'Mario' remove illegal chars
my_first2_Name = 'Mario'
print (my_first2_Name)
# removed leading 1 and changed hyphen to underscore
# invalid decimal literal - variables can't start with a decimal
# hyphen is an operator for a math expression

print('\nEx 7. ')
# unclear exactly what this exercise is after but ...

print ("Hi,\nmy name is\nJohn Doe")
print("python")

print('\nEx 8. ')
x=3
y=4
z=5
print(x, y, z)

print('\nEx 9. ')
a = 12
b = 'Hello'
print(a, b)
print('\nswapping variable values\n ')
temp =a
a=b
b=temp
print(a, b)

print('\nEx 10. ')
hello = 'Hello!'
name = 'Jhon Doe'
age = '40'

print (len(hello))
print (len(name))
print (len(age))

print('\nEx 11. ')
#capitalise
a = 'hello'
print (a.capitalize())

#uppercase
b='tom'
print (b.upper())

#lowercase
c='LAURA'
print (c.lower())

#change
question = 'How are you'
fixd=question.replace("o", "e")
print (fixd)

#string for each word
age_question = 'How old are you?'

x = age_question.split(" ")
print(x)
print(x[0])
print(x[1])
print(x[2])
print(x[3])

print(a,b,c,question,age_question)

print('\nEx 12. ')

hello = {'name':'Daniel', 'age':'32'}
print('hello {name}. you are {age}.'.format(**hello))








