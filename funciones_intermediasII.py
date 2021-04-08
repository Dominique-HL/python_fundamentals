""" 
1.Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
2.Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
3.En el directorio sports_directory, cambia 'Messi' a 'Andres'
4.Cambia el valor 20 en z a 30 """

""" x = [ [5,2,3], [10,8,9] ] 
x [1][0] = 15
print(x) """
""" 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students) """

""" sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory ['soccer'][0] = 'Andres'
 """
""" z = [ {'x': 10, 'y': 20} ]
z [0]['y'] = 30
print(z) """


""" students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionarycopy(some_list):
    stringReturn = ''
    for val in some_list:
        stringReturn += f"first_name - {val['first_name']}, last_name - {val['last_name']}\n"
    return stringReturn
iterateDictionarycopy(students) """

""" students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary2(key_name, some_list):
    stringReturn = ''
    for val in some_list:
        stringReturn += f"{val[key_name]}\n"
    return stringReturn
print(iterateDictionary2('first_name',students))
print(iterateDictionary2('last_name',students))
 """

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
""" def printInfo(my_dictionary):
    for key in my_dictionary:
        print(f"{len(my_dictionary[key])} {key.upper()}")
        for val in my_dictionary[key]:
            print(val)
        print("")
printInfo(dojo) """
