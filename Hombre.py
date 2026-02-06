from Person import*

class Hombre(Person):
     """A derived class to define Man properties"""

     def speak(self, msg):
         print(self.name, ":\n\tHola!", msg)