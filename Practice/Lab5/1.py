import re 

# data = """
# Name: John Doe, Year: 1985, Gender: Male
# Name: Emily Smith, Year: 1990, Gender: Female
# Name: Michael Johnson, Year: 1978, Gender: Male
# Name: Sarah Brown, Year: 2001, Gender: Female
# Name: David Miller, Year: 1995, Gender: Male
# Name: Jessica Lee, Year: 1982, Gender: Female
# Name: Christopher Wilson, Year: 1973, Gender: Male
# Name: Olivia Davis, Year: 2000, Gender: Female
# Name: Matthew Taylor, Year: 1992, Gender: Male
# Name: Sophia Martinez, Year: 1988, Gender: Female
# Name: Daniel Clark, Year: 1976, Gender: Male
# Name: Chloe Rodriguez, Year: 1997, Gender: Female
# Name: Joshua Hernandez, Year: 1983, Gender: Male
# Name: Isabella Gonzalez, Year: 2005, Gender: Female
# Name: Ethan White, Year: 1979, Gender: Male
# Name: Ava Anderson, Year: 1993, Gender: Female
# Name: Alexander Wilson, Year: 1969, Gender: Male
# Name: Madison Taylor, Year: 2002, Gender: Female
# Name: Benjamin Thomas, Year: 1987, Gender: Male
# Name: Victoria Moore, Year: 1971, Gender: Female
# """

def print_names(file_path):
    with open(file_path, 'r') as file: 
        data = file.read()
        pattern = r'Name: (\w+),'
        names = re.findall(pattern, data)
        for name in names:
            print(name)

file_path = 're.txt'

print_names(file_path)



# Регулярное выражение для поиска имен
# pattern = r'Gender: ([\w\s]+),'
pattern = r'Gender: (\w+)'

# Используем re.findall для нахождения всех совпадений с шаблоном в данных
names = re.findall(pattern, data)

# Выводим найденные имена
for name in names:
    print(name)








# import re

# # Function to extract names from a text file using regular expressions
# def extract_names(file_path):
#     with open(file_path, 'r') as file:
#         # Read the content of the file
#         data = file.read()
#         # Regular expression pattern to find names
#         pattern = r'Name: ([\w\s]+),'
#         # Using re.findall to find all matches with the pattern in the data
#         names = re.findall(pattern, data)
#         # Printing the extracted names
#         for name in names:
#             print(name)

# # Path to the text file containing the data
# file_path = 'data.txt'

# # Calling the function to extract names from the file
# extract_names(file_path)




# file handling
 
# # 1) without using with statement
# file = open('file_path', 'w')
# file.write('hello world !')
# file.close()
 
# # 2) without using with statement
# file = open('file_path', 'w')
# try:
#     file.write('hello world')
# finally:
#     file.close()
    

# using with statement
# with open('file_path', 'w') as file:
# 	file.write('hello world !')
