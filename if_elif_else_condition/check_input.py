# Write a python program to check if the input number is
# -real number
# -float number
# -string
# -complex number
# -Zero (0)
def check_user_input(input):
    try:
        val = int(input)
        print("Input is an integer = ", val)
    except ValueError:
        try:
            val = float(input)
            print("Input is a float = ", val)
        except ValueError:
            try:
                val = complex(input)
                print("Input is a complex =", val)
            except ValueError:
                try:
                    val = str(input)
                    print("Input is a string =", val)
                except ValueError:
                    print("Input is zero")


input1 = input("Enter float number:\n ")
check_user_input(input1)

input2 = input("Enter integer number:\n")
check_user_input(input2)

input2 = input("Enter string:\n")
check_user_input(input2)

input2 = input("Enter complex number [x+yi]:\n")
check_user_input(input2)