from abc import abstractmethod, ABCMeta

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass
    
class Dog(Animal):
    def do_say(self):
        print("멍멍!")
        
class Cat(Animal):
    def do_say(self):
        print("냐옹")
        
class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()
    
if __name__ == '__main__':
    ff = ForestFactory
    animal = input("어떤 동물의 소리를 낼까요? <Dog/Cat>")
    ff.make_sound(animal)