""" #1
def big_size(array):
    for i in range(len(array)):
        if array[i]>0:
            array[i]='big'
    return array
print(big_size([-1,3,5,-5]))
 """

""" #2
def count_positives(array):
    count = 0
    for val in array:
        if val > 0:
            count += 1
    array[len(array)-1] = count
    return array
print(count_positives([-1,1,1,1])) """

""" #3
def sum_total(array):
    sum=0
    for val in array:
        sum+= val
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))
 """
""" 
 #4
def avg(array):
    sum=0
    for val in array:
        sum+= val
    return(sum/len(array))
print(avg([1,2,3,4]))


 """
""" #5
def length_return(array):
    return len(array)
print(length_return([37,2,1,9]))
print(length_return([]))
 """

"""  #6
def minValue(array):
    if len(array)<=0:
        return False
    min = array[0]
    for val in array:
        if val<min:
            min = val
    return min
print(minValue([37,2,1,-9]))
print(minValue([])) """

""" #7
def maxValue(array):
    if len(array)<=0:
        return False
    max = array[0]
    for val in array:
        if val>max:
            max = val
    return max
print(maxValue([37,2,1,-9]))
print(maxValue([])) """

""" #8
def ultimate_analysis(array):
    myDictionary = {'sumTotal': 0, 'promedio': 0, 'minimo': array[0], 'maximo': array[0], 'longitud': len(array)}
    for val in array:
        if myDictionary['minimo']>val:
            myDictionary['minimo'] = val
        if myDictionary['maximo']<val:
            myDictionary['maximo'] = val
        myDictionary['sumTotal']+= val
        myDictionary['promedio']=myDictionary['sumTotal']/len(array)
    return myDictionary
print(ultimate_analysis([37,2,1,-9])) """

""" #9
def reverse_list(array):
    for i in range (0, (len(array)-1)//2):
        temp = array[i]
        array[i] = array[len(array)-1-i]
        array[len(array)-1-i] = temp
    return array
print(reverse_list([37,2,1,-9])) """