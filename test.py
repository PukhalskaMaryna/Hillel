# інкапсуляція, наслідування, поліморфізм та абстракція
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def introduce(self):
#         return f"Hi, my name is {self.name}, I'm {self.age}"

# p = Person("Mary",41)
# p2 = Person("Max",40)
# print (p.introduce())
# print (p2.introduce())

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self._balance = balance