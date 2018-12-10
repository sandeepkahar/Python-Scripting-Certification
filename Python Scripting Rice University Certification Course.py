#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello, world!")


# In[2]:



# Unary + and -
print("Unary operators")
print(+3)
print(-5)
print(+7.86)
print(-3348.63)

print("")

# Simple arithmetic
print("Addition and Subtraction")
print(1 + 2)
print(48 - 89)
print(3.45 + 2.7)
print(87.3384 - 12.35)
print(3 + 6.7)
print(9.8 - 4)

print("")

print("Multiplication")
print(3 * 2)
print(7.8 * 27.54)
print(7 * 8.2)

print("")

print("Division")
print(8 / 2)
print(3 / 2)
print(7.538 / 14.3)
print(8 // 2)
print(3 // 2)
print(7.538 // 14.3)

print("")

print("Exponentiation")
print(3 ** 2)
print(5 ** 4)
print(32.6 ** 7)
print(9 ** 0.5)


# In[3]:


"""
Demonstration of compound arithmetic expressions in Python
"""

# Expressions can include multiple operations
print("Compound expressions")
print(3 + 5 + 7 + 27)
print(18 - 6 + 4)

print("")

# Operator precedence defines how expressions are evaluated
print("Operator precedence")
print(7 + 3 * 5)
print(5.5 * 6 // 2 + 8)
print(-3 ** 2)

print("")

# Use parentheses to change evaluation order
print("Grouping with parentheses")
print((7 + 3) * 5)
print(5.5 * ((6 // 2) + 8))
print((-3) ** 2)


# In[4]:


"""
Demonstration of the use of variables and how to assign values to
them.
"""

# The = operator can be used to assign values to variables
bakers_dozen = 12 + 1
temperature = 93

# Variables can be used as values and in expressions
print(temperature, bakers_dozen)
print("celsius:", (temperature - 32) * 5 / 9)
print("fahrenheit:", float(temperature))

# You can assign a different value to an existing variable
temperature = 26
print("new value:", temperature)

# Multiple variables can be used in arbitrary expressions
offset = 32
multiplier = 5.0 / 9.0
celsius = (temperature - offset) * multiplier
print("celsius value:", celsius)


# In[5]:


"""
Examples of common errors in Python
"""

# Remember you can use ctrl+k to comment a block of code and
# ctrl+shift+k to uncomment a block of code



# Syntax errors correspond to problems where your code doesn't follow the rules
# for writing valid Python programs.  Note that these errors arise
# before Python tries to run your code



print "To error is human, to forgive is divine"

# In Python 2, print was a statement and didn't need parentheses
# In Python 3, print is a function and its arguments should be enclosed in parentheses
# For those moving from Python 2 to Python 3, this syntax error will be extrememly common



#print("To error is human, to forgive is divine")

# As you enter expressions in Python, you will sometimes forget to include
# matching parentheses, quotations, brackets, etc.
      
# When you get a syntax error, always check whether you have matched up pairs correctly.
# Note that CodeSkulptor tries to help you with this task via coloring.  
# The right parenthesis is colored red to indicate an issue.



#print_quote = True
#if print_quote:
#    print("To error is human, to forgive is divine")
#else:
#    pass
#print_quote = False      
      
      
# Note that sometimes Python doesn't detect a syntax error until it's moved on to 
# processing the next line in your program.  If the line marked as having an error looks OK,
# be sure to check your previous line of code for problems.

# Here the previous else clause is missing its body.  Since Python requires each if-else 
# clause to have a body, we can insert a "pass" statement that does nothing.



# Syntax errors happen while Python is trying to parse your program into a recognizable form.
# A second class of errors happen while Python is running your code. Here are a few examples.

      
      
#pope_quote = "To error is human, to forgive is divine"
#print(pope_quote)

# Name errors corresponds to issues where Python is trying to find a value for one
# of the variables in your code and doesn' have one.  In that case, Python tells
# you that your variable is not defined.

# The most common cause of this error is misspelling a variable name.


#joe_ranking = 1
#print("Joe is number " + str(joe_ranking) + " coder.")

# Python loves to use the same operator on as many different types of data as possible.
# The + operator can be used to add numbers as well as add string (via concatenation)
# However, Python does know how to add a number and a string.  
# Here, Python threw a Type error to indicate this fact. 

# To fix this error, you can convert joe_ranking to a string using str().


# In[6]:


"""
Demonstration of how to call functions.
"""

# Function that we can call
def useless(input1, input2, input3):
    """
    This function takes three arguments and always returns 3.
    """
    return 3

# Calling the function
useless(1, 2, 3)

# Calling the function and printing the result
print(useless(4, 5, 6))

# Calling the function and assigning the result to a variable
result = useless(7, 8, 9)
print(result)

# You must pass the right number of arguments
# useless()
# useless(1)
# useless(1, 2)


# In[7]:


"""
Demonstration of defining functions.
"""

def sayhello():
    """
    Prints "hello".
    """
    print("hello")

# Call the function
sayhello()

def double(value):
    """
    Return twice the input value
    """
    return value * 2

# Call the function and assign the result to a variable
result = double(6)
print(result)

def product(value1, value2, value3):
    """
    Returns the product of the three input values.
    """
    prod = value1 * value2
    prod = prod * value3
    return prod

# Call the function and assign the result to a variable
result = product(7, 13.3, -1.2)
print(result)


# In[8]:


"""
Demonstration of parameters and variables within functions.
"""

def fahrenheit_to_celsius(fahrenheit):
    """
    Return celsius temperature that corresponds to fahrenheit
    temperature input.
    """
    offset = 32
    multiplier = 5 / 9
    celsius = (fahrenheit - offset) * multiplier
    print("inside function:", fahrenheit, offset, multiplier, celsius)
    return celsius

temperature = 95
converted = fahrenheit_to_celsius(temperature)
print("Fahrenheit temp:", temperature)
print("Celsius temp:", converted)

# Variables defined inside a function are local to that function
fahrenheit = 27
offset = 2
multiplier = 19
celsius = 77
print("before:", fahrenheit, offset, multiplier, celsius)
newtemp = fahrenheit_to_celsius(32)
print("after:", fahrenheit, offset, multiplier, celsius)
print("result:", newtemp)


# In[11]:


def future_value(present_value, annual_rate, periods_per_year, years):
    """
    Input: the numbers present_value, annual_rate, periods_per_year, years
    Output: future value based on formula given in question
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    return(present_value * ((1+rate_per_period) ** periods))
    # Put your code here. 
    

print("$1000 at 2% compounded daily for 4 years yields $", future_value(500,.04,10,10))


# In[12]:


"""
Demonstration of logical expressions.
"""

# Boolean values are True and False
value1 = True
value2 = False
print(value1, value2)

print("")

# Logical NOT
print("Logical NOT")
print("===========")
print(not value1)
print(not value2)

print("")

# Logical AND
print("Logical AND")
print("===========")
print(value1 and value1)
print(value1 and value2)
print(value2 and value2)

print("")

# Logical OR
print("Logical OR")
print("==========")
print(value1 or value1)
print(value1 or value2)
print(value2 or value2)

print("")

value3 = True
value4 = True

print(value2 or ((value1 and value4) or value3))


# In[13]:


"""
Demonstration of arithmetic comparisons
"""

# Six different arithmetic comparison operators
print("Comparisons")
print("===========")
print(7 > 3)
print(7 < 3)
print(7 >= 3)
print(7 <= 3)
print(7 == 3)
print(7 != 3)

print("")

# Using comparisons to get a boolean value
print("Comparing Variables")
print("===================")
num1 = 7.3
num2 = 8.6

greater = num1 > num2
print(greater)

print("")

# == and != are also useful for non-numeric types
print("Comparing Strings")
print("=================")
name = 'Scott'

# Beware of = and == confusion!
equal = name != "Joe"
print(equal)


# In[14]:


"""
Demonstration of if statements.
"""

def greet(friend, money):
    """
    Greet people.  Say hi if they are your friend and give them
    $20 if you have enough money.
    """
    if friend:
        print("Hi!")

    if money > 20:
        money = money - 20

    return money


money = 25

money = greet(False, money)
print("Money:", money)
print()

money = greet(True, money)
print("Money:", money)
print()

money = greet(True, money)
print("Money:", money)
print()


# In[15]:


"""
Demonstration of else and elif.
"""

def greet(friend, money):
    """
    Greet people.  Say hi if they are your friend.  Give them
    $20 if they are your friend and you have enough money.  Steal
    $10 from them if they are not your friend.
    """
    if friend and (money > 20):
        print("Hi!")
        money = money - 20
    elif friend:
        print("Hello")
    else:
        print("Ha ha!")
        money = money + 10
    return money


money = 15

money = greet(True, money)
print("Money:", money)
print()

money = greet(False, money)
print("Money:", money)
print()

money = greet(True, money)
print("Money:", money)
print()


# In[16]:


# Documentation https://py3.codeskulptor.org/docs.html#style


# In[1]:


# Strings are enclosed in quotes
name = 'Scott Rixner'
university = "Rice"

print(name)
print(university)

# Multiline strings use triple quotes
address = '''Rice University
Houston, TX
'''

# First Fig by Edna St. Vincent Millay
poem = """My candle burns at both ends;
  It will not last the night;
But ah, my foes, and oh, my friends---
  It gives a lovely light!
"""

print("")

print("Address")
print("=======")
print(address)

print("First Fig")
print("=========")
print(poem)


# Characters
chars = "abc'DEF*&$"
print(chars)
chars2 = '\t"abc"\ndef\''
print(chars2)

# String "arithmetic"
print("Concatenating strings")
name_and_uni = name + " " + university
print(name_and_uni)

print("")
print("")
print("Repeating strings")
lots_o_rice = university * 4
print(lots_o_rice)

# Using str
num = 3.87
strnum = str(num)
print("number: " + strnum)
# print("number: " + num)


# In[2]:


## String Indexing


# In[3]:


"""
String indexing examples.
"""

phrase = "Python is great!"

# first character
print(phrase[0])

# fourth character
fourth = phrase[3]
print(fourth)
print(type(phrase))
print(type(fourth))

# length of string
phraselen = len(phrase)
print(phraselen)

# last character
print(phrase[phraselen - 1])
print(phrase[-1])

# thirteenth from last (fourth) character
print(phrase[-13])

# Out of bounds
#print(phrase[phraselen])
#print(phrase[-20])

# Indices
# string = "abcde"
# character   a  b  c  d  e
# pos index   0  1  2  3  4
# neg index  -5 -4 -3 -2 -1


# In[4]:


## Searching String


# In[5]:


"""
String searching examples.
"""

sentence = "When I tell you pick up the " +            "left rock, it will be the " +            "right one, and then only " +            "the right rock will be left."

# Finding strings within strings
print("Finding lefts")
firstleft = sentence.find("left")
print(firstleft, sentence[firstleft])
lastleft = sentence.rfind("left")
print(lastleft, sentence[lastleft])

print("")
print("Finding rights")
firstright = sentence.index("right")
print(firstright, sentence[firstright])
lastright = sentence.rindex("right")
print(lastright, sentence[lastright])

print("")
print("Finding Rixner")
firstrixner1 = sentence.find("Rixner")
print(firstrixner1)
# firstrixner2 = sentence.index("Rixner")
# print(firstrixner2)

# Counting strings within strings
print("")
print("Counting substrings")
print("Number of lefts:", sentence.count("left"))
print("Number of apples:", sentence.count("apple"))

# Checking start/ends
print("")
print(sentence.startswith("When"))
print(sentence.endswith("The end."))


# In[6]:


### String Slicing


# In[7]:


"""
Slicing strings.
"""

word = "everything"

# Selecting substrings
print(word[1:5])
print(word[5:9])

# Open ended slices
print(word[5:])
print(word[:4])

# Using negative indices
print(word[-3:])
print(word[2:-3])

# Indexing past the end
print(word[8:20])
print("$" + word[22:29] + "^")

# Empty slices
print(word[6:6])
print(word[4:2])


# In[8]:


## Formatting String


# In[9]:


country = "France"
capital = "Paris"
sentence = "The capital of {} is {}.".format(country, capital)
print(sentence)

mood1 = "happy"
mood2 = "sad"
sentence1 = "I feel {0}, do you feel {0}?  Or are you {1}? I'm not sure if we should be {0}.".format(mood1, mood2)
print(sentence1)

name1 = "Pierre"
age1 = 7
name2 = "May"
age2 = 13

line1 = "{0:^7} {1:>3}".format(name1, age1)
line2 = "{0:^7} {1:>3}".format(name2, age2)
print(line1)
print(line2)

num = 3.283663293
output = "{0:>10.3f} {0:.2f}".format(num)
print(output)


# In[ ]:


# DICTIONARY


# In[1]:


"""
Dictionary creation.
"""

print("Dictionary Literals")
print("===================")

# Dictionary literals
empty = {}
print(empty)

simple = {1: 2}
print(simple)

squares = {1: 1, 2: 4, 3: 9, 4: 16}
print(squares)

cipher = {'p': 'o', 'y': 'h', 't': 'n',
          'h': 't', 'o': 'y', 'n': 'p'} 
print(cipher)

goodinstructors = {'Rixner': True, 'Warren': False}
print(goodinstructors)

cities = {'China': ['Shanghai', 'Beijing'],
          'USA': ['New York', 'Los Angeles'],
          'Spain': ['Madrid', 'Barcelona'],
          'Australia': ['Sydney', 'Melbourne'],
          'Texas': ['Houston', 'San Antonio']}
print(cities)

print("")
print("Creating Dictionaries")
print("=====================")

empty2 = dict()
print(empty2)

data = [(1, 'one'), (2, 'two'), (3, 'three')]
names = dict(data)
print(names)

cipher2 = dict(cipher)
print(cipher2)


# In[2]:


# DICTIONARY LOOKUPS AND UPDATES


# In[3]:


"""
Dictionary lookup and update.
"""


print("Dictionary Lookup")
print("=================")

cipher = {'p': 'o', 'y': 'h', 't': 'n',
          'h': 't', 'o': 'y', 'n': 'p'} 
print(cipher)

# Use indexing with keys to access values
print(cipher['t'])
print(cipher['n'])

def encrypt(cipher, word):
    """encrypt word using cipher"""
    encrypted = ""
    for char in word:
        encrypted += cipher[char]
    return encrypted

python = "python"
enc = encrypt(cipher, python)
print(python, enc)

# It is an error to use a non-existent key
# print(cipher[1])

# Use .get when you are unsure if the key exists
print(cipher.get('t'))
print(cipher.get(1))
print(cipher.get(1, 'z'))

print("")
print("Dictionary Update")
print("=================")

print(cipher)

# Modify an existing key->value mapping
cipher['p'] = 'q'
print(cipher)

# Create a new key->value mapping
cipher['r'] = 'z'
print(cipher)

enc2 = encrypt(cipher, python)
print(python, enc, enc2)


# In[4]:


# Checking Keys in a dictionary 


# In[5]:


"""
Checking for keys in a dictionary.
"""

print("Using 'in'")
print("==========")

mapping = {1: 5, 8: -3, 7: 22, 4: 13, 22: 17}

# Keys
print(1 in mapping)
print(8 in mapping)

# Values
print(5 in mapping)
print(-3 in mapping)

# Both
print(22 in mapping)

# Neither
print(82 in mapping)

print("")

print("Protecting from Errors")
print("======================")

keys = [8, 14, 22, 25]

#for key in keys:
#    print(key, mapping[key])

for key in keys:
    if key in mapping:
        print(key, mapping[key])
    else:
        print("{} not in mapping".format(key))


print("Issues with Keys")
print("================")
        
# Be careful with what you use as keys!
# If all keys are of the same type, you won't run
#  into these issues
mapping = {4.0: 2, 'a': 3, True: 'true', False: 9}
print(mapping)

mapping[1] = 7
print(mapping)

mapping[0] = 'false'
print(mapping)

mapping[4] = 7
print(mapping)

mapping['A'] = 'abc'
print(mapping)


# In[6]:


# Handling Dictionary Errors


# In[8]:


"""
Example code for working with dictionary keys
"""

# Three example of dictionaries - note that dictionary keys in Python must be immutable
simple_dict = {"Joe" : 1, "Scott" : 2, "John" : 3}
##print(simple_dict)

#bad_dict = {["Joe", "Warren"] : 1, ["Scott", "Rixner"] : 2, ["John", "Greiner"] : 3}
#print(bad_dict)

good_dict = {("Joe", "Warren") : 1, ("Scott", "Rixner") : 2, ("John", "Greiner") : 3}
#print(good_dict)


# Examples of dictionary lookup
#print(simple_dict["Joe"])
#print(simple_dict["Scott"])
#print(simple_dict["Stephen"])
#print(good_dict[("Joe", "Warren")])
#print(good_dict[("John", "Greiner")])




# Custom code for looking up keys that may not always be present

def lookup(my_dict, my_key, default_value=None):
    """
    Given dictionary my_dict and key my_key, 
    return my_dict[my_key] if my_key is in my_dict
    otherwise return default_value
    """
    if my_key in my_dict:
        return my_dict[my_key]
    else:
        return default_value

simple_dict = {"Joe" : 1, "Scott" : 2, "John" : 3}
print(lookup(simple_dict, "Joe", -1))
print(lookup(simple_dict, "Stephen", -1))
print(lookup(simple_dict, "Stephen"))







# In[ ]:




