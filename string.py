# name = 'durga'
# print(name[0])
# print(name[4])
# print(name[-1])


# name = input('Enter some string: ')
# i = 0
# for x in name:
#     print(f"the charater present at positive index {i} and at negative index {i-len(name)} is {x}")
#     i = i + 1



# s = 'learning python is very easy!'
# print(s[1:8])
# print(s[::-1])




# s = 'learning python is very easy!'
# n = len(s)
# i = 0
# print('forward direction')
# while i < n:
#     print(s[i], end='')
#     i += 1
# print()
# print('backward direction')
# i = -1
# while i >= -n:
#     print(s[i], end='')
#     i = i-1



# s = input('enter main string: ')
# subs = input('enter sub string: ')
# if subs in s:
#     print(subs, 'is found in main string')
# else:
#     print('substtring is not found in the string')



# s1 = input('Enter first string: ')
# s2 = input('enter second string: ')
# if s1 == s2:
#     print('both string are equal')
# elif s1 < s2:
#     print('first string is less than the second string')
# else:
#     print('first string is greater than second string.')



# city = input('Enter your city name: ')
# scity = city.strip()
# if scity == 'Hyderabad':
#     print('hello hyderabadi.. adab')
# elif scity == 'Chennai':
#     print('hello madrasi..vanakkam')
# elif scity == 'Banglore':
#     print('hello kannadiga..shubhodaya')
# else:
#     print('your entered city is invalid')




# s = input('Enter main string: ')
# subs = input('Enter sub string: ')
# flag = False
# pos = -1
# n = len(s)
# while True:
#     pos = s.find(subs,pos+1, n)
#     if pos == -1:
#         break
#     print('found at position', pos)
#     flag = True
# if flag == False:
#     print('not found')




# s = input('Enter any charater: ')
# if s.isalnum():
#     print('alpha numeric character')
#     if s.isalpha():
#         print('alpba charater')
#         if s.islower():
#             print('lower case alphabet charater')
#         else:
#             print('upper case alphabet charter')
#     else:
#         print('it is a digit')
# elif s.isspace():
#     print('it is space charater')
# else:
#     print('non space specail charater')



s = input('Enter some string: ')
print(s[::-1])

