# sum of value in dictionary

# d = eval(input('Enter dictionary: '))
# s = sum(d.values())


# word = input('Enter any word: ')
# d = {}
# for x in word:
#     d[x] = d.get(x, 0)+1
# for k, v in d.items():
#     print(k, v)


# word = input('enter some word: ')
# d = {}
# vowels = ['a', 'e', 'i', 'o', 'u']
# for i in word:
#     if i in vowels:
#         d[i] = d.get(i, 0) + 1

# for k, v in d.items():
#     print(k, v)



n = int(input('enter the number of student: '))
d = {}
for i in range(n):
    name = input('Enter student name: ')
    marks = input('Enter student marks: ')
    d[name] = marks

while True:
    name = input('Enter student name to get marks: ')
    marks = d.get(name, -1)
    if marks == -1:
        print('student not found')
    else:
        print(f"the marks of {name} are {marks}")
    option = input('DO you want to find another studetn marks[yes/no]')
    if option == 'no':
        break
print('thanks for using our app')