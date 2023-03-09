class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, val):
        if 20 < val < 80:
            self._age = val
        else:
            raise ValueError('Age must be between 20 and 80')

    def display(self):
        print("I am", self.name)
    
    def greet(self):
        if self.age < 80:
            print("Hello, how are you doing?")
        else:
            print("Hello, how do you do?")
        self.display()

class Product:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def display(self):
        print(self._x, self._y) 

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, val):
        self._x = val

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, val):
        self._y = val

def main():

    p = Person('Nick', 79)
    p.age = 79
    print(p.age)

if __name__ == "__main__":
    main()