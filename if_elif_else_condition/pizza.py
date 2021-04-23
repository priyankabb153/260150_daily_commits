# Write Python code that asks a user how many pizza slices they want.
# The pizzeria charges Rs 123.00 a slice.
# if user order even number of slices, price per slice is Rs 120.00.
# Print the total price depending on how many slices user order

n = int(input("Enter the number of slices you want "))
if n % 2 == 0:
    print("Total price : "+str(n*120))
else:
    print("Total price : " + str(n * 123))