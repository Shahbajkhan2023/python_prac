# f = open('abcd.txt', 'w')
# f.write('durga\n')
# f.write('Software\n')
# f.write('Solution\n')
# print('Data written in the file successfully')
# f.close()


# f = open('abcd.txt', 'w')
# list = ['sunny\n', 'bunny\n', 'vinny\n', 'chinny']
# f.writelines(list)
# print('List of lines written to the file successfully')
# f.close()




with open('abcd.txt', 'w') as f:
    f.write('Durga\n')
    f.write('Software\n')
    f.write('Solution\n')
    print('is file closed', f.closed)
print('is file closed', f.closed)