
## SHELL

- from terminal type `python` and prompt goes to >>>
- type `exit()`
- it will be 2.7 but if you do it within the virtual env of the django project it will be 3.6


## PYTHON 101 CRASH COURSE

- I'm coming from a javascript perspective
- a list is an array
- a tuple is an immutable array
- a dictionary is an object
- an ordered dict is a collection
- https://pyfiddle.io/


```
listOfNumbers = [1,2,3,4,5,6]           # a python list is an array 
print(listOfNumbers[1])                 # bracket notation to retreive 2nd element
print(len(listOfNumbers))               # gets length of the python list
print(listOfNumbers[:3])                # subset or slice, returns everything before index 3
print(listOfNumbers[3:])                # subset or slice, returns everything after and including index 3
print(listOfNumbers[-1:])               # get last element
listOfNumbers.extend([10,20])           # adds two more elements
listOfNumbers.append(9)                 # adds one more elements
listOfNumbers.sort(reverse=True)        # will sort, also works on alpha
for number in listOfNumbers:
    print(number)
    if (number % 2 == 0):
        print("is even")
    else:
        print("is odd")
print("All done.")
mytuple = (1,2,3,4,5,6)                 # tuple is an immutable list, use parenthesis not []
(x,y) = "abc,def".split(",")            # similar to JS reverse object shorthand assignment
stuff = {}                              # dictionaries, keys with spaces, no dot notation
stuff = {"name" : "gary"} 
stuff["a a"] = "hello"                  # assign new key
print(stuff.get("a a"))                 # retreive value
print(stuff["a a"])                     # retreive value
for k in stuff:
    print(k)
    print(stuff[k])
def SquareIt(x):                        # function definition
    return x * x
print(SquareIt(5))
def Process(f, v):                      # like javascript function pointers can be passed
    return f(v)
print(Process(SquareIt, 10))
print(Process(lambda x: x-2, 10))       # use key word lambda to create an anonymous function
                                        # in python sometimes referred to as inline function
print(1==3)                             # yields boolean False with a capital F
print(1 is 3)                           # same
if 1 is 3:                              # clunky if elif else
    print("wtf")
elif 1 > 3:
    print("yikes")
else:
    print("whew")
for x in range(10):                     # range evaluates to an array or maybe its a tuple
    if x is 1:
        continue                        # continue means skip this iteration
    if x > 5:
        break                           # break means stop looping
    print(x)
x = 0
while (x < 10):
    print(x)
    x += 1
```
