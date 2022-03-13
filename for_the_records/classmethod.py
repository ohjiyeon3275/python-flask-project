class test:
    pet = "dog"

    @classmethod
    def dog(self):
        return self.pet
    
    @classmethod
    def doggy(doggy):
        return doggy.pet

    @classmethod
    def getA(cls, a):
        return a


class cat(test):
    pet = "cat"


print(test.dog())
print(test.doggy())
print(test.getA("iguana")) #iguana
print(cat.pet) #cat