""" for i in range (151):
    print(i)

for i in range (5,1001,5):
    print (i) """
""" 
for i in range (1,101):
    print(i)
    if i % 5 == 0:
        print("Coding")
    if i % 10 == 0:
        print("Coding Dojo") """
""" 
sum=0

for i in range (0,101):
    if i % 2 !=0:
        sum += i
    print(sum) """

""" for i in range (2018, -1,-4):
    print(i)
 """
lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum+1):
    if i%mult == 0:
         print(i, '' , end= '')
## again in another for loop
# # this one below does NOT work because it assumes that the first low number is a mulitple multip which isn't always the case
 for i in range(lowNum, highNum, mult):
     print(i, '', end = '')
