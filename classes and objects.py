print(f'classes and objects ex.1 and 2')
class Animal:
    def __init__(self, leg_count):
        self.leg_count = leg_count
        print('Animal object was created')

    def runs(self):
        print('Running started')

    def count_the_legs(self):
        print(f'Animal has : {self.leg_count} legs')

    def return_the_legs(self):
        return self.leg_count


a = Animal(4)
a.count_the_legs()
a.return_the_legs()
a.leg_count
a.runs()


print(f'\nclasses and objects ex.3')
class Animal:
    def __init__(self, leg_count):
        self._leg_count = leg_count
        print('Animal object was created')

    def runs(self):
        print('Running started')

    def count_the_legs(self):
        print(f'Animal has : {self._leg_count} legs')

    def return_the_legs(self):
        return self._leg_count


a = Animal(4)
a.count_the_legs()
a.return_the_legs()


print(f'\nclasses and objects ex.3')

class Animal:
    def __init__(self, legs_count):
        print('Animal object was created')
        self._number_of_legs = legs_count

    def runs(self):
        print('Running started')

    def count_legs(self):
        print(f'Animal has {self._number_of_legs} legs')

    def return_legs(self):
        return self._number_of_legs

    def bark(self):
        print('woof woof')


animal1 = Animal(4)
animal1.count_legs()

setattr(animal1, 'name', 'Dougie')
print(animal1.name)
animal1.bark()
