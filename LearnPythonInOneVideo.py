# https://www.youtube.com/embed/N4mEzFDjqtA

'''
Data Types : Numbers, String, Lists, Tuples, Dictonaries
Airthmetic operators (7) : + - * / 
                        % (modules returns remainder of division)
                        ** (Exponent performs exponential (power) calculation on operator)
                        // (Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity))
                            9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0


Order of Execution for Airthmetic Operators : * / first before + - BODMAS
'''

grocery_list =['Juice','Tomatoes','Potatoes']
print('First Item', grocery_list[0])

pi_tuple = (3,1,4,1,5,9)
new_tuple = list(pi_tuple)
print(len(pi_tuple))
print('min: ',min(pi_tuple))
print('max: ', max(pi_tuple))

#Dictonaries
super_villains = {'Fiddler' : 'isaac Bowin',
'Captain Cold': 'Leonard Snart'}

print(super_villains['Captain Cold'])


age = 21
if age > 16 :
    print('your are old enough to drive')
else :
    print ('you are not old enough to drive')


def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum

print(addNumber(1,4))

class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name =  name
        self.__height = height
        self.__weight = weight
        self.__sound = sound


    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

cat = Animal('whiskers',33,10,'Meow')
print(cat.get_name)