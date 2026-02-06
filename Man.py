from Person import*
class Man(Person):
    """A derived class to describe Man properties"""

    def speak(self, msg):
        print(self.name, ":\n\tHello!", msg)
