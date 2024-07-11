# list = []
# for i in range(101):
#     if i%10 == 0:
#         list.append(i)
# print(list)



# n = [1, 2, 3, 4]
# n.insert(10, 777)
# n.insert(1, 888)
# print(n)



# order1 = ['chicken', 'mutton', 'fish']
# order2 = ['rc', 'kf', 'fo']
# order1.extend(order2)
# print(order1)



# a = [10, 20, 30, 40]
# a.remove(10)
# a.remove(20)
# print(a)



# l = [1, 2, 3, 4, 5]
# l.pop()
# print(l)
# l.pop(1)
# print(l)



# n = [10, 20, 30, 40]
# n.reverse()
# print(n)


# n = [20, 5, 15, 10, 0]
# n.sort()
# print(n)





# a = [10, 20, 30]
# b = [40, 50, 60]
# c = a + b
# print(c)



# x = [10, 20, 30]
# y = x * 3
# print(y)






# n = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# print(n)
# for r in n:
#     print(r)


# for i in range(len(n)):
#     for j in range(len(n[i])):
#             print(n[i][j])
#     print()




# s = [x*x for x in range(1, 11)]
# print(s)


# v = [2**x for x in range(1, 6)]
# print(v)

# m = [x for x in s if x % 2 == 0]
# print(m)



# words = ['balaiah', 'nag', 'venkatesh', 'chiranjeevi']
# l = [w[0] for w in words]
# print(l)




vowels = ['a', 'e', 'i', 'o', 'u']
word = input('enter the word to search for vowels: ')
found = []
for leter in word:
    if leter in vowels:
        if leter not in found :
            found.append(leter)
print(found)

