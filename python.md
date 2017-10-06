# EXAM: Programming Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Create a `.gitignore` file so generated files won't be committed
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
- You can use any resource online, but **please work individually**
- **Don't just copy-paste** your answers and solutions, use your own words instead.
- **Don't push your work** to GitHub until your mentor announces that the time is up


# Tasks
## 1-3. Complete the following tasks: (~90 mins)
- [Uniques Characters](uniquechars/unique_chars.py)
- [Favourite Animals](favouriteanimals/favourite_animals.py)
- [Candy Shop](candyshop/candy_shop.py)

### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- The solution follows [styleguide](https://google.github.io/styleguide/pyguide.html) [1p]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently with descriptive commit messages [1p]

## 4. Question time! (~10 mins) [4p]

###  What is the difference between a function and a method? [2p]
#### Your answer:

A function: organized, reusable code that is used to perform a single, related action. It is useful, becouse it provides better modularity for your application and a high degree of code reusing. Optionally it can return with values. Python has a lot of built-in functions like print(), and can also create my own functions. 
Define a functions (it is important to name it by it's functionality): - use def to it

def print_out_some_stufs():
    print("Some stuff")

you can call it with: print_out_some_stuff()

Method:
Methods are members of classes in OO programing. A method is a function that takes a class instance as its first parameter. 
A method is able to operate on data that is contained within the class.

Example:
class Example(object):
    def method(self, other, arguments):
        pass

### What is the constructor? When it is used? [2p]
#### Your answer:

constructor or initialization method
The first method in a class: is __init__() This special method is the constructor. Python calls it when we create a new instance of the class.

Example: 
def __init__(self, argument):
      self.ex = ex
      self.argument = argument

