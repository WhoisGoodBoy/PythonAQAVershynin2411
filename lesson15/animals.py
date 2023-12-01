import datetime

class Horse:
    attempts_to_call_nonexisting_parameters = []
    def __init__(self):
        self.age=5
        self.speed = 10

    def __getattr__(self, item):
        self.attempts_to_call_nonexisting_parameters.append(f'at {datetime.datetime.now()} sombody tried to call parameter: {item}')
        return f"it's okey that {item} doesn`t exist. some day, bro"

    def __eq__(self, other):
        return self.age == other.age

    def __add__(self, other):
        return Mul(self.speed, other.strength)

    def __del__(self):
        print('The horse is dead. Our thoughts and prayers')

    #def __radd__(self, other):
    #    return Mul(self.speed, other.strength)

class Donkey:
    def __init__(self):
        self.age=5
        self.strength = 11

    def __add__(self, other):
        return Mul(self.strength, other.speed)

    def __isub__(self, other):
        return self.strength + other.speed

    def __bool__(self):
        return True

    def __int__(self):
        return self.strength

class Mul:
    def __init__(self, speed, strength):
        self.speed = speed
        self.strength = strength


horse = Horse()
donkey = Donkey()
mul = horse + donkey
mul2 = donkey + horse
print(mul2)
horse2 = Horse()
del(horse2)
print(horse.speed)
print(horse == donkey)
print(bool(donkey))
print(int(donkey))
'''
print(horse.age)
print(horse.speed)
print(horse.strength)
print(horse.attempts_to_call_nonexisting_parameters)
'''