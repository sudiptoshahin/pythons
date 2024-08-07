
"""
# Python datatypes
---------------------------
# str -> string
# int, float, complex -> numbers
# list, tuple, range
# mapping -> dict
# set -> set, frozenset
ex: x = frozenset({"apple", "banana", "cherry"})	
# bool -> True, False
# bytes, bytearray, memoryview
bytes -> ex: x = b"Hello"
bytearray -> x = bytearray(5)	
memoryview -> x = memoryview(bytes(5))
# None Type: NoneType
x = None
"""

"""
# Operators
=====================
* Arithmatic
-----------------------------
'+', '-', '*', '/', '%', '**'
'//' => floor division (the floor division // 
rounds the result down to the nearest whole 
number)
-----------------------------
* Assignment
-----------------------------
'=', '+=', '-=', '*=', '/=', '%=',
'//=', '**=', 
'&=' => [
* The binary representation of 5 is 101.
* The binary representation of 3 is 011.
* The bitwise AND operation compares each bit of 
** the two numbers and returns 1 only if both 
corresponding bits are 1. Otherwise, it returns 0.
]
'|=' => [
** The bitwise OR operation compares each bit of 
the two numbers and returns 1 if at least one 
of the corresponding bits is 1. If both bits 
are 0, it returns 0.
] ex: x=5 x |= 3 => 7

'^=' => [
** The ^= operator in Python is a bitwise XOR 
(exclusive OR) assignment operator.

** The bitwise XOR operation compares each bit of 
the two numbers and returns 1 if the corresponding 
bits are different (one is 1 and the other is 0). 
If both bits are the same (both 0 or both 1), 
it returns 0.
]

** '>>='
*** The >>= operator in Python is a right shift 
    assignment operator. It shifts the bits of 
    the left-hand operand to the right by the 
    number of positions specified by the 
    right-hand operand and assigns the result 
    back to the left-hand operand.
*** The binary representation of 5 is 101.
    The right shift operation shifts the bits to 
    the right by the specified number of 
    positions (in this case, 3). Each shift to 
    the right effectively divides the number by 
    2 and drops the rightmost bit.

ex: 
101 (binary for 5)
000 (binary result after shifting right by 3 positions)
x=5
x >>=3
result: 0

** '<<='
*** It shifts the bits of the left-hand operand 
    to the left by the number of positions specified 
    by the right-hand operand and assigns the 
    result back to the left-hand operand.

*** The left shift operation shifts the bits 
    to the left by the specified number of 
    positions (in this case, 3). Each shift to 
    the left effectively multiplies the number 
    by 2 and adds a zero bit on the right.
ex: 
101   (binary for 5)
101000   (binary result after shifting left by 3 positions)
x = 5
x <<= 3
result: 40

** ':='
*** The walrus operator allows you to assign a 
    value to a variable as part of an expression.

-----------------------------
* Comparison
-----------------------------
'==', '!=', '>', '<', '>=', '<='
-----------------------------
* Logical
-----------------------------
and, or, not
-----------------------------
* Identity
-----------------------------
is, is not
-----------------------------
* Membership
-----------------------------
in, not in
-----------------------------
* Bitwise
-----------------------------
&, |, ^, ~, <<, >>
-----------------------------
"""

"""
# Arrays
========================
* List is a collection which is ordered and 
  changeable. Allows duplicate members.
* Tuple is a collection which is ordered and 
  unchangeable. Allows duplicate members.
* Set is a collection which is unordered, 
  unchangeable*, and unindexed. No duplicate members.
* Dictionary is a collection which is ordered
  and changeable. No duplicate members.

  * While loop over the dictionaries as dict.items()
    this will returns tuple as a item

"""

