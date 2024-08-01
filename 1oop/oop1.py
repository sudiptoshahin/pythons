

class Person:
    def __init__(self, fname, lname, age=30):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __str__(self):
        return f"{self.fname+' '+self.lname}({self.age})"
    
    def full_name(self):
        return f"{self.fname+' '+self.lname}"


# inheritance
class Customer(Person):
    """
    # To keep the inheritance of the parents __init__()
    function, add a cakk to the parents __init__ function

    """
    # def __init__(self, fname, lname):
    #     Person.__init__(self, fname, lname)
    # OR WE CAN USE AS FOLLOW:
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduate_year = 2019

    def __str__(self):
        return f"""Name: {self.full_name()}\nGraduate year: {self.graduate_year}"""
    

# Creating iterators
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self): 
        # stop the iteration
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
## Polymorphism
#---------------------
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("DRIVE!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("SAIL!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("FLY!")
#---------------------

## Interface
#---------------------
class InformalParserInterface:
    def load_data_source(self, path: str, filename: str) -> str:
        # load the file and extracting text
        pass

    def extract_text(self, abs_file_name: str) -> dict:
        # extract text from the currently loaded file.
        pass

class IVehicle:
    @abstractmethod
    def move(self):
        pass

class Vehicle(IVehicle):
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
    

class Car():
    def __init__(self, ) -> None:
        super().__init__()


#---------------------

if __name__ == '__main__':

    p1 = Person("Sudipto", "Shahin", 20)
    print(p1.fname)
    print(p1.age)
    print(f"\n String representation of p1 object\n{p1}")

    customer1 = Customer("Sudipto", "Shahin")
    print(customer1)
    print('-------------------')
    mytuple = (p1, customer1)
    tuple_iter = iter(mytuple)

    print(next(tuple_iter))
    print(next(tuple_iter))

    print(f"------iterator-----------")
    my_iter_class = MyNumbers()
    my_iter = iter(my_iter_class)
    for iter in my_iter:
        print(iter)
    # print(next(my_iter))
    # print(next(my_iter))
    # print(next(my_iter))
    # print(next(my_iter))



