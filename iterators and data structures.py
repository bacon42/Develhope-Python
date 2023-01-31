
print('iterators ex1.')

temp =('*')
count =0
while count < 5:
    print(temp)
    temp +="*"
    count+=1

print('\niterators ex2.')

temp =('*')
for x in range(3):
    print(temp)
    temp += "**"

print('\niterators ex3.')

todo = ["exercise1", "exercise2", "exercise3","coffee break" ,"exercise4","exercise5","exercise6"]
for x in todo:
    if x.upper() == "COFFEE BREAK":
        print(x)
        break

print('\niterators ex4.')

list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

print('list')
for x in list1:
    print (x)

print('\ntuple1')
for x in tuple1:
    print (x)

print('\nset1')
for x in set1:
    print (x)

print('\ndict1')
for i in dict1:
    if dict1[i] == 'land':
        print(i,' Lives on ',dict1[i])

print('\nData structures ex5.')

list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":4, "monkey":2, "dog":4,"fish":2}

print('list lenght is ',len(list1))
print('tuple lenght is ',len(tuple1))
print('set lenght is ',len(set1))
print('dictionary lenght is ',len(dict1))

print(list1[0])
print(tuple1[0])

for i in dict1.items():
    print('value of lion is ',i[1])
    break




