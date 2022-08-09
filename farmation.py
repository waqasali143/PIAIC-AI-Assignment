
name = input("Enter Name: ")
father_name = input("Enter Father name: ")
gender = input("Enter Gender: ")
education = input("Enter Education: ")

# data = '''
# Name: {}
# Father Name: {}
# Gender: {}
# Education: {}

# '''.format(name,father_name,gender,education)
#                     or

data =f"""
Name:           {name}
Father Name:    {father_name}
Gender:         {gender}
Education:      {education}
"""
print(data)