"""
## Classes and Objects
--------------------------------
* Everything in python is an Object
* A Class is like an object constructor, or a 
  "blueprint" for creating objects.
* All classes have a function called '__init__' which
  is always executed when the is being initiated.
* '__str__' is function, which controls what should 
  be returned when the class object is represented
  as a string. Object function is called methods of 
  the class.
* self parameter is a reference to the current instance of 
  of the class.
------------------
# Inheritance
------------------
* To keep the inheritance of the parents __init__()
  function, add a call to the parents __init__ function.
  We can call it 2 ways
  ** ParentClass.__init__(self, params1, params2, params3)
  ** super().__init__(self, param1, params2, params3)

-------------------
# Polymorphism
-------------------
* Polymorphism means many forms, refers to methods/functions/operators
* 

"""

"""
## Iterators
----------------------------
* An iterator is an object that contains a countable number of values.
  Which means that we can traverse throuh all the values.
* Every strings in pythons is a iterators
* Iterator consists of '__iter__()' and '__next__()'
ex:
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

"""

"""
# JSON
-----------------------
* JSON is JavaScript Object Notations
* When we convert JSON to python it returns dict
* When we convert python object to JSON it returns a simple string

PyObject --> JSON
-------------------
* dict ----> Object
* list --> Array
* tuple --> Array
* str --> String
* int --> Number
* float --> Number
* True --> true
* False --> false
* None --> null
"""

"""
# Try Except
-----------------
* try block test a block of code for errors.
* except block handle the rror
* else block execute code when there is no error
* finally block execute code regardless of the result of 
  the try-and-except block


"""

# Strings common methods
#---------------------------
msg = "Hello, World"
print(msg.split(","))
print(msg.replace("H", "I"))

# Format strings
age = 20
price = 59
print(f'My name is John Doe and I\'m {age} years old.')
print(f'Price: {price:.2f}$')

# print octal value
txt = "\110\145\154\154\157"
print(f'Octal value: {txt}')

# show capitalize
a = 'capitalize'
print(a.capitalize())

# Tuples
# --------------------
thistuple = ("apple", "bananna", "kola", "cherry")
print(thistuple[1])

nottuple = ("apple")
print(type(nottuple))

thetuple = ("apple", )
print(type(thetuple))

y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

# unpacking tuple
(bananna, kola, cherry) = thistuple
print(bananna)
print(kola)
print(cherry)

# Sets
#-------------------------------
# Set is unordered, unchangable and unindexed
thisset = {"apple", "bananna", "cherry", "apple"}
print(thisset)
thisset.add("orange")
thisset.add(2)
print(thisset)

# Dict
person_obj = {
    "name": "Sudipto Shahin",
    "age": 20,
    "year": 1964,
    "dob": "1995/12/31",
    "year": 2022
}

print(person_obj["name"])
print(person_obj.get("year"))
print(type(person_obj.keys()))

# update dict
person_obj.update({ "age": 25 })
print(person_obj)

# remove specific key
person_obj.pop("dob")
# person_obj.clear()

# change dict_key to list
person_obj_keys = list(person_obj.keys())
print(person_obj_keys)
for key in person_obj_keys:
  print(f"{key} : {person_obj[key]}")


for person in person_obj.items():
  print(type(person))

# nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print('\nChildrens names: ')
childs = []
for (idx, child) in enumerate(myfamily.items()):
  childs.append(child[1]['name'])
  print(f"{idx+1} {child[1]['name']}")

# Short-hand if else
a = 2
b = 3
if a > b: print('a is grater than b')
print('b is grater than a') if a > b else print('a is grater than b')

for fruit in thistuple:
  if fruit == "kola":
    continue
  print(f'**{fruit}**')

# Functions
# Arbitrary Arguments, *args
def show_younget_child(*allChilds):
  print('The youngest child is '+ allChilds[2])


show_younget_child("childs1", "child2", "child3", "allChilds")
# print(childs)

# JSON
# --------------------------
import json

x = '{ "name":"John", "age":30, "city":"New York"}'
# parse json
x_json = json.loads(x) # returns a dict
print(type(x_json))

# python to json
py_json = json.dumps(x_json) # json is string type
print(type(py_json))