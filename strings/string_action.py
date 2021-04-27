# string compare
# Both comparisons give True as a result:

print('alpha' == 'alpha')
print('alpha' != 'Alpha')

# longer string is considered greater.

print('alpha' < 'alphabet')

# upper-case letters are taken as lesser than lower-case
print('beta' > 'Beta')

print('10' == '010')
print('10' > '010')
print('10' > '8')
print('20' < '8')
print('20' < '80')

# Sorting
# Demonstrating the sorted() function: this returns new list
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()

# Demonstrating the sort() method: here sort is applied and reflected in same list
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)

# number to string
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)

# reverse transformation
si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
print(s2)
s3 = sorted(s2)
print(s3)
print(s3[1])
