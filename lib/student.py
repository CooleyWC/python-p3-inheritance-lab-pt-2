import ipdb

class Student:
    def __init__(self):
        pass
    
    def hello(self, greeting="Hey there! I'm so excited to learn stuff."):
        print(greeting)

    def raise_hand(self):
        print("Pick me!")


class ChattyStudent(Student):
    def hello(self):
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")

    def raise_hand_dec(func):
        def wrapper(self):
            for x in range(10):
                func(self)
        return wrapper

    @raise_hand_dec
    def raise_hand(self):
        super().raise_hand()

