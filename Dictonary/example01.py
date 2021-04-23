cities = {101: "Pune", 102: "Mumbai", 105: "Delhi", 103: "Chennai"}

cities[104] = "Bengaluru"

# rename or replace
cities[103] = "Kolkata"

print(cities)
print()
print(cities.keys())
print()
print(cities.values())

# to get value of city
print(cities.get(103, "NIL"))

# if key not present return nil
print(cities.get(200, "NIL"))

# if present return true or else false
print(104 in cities)
print(109 in cities)

print()

for k in cities:
    print(cities[k])

print()

for cid, name in cities.items():
    print(cid, name)

print("length:", end=" ")
print(len(cities))
