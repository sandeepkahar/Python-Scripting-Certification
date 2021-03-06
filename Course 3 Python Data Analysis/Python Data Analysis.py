#!/usr/bin/env python
# coding: utf-8

# In[1]:


# DICTIONARY


# In[2]:


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


# In[3]:


# DICTIONARY LOOKUPS AND UPDATES


# In[4]:


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


# In[5]:


# Checking Keys in a dictionary 


# In[6]:


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


# In[7]:


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




