# інкапсуляція, наслідування, поліморфізм та абстракція

# Інкапсуляція — це об’єднання атрибутів і методів всередині класу, 
# яке запобігає доступу зовнішніх класів до атрибутів і методів даного класу та їх зміні. 
# Іншими словами, це “приховування даних”.
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def introduce(self):
#         return f"Hi, my name is {self.name}, I'm {self.age}"

# p = Person("Mary",41)
# p2 = Person("Max",40)
# # print (p.introduce())
# # print (p2.introduce())

# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.__balance = balance

#     def depos(self,amount):
#         if amount > 0:
#             self.__balance += amount
#             return f'Done, + {amount}, bal {self.__balance}'
#         return f'Negative summ'
    
#     def withdraw(self,amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             return f'Done, - {amount}, bal {self.__balance}'
#         return f'No many'
    
#     def get_balance(self):
#         return f'Bal: {self.__balance}'
    
# acc = BankAccount(p.name,1000)    
# print(acc.get_balance())
# print(acc.depos(500))
# print(acc.depos(500))
# print(acc.withdraw(500))

# acc.__balance += 10000

# acc._BankAccount__balance += 10000
# acc.get_balance
#     @property
#     def bal(self):
#         return self.__balance
    
#     @bal.setter
#     def bal(self,amount):
#          if amount > 0:
#             self.__balance += amount

# acc = BankAccount(p.name,1000) 
# print(acc.bal)
# acc.bal = 1000000000
# print(acc.bal)


# наслідування

class Animal:
    def __init__(self, name = 'Any'):
        self.name = name

    def make_sound(self):
        return f'some sound - {self.name}' 

class Dog(Animal):
    def __init__(self,breed,name = 'Any dog'):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        return f'{self.name} says GAU! Breed {self.breed}'
    
d = Dog(breed = 'Mops')
a = Animal("Bonny")
print(d.make_sound())
print(a.make_sound())