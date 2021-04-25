import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

if re.search(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

print(re.findall(pattern, "eggspamsausagespam"))

# The function re.finditer does the same thing as re.findall,
# except it returns an iterator, rather than a list.


match = re.search(pattern, "eggspamsausagespam")

if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

str = "My name is David. Hi David"
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)

pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1")
if re.match(pattern, "gray"):
    print("Match 2")
if re.match(pattern, "blue"):
    print("Match 3")

patt = r"^gr.y$"

if re.match(patt, "grey"):
    print("Match 1")
if re.match(patt, "gray"):
    print("Match 2")
if re.match(patt, "stringray"):
    print("Match 3")
if re.match(patt, "groy"):
    print("Match 4")
if re.match(patt, "greatday"):
    print("Match 5")

patt = r"[aeiou]"
print()
if re.search(patt, "grey"):
    print("Match 1")
if re.search(patt, "qwertyuiop"):
    print("Match 2")
if re.search(patt, "rhythm myths"):
    print("Match 3")
if re.search(patt, "aeiou"):
    print("Match 4")
if re.search(patt, "greatday"):
    print("Match 5")
# The pattern [aeiou] in the search function matches all strings that contain any one of the characters defined.

patt = r"[A-Z][a-z][0-9]"
print()
if re.search(patt, "Ls8"):
    print("Match 1")
if re.search(patt, "sl9"):
    print("Match 2")
if re.search(patt, "sss"):
    print("Match 3")
if re.search(patt, "aeiou"):
    print("Match 4")
if re.search(patt, "greatday"):
    print("Match 5")

patt = r"[^A-Z]"
print()
if re.search(patt, "this is all quiet"):
    print("Match 1")
if re.search(patt, "sl9"):
    print("Match 2")
if re.search(patt, "sss"):
    print("Match 3")
if re.search(patt, "ABC"):
    print("Match 4")
if re.search(patt, "999"):
    print("Match 5")

# The pattern [^A-Z] excludes uppercase strings.
# Note, that the ^ should be inside the brackets to invert the character class.


pattern = r"egg(spam)*"  # The example above matches strings that start with "egg" and follow with zero or more "spam"s.

print()
if re.match(pattern, "egg"):
    print("Match 1")
if re.match(pattern, "eggspamspamegg"):
    print("Match 2")
if re.match(pattern, "blue"):
    print("Match 3")
if re.match(pattern, "spam"):
    print("Match 4")

pattern = r"g+"

print()
if re.match(pattern, "grey"):
    print("Match 1")
if re.match(pattern, "gray"):
    print("Match 2")
if re.match(pattern, "gggggggggg"):
    print("Match 3")
if re.match(pattern, "GGGGGGGggggggggg"):
    print("Match 4")
if re.match(pattern, "GGGGGGGG"):
    print("Match 5")
if re.match(pattern, "abc"):
    print("Match 6")

# To summarize:
# * matches 0 or more occurrences of the preceding expression.
# + matches 1 or more occurrence of the preceding expression.

pattern = r"ice(-)?cream"

print()
if re.match(pattern, "ice-cream"):
    print("Match 1")
if re.match(pattern, "icecream"):
    print("Match 2")
if re.match(pattern, "gggggggggg"):
    print("Match 3")
if re.match(pattern, "sausages"):
    print("Match 4")
if re.match(pattern, "ice--ice"):
    print("Match 5")
if re.match(pattern, "abc"):
    print("Match 6")

# The metacharacter ? means "zero or one repetitions".

pattern = r"9(1,3)$"

print()
if re.match(pattern, "9"):
    print("Match 1")
if re.match(pattern, "999"):
    print("Match 2")
if re.match(pattern, "9999"):
    print("Match 3")
if re.match(pattern, "1111"):
    print("Match 4")
if re.match(pattern, "0000"):
    print("Match 5")
if re.match(pattern, " 9"):
    print("Match 6")
# "9{1,3}$" matches string that have 1 to 3 nines.


pattern = r"egg(spam)*"

print()
if re.match(pattern, "egg"):
    print("Match 1")
if re.match(pattern, "eggspamspamegg"):
    print("Match 2")
if re.match(pattern, "blue"):
    print("Match 3")
if re.match(pattern, "spam"):
    print("Match 4")

# (spam) represents a group in the example pattern shown above.

pattern = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern, "abcdefghijklmnop")
print()
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group())

# The content of groups in a match can be accessed using the group function.
# A call of group(0) or group() returns the whole match.
# A call of group(n), where n is greater than 0, returns the nth group from the left.
# The method groups() returns all groups up from 1.

print()
pat = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pat, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())

pat = r"gr(a|e)y"
print()
match = re.match(pat, "gray")
if match:
    print("Match 1")

match = re.match(pat, "grey")
if match:
    print("Match 2")

match = re.match(pat, "griy")
if match:
    print("Match 3")

pat = r"(.+)\1"
print()
match = re.match(pat, "wordword")
if match:
    print("Match 1")

match = re.match(pat, "?| ?|")
if match:
    print("Match 2")

match = re.match(pat, "abc cde")
if match:
    print("Match 3")

pat = r"(\D+\d)"  # (\D+\d) matches one or more non-digits followed by a digit.
print()
match = re.match(pat, "Hi 999!")
if match:
    print("Match 1")

match = re.match(pat, "1, 23, 456!")
if match:
    print("Match 2")

match = re.match(pat, " ! $?")
if match:
    print("Match 3")

match = re.match(pat, " ! 77")
if match:
    print("Match 4")

match = re.match(pat, "$777")
if match:
    print("Match 5")

"""

Additional special sequences are \A, \Z, and \b.
The sequences \A and \Z match the beginning and end of a string, respectively.
The sequence \b matches the empty string between \w and \W characters, or \w characters and the beginning or end of the string. Informally, it represents the boundary between words.
The sequence \B matches the empty string anywhere else.

"""

pattern = r"\b(cat)\b"  # \b(cat)\b" basically matches the word "cat" surrounded by word boundaries.
print()
match = re.search(pattern, "The cat sat!")
if match:
    print("Match 1")

match = re.search(pat, "We s>cat<tered?")
if match:
    print("Match 2")

match = re.search(pat, "We scattered.")
if match:
    print("Match 3")

match = re.search(pattern, " cat ")
if match:
    print("Match 4")

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@sololearn.com for assitance"

match = re.search(pattern, str)
if match:
    print(match.group())

# [\w\.-]+ matches one or more word character, dot or dash.
# The regex above says that the string should contain a word (with dots and dashes allowed), followed by the @ sign,
# then another similar word, then a dot and another word.

import re

# your code goes here
x = input()

# pattern  = r"[1|8|9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"
# validate phone no
pattern = r"1|8|9{1}[0-9]"

match = re.match(pattern, x)
if match and len(x) == 8:
    print("Valid")
else:
    print("Invalid")
