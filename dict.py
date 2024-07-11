# d = {}

# d[100] = 'durga'
# d[200] = 'ravi'
# d[300] = 'shiva'
# print(d)



# d = {100: 'durga', 200: 'ravi', 300: 'shiva'}
# print(d[100])
# print(d[300])



# rec = {}
# n = int(input('Enter number of student: '))
# i = 1
# while i <= n:
#     name = input('Enter student name: ')
#     marks = input('enter percentage of marks of student: ')
#     rec[name] = marks
#     i = i + 1
# print('name of student', '\t', "pecentage of student")
# for x in rec:
#     print('\t', x , "\t\t", rec[x])



# d = {100: 'durga', 200: 'ravi', 300: 'shiva'}
# print(d)
# d[400] = 'mama'
# print(d)
# d[200] = 'khan'
# print(d)


# del d[400]
# print(d)

# d.clear()
# print(d)



# d = {100: 'durga', 200: 'ravi', 300:'shiva'}
# print(d.get(100))
# print(d.get(400, 'guest'))


# d = {100: 'durga', 200: 'ravi', 300: 'ravi'}
# print(d)
# print(d.pop(100))
# print(d.popitem())
# print(d)

# d = {100: 'durga', 200: 'ravi', 300: 'shiva'}
# print(d.keys)
# for k in d.keys():
#     print(k)


# d = {100: 'durga', 200: 'ravi', 300: 'shiva'}
# print(d.values())
# for k in d.values():
#     print(k)


d = {100: 'durga', 200: 'ravi', 300: 'shiva'}
print(d)
for k, v in d.items():
    print(k, v)


    