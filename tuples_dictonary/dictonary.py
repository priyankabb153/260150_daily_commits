"""
This means that a dictionary is a set of key-value pairs. Note:

each key must be unique - it's not possible to have more than one key of the same value;
a key may be any immutable type of object: it can be a number (integer or float), or even a string, but not a list;
a dictionary is not a list - a list contains a set of numbered values, while a dictionary holds pairs of values;
the len() function works for dictionaries, too - it returns the numbers of key-value elements in the dictionary;
a dictionary is a one-way tool - if you have an English-French dictionary, you can look for French equivalents of
 English terms, but not vice versa.

"""

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)
# stores its data is completely out of your control,

print(dictionary['cat'])
print(phone_numbers['Suzy'])

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

print()

for key in dictionary.keys():
    print(key, "->", dictionary[key])

print()
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])

print()
for english, french in dictionary.items():
    print(english, "->", french)

print()
for french in dictionary.values():
    print(french)

dictionary['cat'] = 'minou'
print(dictionary)

dictionary['swan'] = 'cygne'
print(dictionary)

dictionary.update({"duck": "canard"})
print(dictionary)

# removal of the associated value.
# Values cannot exist without their keys.

del dictionary['dog']
print(dictionary)

#  removing a non-existing key causes an error.

# To remove the last item in a dictionary,
# you can use the popitem() method:


dictionary.popitem()
print(dictionary)

#  popitem() method removes a random item from a dictionary.

"""
1. Dictionaries are unordered*, changeable (mutable), 
and indexed collections of data. (*In Python 3.6x dictionaries have become ordered by default.


"""

# To add or remove a key (and the associated value), use the following syntax:

phonebook = {}    # an empty dictionary

phonebook["Adam"] = 3456783958    # create/add a key-value pair
print(phonebook)    # outputs: {'Adam': 3456783958}

del phonebook["Adam"]
print(phonebook)    # outputs: {}

pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

print(len(pol_eng_dictionary))    # outputs: 3
del pol_eng_dictionary["zamek"]    # remove an item
print(len(pol_eng_dictionary))    # outputs: 2

pol_eng_dictionary.clear()   # removes all the items
print(len(pol_eng_dictionary))    # outputs: 0

del pol_eng_dictionary    # removes the dictionary


# To copy a dictionary, use the copy() method:

pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

copy_dictionary = pol_eng_dictionary.copy()

# Write a program that will "glue" the two dictionaries (d1 and d2)
# together and create a new one (d3).

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

# Write a program that will convert the colors tuple to a dictionary.

colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)


