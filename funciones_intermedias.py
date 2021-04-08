""" import random
def randInt(min = 0,max = 100):
    num = random.random()*100
    return num
print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
 """