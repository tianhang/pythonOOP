class people:
    name = 'tianhang'     #public class property
    __sex = 'f'           #private class property

    def __init__(self,age):
        self.age = age           #instance property

    def getSex(self):            #public
        return self.__sex;

    @classmethod
    def getName(cls):
        return cls.name

    @classmethod
    def setName(cls,name):
        cls.name = name

    @staticmethod
    def getNameSex():
        return people.name +"--"+ people.__sex

p = people(12);

print p.name             #correct
print people.name        #correct
#print p.__sex           #error,instance object can not access the private class property
#print people.__sex      #error,class object can not access the private class property
#print people.getSex()   #error, cause need pass self as first params
print p.getSex()         #correct
print people.getName()
print p.getName()
people.setName("jack")
print p.getName()

print p.getNameSex()
print people.getNameSex()