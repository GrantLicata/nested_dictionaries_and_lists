# 1 -- Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'

# Change the value 20 in z to 30
z[0]['y'] = 30

# Validation
print(x)
print(students)
print(sports_directory)
print(z)


# 2 -- Iterate Through a List of Dictionaries

# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.
def iterateDictionary(list):
    for dic in list:
        for key in dic.keys():
            print(key)
        for val in dic.values():
            print(val)

# Validation
stuff = [
    {'w': 'wombat', 'm': 'mellon'},
    {'q': 'quality', 'l': 'llama'}
]
iterateDictionary(stuff)

# 3 -- Get Values From a List of Dictionaries

# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.
def iterateDictionary2(key_name, some_list):
    for dic in some_list:
        for key_name in dic.keys():
            print(key_name)

# Validation
stuff = [
    {'w': 'wombat', 'm': 'mellon'},
    {'w': 'worm', 'l': 'llama'}
]
iterateDictionary2('w', stuff)

# 4 -- Iterate Through a Dictionary with List Values

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. 
def printInfo(some_dict):
    for key in some_dict:
        count = len(some_dict[key])
        print(f"{key} {count}")
        for i in some_dict[key]:
            print(i)

# Validation
dojo = {
    'locations': ['moon', 'mars', 'europa', 'saturn'],
    'instructors': ['Michael', 'Amy', 'Eduardo']
}
printInfo(dojo)

