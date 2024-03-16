import re

# def printNames(file_path):
#     with open(file_path, 'r') as file: 
#         data = file.read()
#         pattern = r'Name: (\w+),'
#         names = re.findall(pattern, data)
#         for name in names:
#             print(name)


file_path = 'C:\Users\User\Documents\PP2\Practice\Lab5\re.txt'

file = open(file_path, 'r')
data = file.read()

pattern = r'Name: (\w+),'
names = re.findall(pattern, data)
for name in names:
    print(name)



# printNames(file_path)

