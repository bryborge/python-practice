class Dog:
    # Class attributes
    species = "Canine familiaris"

    # Instance initialization
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Dunder method
    def __str__(self):
        return f"{self.name} is {self.age} years old."

    # Instance method
    def speak(self, sound) -> str:
        return f"{self.name} says {sound}."


class Malamute(Dog):
    pass


class CockerSpaniel(Dog):
    def speak(self, sound="Arf") -> str:
        return super().speak(sound)


class LabradorRetriever(Dog):
    def speak(self, sound="Woof") -> str:
        return super().speak(sound)
