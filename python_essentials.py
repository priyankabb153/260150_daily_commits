print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print("I like \"Monty Python\"")

print(True > False)
print(True < False)
print("\"I'm\"")
print("\"\"learning\"\"")
print("\"\"\"Python\"\"\"")

"""
Most of Python's operators have left-sided binding, which means that the calculation of the expression is conducted from left to right.

This simple example will show you how it works. Take a look:

print(9 % 6 % 2)


There are two possible ways of evaluating this expression:

from left to right: first 9 % 6 gives 3, and then 3 % 2 gives 1;
from right to left: first 6 % 2 gives 0, and then 9 % 0 causes a fatal error.

Run the example and see what you get.

The result should be 1. This operator has left-sided binding. But there's one interesting exception.

the exponentiation operator uses right-sided binding.
"""

"""
Key takeaways
1. An expression is a combination of values (or variables, operators, calls to functions - you will learn about them soon) which evaluates to a value, e.g., 1 + 2.

2. Operators are special symbols or keywords which are able to operate on the values and perform (mathematical) operations, e.g., the * operator multiplies two values: x * y.

3. Arithmetic operators in Python: + (addition), - (subtraction), * (multiplication), / (classic division - always returns a float), % (modulus - divides left operand by right operand and returns the remainder of the operation, e.g., 5 % 2 = 1), ** (exponentiation - left operand raised to the power of right operand, e.g., 2 ** 3 = 2 * 2 * 2 = 8), // (floor/integer division - returns a number resulting from division, but rounded down to the nearest whole number, e.g., 3 // 2.0 = 1.0)

4. A unary operator is an operator with only one operand, e.g., -1, or +3.

5. A binary operator is an operator with two operands, e.g., 4 + 5, or 12 % 5.

6. Some operators act before others - the hierarchy of priorities:

unary + and - have the highest priority
then: **, then: *, /, and %, and then the lowest priority: binary + and -.
7. Subexpressions in parentheses are always calculated first, e.g., 15 - 1 * (5 * (1 + 2)) = 0.

8. The exponentiation operator uses right-sided binding, e.g., 2 ** 2 ** 3 = 256.

Keywords
Take a look at the list of words that play a very special role in every Python program.

['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
   'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
   
   
   
   
   
Priority	        Operator	
1	+, -	        unary
2	**	
3	*, /, //, %	
4	+, -	        binary
5	<, <=, >, >=	
6	==, !=


3. The while and for loops can also have an else clause in Python. 
The else clause executes after the loop finishes its execution as long as it has not been terminated by break



 programming 
BACK
MODULE 1: INTRODUCTION TO PYTHON AND COMPUTER PROGRAMMING
1.1. Introduction to programming with Python 
BACK
1.1. INTRODUCTION TO PROGRAMMING WITH PYTHON
1.1.1.0 Python Essentials 1 - Module 1
1.1.1.1 Programming - absolute basics
1.1.1.2 Programming - absolute basics
1.1.1.3 Programming - absolute basics
1.1.1.4 Programming - absolute basics | Compilation vs. interpretation
1.1.1.5 Programming - absolute basics | Compilation vs. interpretation
1.1.1.6 Programming - absolute basics | Compilation vs. interpretation
1.1.2.1 Python - a tool, not a reptile
1.1.2.2 Python - a tool, not a reptile
1.1.2.3 Python - a tool, not a reptile | Why Python?
1.1.2.4 Python - a tool, not a reptile | Why Python, why not?
1.1.3.1 Python 2 vs. Python 3
1.1.3.2 There is more than one Python: CPython and Cython
1.1.3.3 There is more than one Python: Jython, PyPy, and RPython
1.2. Downloading and installing Python 
BACK
1.2. DOWNLOADING AND INSTALLING PYTHON
1.2.1.1 Begin your Python journey
1.2.1.2 Begin your Python journey | Downloading and installing Python
1.2.1.3 Begin your Python journey
1.2.1.4 Begin your Python journey
1.2.1.5 Begin your Python journey
1.2.1.6 Begin your Python journey
1.2.1.7 Begin your Python journey
1.2.1.8 Begin your Python journey
1.2.1.9 Module Completion
Module 1 Quiz Quiz 
BACK
MODULE 1 QUIZ
1.3.1.1 PE1 -- Module 1 Quiz Quiz
Module 2: Data types, variables, basic I/O operations, and basic operators 
BACK
MODULE 2: DATA TYPES, VARIABLES, BASIC I/O OPERATIONS, AND BASIC OPERATORS
2.1. Hello, world! 
BACK
2.1. HELLO, WORLD!
2.1.1.0 Python Essentials 1: Module 2
2.1.1.1 Your very first program
2.1.1.2 Your first program
2.1.1.3 Your first program
2.1.1.4 Your first program
2.1.1.5 Your first program
2.1.1.6 LAB: The print() function Lab
2.1.1.7 Your first program
2.1.1.8 Your very first program
2.1.1.9 Your very first program
2.1.1.10 Your very first program
2.1.1.11 Your very first program
2.1.1.12 Your very first program
2.1.1.13 Your very first program
2.1.1.14 Your very first program
2.1.1.15 Your very first program
2.1.1.16 Your very first program
2.1.1.17 Your very first program
2.1.1.18 LAB: The print() function Lab
2.1.1.19 LAB: Formatting the output Lab
2.1.1.20 SECTION SUMMARY
2.2. Python literals 
BACK
2.2. PYTHON LITERALS
2.2.1.1 Python literals
2.2.1.2 Python literals
2.2.1.3 Python literals
2.2.1.4 Python literals
2.2.1.5 Python literals
2.2.1.6 Python literals
2.2.1.7 Python literals
2.2.1.8 Python literals
2.2.1.9 Python literals
2.2.1.10 Python literals
2.2.1.11 LAB: Python literals - strings Lab
2.2.1.12 SECTION SUMMARY
2.3. Arithmetic operators and the hierarchy of priorities 
BACK
2.3. ARITHMETIC OPERATORS AND THE HIERARCHY OF PRIORITIES
2.3.1.1 Operators - data manipulation tools
2.3.1.2 Operators - data manipulation tools
2.3.1.3 Operators - data manipulation tools
2.3.1.4 Operators - data manipulation tools
2.3.1.5 Operators - data manipulation tools
2.3.1.6 Operators - data manipulation tools
2.3.1.7 Operators - data manipulation tools
2.3.1.8 Operators - data manipulation tools
2.3.1.9 Operators - data manipulation tools
2.3.1.10 SECTION SUMMARY
2.4. Variables 
BACK
2.4. VARIABLES
2.4.1.1 Variables - data-shaped boxes
2.4.1.2 Variables - data-shaped boxes
2.4.1.3 Variables - data-shaped boxes
2.4.1.4 Variables - data-shaped boxes
2.4.1.5 Variables - data-shaped boxes
2.4.1.6 Variables - data-shaped boxes
2.4.1.7 LAB: Variables Lab
2.4.1.8 Variables - data-shaped boxes
2.4.1.9 LAB: Variables: a simple converter Lab
2.4.1.10 LAB: Operators and expressions Lab
2.4.1.11 SECTION SUMMARY
2.5. Comments 
BACK
2.5. COMMENTS
2.5.1.1 A comment on comments
2.5.1.2 LAB: Comments Lab
2.5.1.3 SECTION SUMMARY
2.6. The input() function and string operators 
BACK
2.6. THE INPUT() FUNCTION AND STRING OPERATORS
2.6.1.1 How to talk to a computer
2.6.1.2 How to talk to a computer
2.6.1.3 How to talk to a computer
2.6.1.4 How to talk to a computer
2.6.1.5 How to talk to a computer
2.6.1.6 How to talk to a computer: string operators
2.6.1.7 How to talk to a computer: string operators
2.6.1.8 How to talk to a computer: string operators
2.6.1.9 LAB: Simple input and output Lab
2.6.1.10 LAB: Operators and expressions Lab
2.6.1.11 LAB: Operators and expressions Lab
2.6.1.12 SECTION SUMMARY
2.6.1.13 Module Completion
Module 2 Quiz Quiz 
BACK
MODULE 2 QUIZ
2.7.1.1 PE1 -- Module 2 Quiz Quiz
Module 3: Boolean values, conditional execution, loops, lists and list processing, logical and bitwise operations Now 
BACK
MODULE 3: BOOLEAN VALUES, CONDITIONAL EXECUTION, LOOPS, LISTS AND LIST PROCESSING, LOGICAL AND BITWISE OPERATIONS
3.1. Comparison operators and conditional execution 
BACK
3.1. COMPARISON OPERATORS AND CONDITIONAL EXECUTION
3.1.1.0 Python Essentials 1: Module 3
3.1.1.1 Making decisions in Python
3.1.1.2 Making decisions in Python
3.1.1.3 Making decisions in Python
3.1.1.4 LAB: Questions and answers Lab
3.1.1.5 Making decisions in Python
3.1.1.6 Making decisions in Python
3.1.1.7 Making decisions in Python
3.1.1.8 Making decisions in Python
3.1.1.9 Making decisions in Python
3.1.1.10 LAB: Comparison operators and conditional execution Lab
3.1.1.11 LAB: Essentials of the if-else statement Lab
3.1.1.12 LAB: Essentials of the if-elif-else statement Lab
3.1.1.13 SECTION SUMMARY (1/2)
3.1.1.14 SECTION SUMMARY (2/2)
3.2. Loops 
BACK
3.2. LOOPS
3.2.1.1 Loops in Python | while
3.2.1.2 Loops in Python | while
3.2.1.3 LAB: Essentials of the while loop - Guess the secret number Lab
3.2.1.4 Loops in Python | for
3.2.1.5 Loops in Python | for
3.2.1.6 LAB: Essentials of the for loop - counting mississippily Lab
3.2.1.7 Loop control in Python | break and continue
3.2.1.8 Loop control in Python | break and continue
3.2.1.9 LAB: The break statement - Stuck in a loop Lab
3.2.1.10 LAB: The continue statement - the Ugly Vowel Eater Lab
3.2.1.11 LAB: The continue statement - the Pretty Vowel Eater Lab
3.2.1.12 Python loops | else
3.2.1.13 Python loops | else
3.2.1.14 LAB: Essentials of the while loop Lab
3.2.1.15 LAB: Collatz's hypothesis Lab
3.2.1.16 SECTION SUMMARY (1/2)
3.2.1.17 SECTION SUMMARY (2/2)
3.3. Logic and bit operations in Python Now 
BACK
3.3. LOGIC AND BIT OPERATIONS IN PYTHON
3.3.1.1 Logic and bit operations in Python | and, or, not
3.3.1.2 Logic and bit operations in Python | and, or, not
3.3.1.3 Logic and bit operations in Python
3.3.1.4 Logic and bit operations in Python | Bitwise operators
3.3.1.5 Logic and bit operations in Python | Bit shifting Now
3.3.1.6 SECTION SUMMARY
3.4. Lists 
BACK
3.4. LISTS
3.4.1.1 Lists - collections of data
3.4.1.2 Lists - collections of data | Indexing
3.4.1.3 Lists - collections of data | Indexing
3.4.1.4 Lists - collections of data | Operations on lists
3.4.1.5 Lists - collections of data | Operations on lists
3.4.1.6 LAB: The basics of lists Lab
3.4.1.7 Lists - collections of data | Functions and methods
3.4.1.8 Lists - collections of data | list methods
3.4.1.9 Lists - collections of data | list methods
3.4.1.10 Lists - collections of data | lists and loops
3.4.1.11 Lists - collections of data | lists and loops
3.4.1.12 Lists - collections of data | lists and loops
3.4.1.13 LAB: The basics of lists - the Beatles Lab
3.4.1.14 SECTION SUMMARY
3.5. Sorting simple lists 
BACK
3.5. SORTING SIMPLE LISTS
3.5.1.1 Sorting simple lists - the bubble sort algorithm
3.5.1.2 Sorting simple lists - the bubble sort algorithm
3.5.1.3 Sorting simple lists - the bubble sort algorithm
3.5.1.4 SECTION SUMMARY
3.6. List processing 
BACK
3.6. LIST PROCESSING
3.6.1.1 Operations on lists
3.6.1.2 Operations on lists | slices
3.6.1.3 Operations on lists | slices
3.6.1.4 Operations on lists | slices
3.6.1.5 Operations on lists | slices, del
3.6.1.6 Operations on lists | in, not in
3.6.1.7 Lists - more details
3.6.1.8 Lists - more details
3.6.1.9 LAB: Operating with lists - basics Lab
3.6.1.10 SECTION SUMMARY
3.7.1 Multidimensional arrays 
BACK
3.7.1 MULTIDIMENSIONAL ARRAYS
3.7.1.1 Lists in advanced applications
3.7.1.2 Lists in advanced applications | Arrays
3.7.1.3 Lists in advanced applications | Arrays
3.7.1.4 Lists in advanced applications | Arrays
3.7.1.5 Lists in advanced applications | Arrays
3.7.1.6 SECTION SUMMARY
3.7.1.7 Module Completion
Module 3 Quiz Quiz 
BACK
MODULE 3 QUIZ
3.8.1.1 PE1 -- Module 3 Quiz Quiz
Module 4: Functions, tuples, dictionaries, and data processing 
BACK
MODULE 4: FUNCTIONS, TUPLES, DICTIONARIES, AND DATA PROCESSING
4.1. Functions 
BACK
4.1. FUNCTIONS
4.1.1.0 Python Essentials 1: Module 4
4.1.1.1 Functions
4.1.1.2 Functions
4.1.1.3 Writing functions
4.1.1.4 Writing functions
4.1.1.5 Functions
4.1.1.6 SECTION SUMMARY
4.2. Function parameters and argument passing 
BACK
4.2. FUNCTION PARAMETERS AND ARGUMENT PASSING
4.2.1.1 How functions communicate with their environment
4.2.1.2 How functions communicate with their environment
4.2.1.3 How functions communicate with their environment
4.2.1.4 How functions communicate with their environment
4.2.1.5 How functions communicate with their environment
4.2.1.6 How functions communicate with their environment
4.2.1.7 How functions communicate with their environment
4.2.1.8 SECTION SUMMARY
4.3. Returning results from functions 
BACK
4.3. RETURNING RESULTS FROM FUNCTIONS
4.3.1.1 Returning a result from a function
4.3.1.2 Returning a result from a function
4.3.1.3 Returning a result from a function
4.3.1.4 Returning a result from a function
4.3.1.5 Returning a result from a function
4.3.1.6 LAB: A leap year: writing your own functions Lab
4.3.1.7 LAB: How many days: writing and using your own functions Lab
4.3.1.8 LAB: Day of the year: writing and using your own functions Lab
4.3.1.9 LAB: Prime numbers - how to find them Lab
4.3.1.10 LAB: Converting fuel consumption Lab
4.3.1.11 SECTION SUMMARY
4.4. Functions and scopes 
BACK
4.4. FUNCTIONS AND SCOPES
4.4.1.1 Scopes in Python
4.4.1.2 Scopes in Python
4.4.1.3 Scopes in Python | global
4.4.1.4 Scopes in Python
4.4.1.5 SECTION SUMMARY
4.5. Creating simple functions 
BACK
4.5. CREATING SIMPLE FUNCTIONS
4.5.1.1 Creating functions | two-parameter functions
4.5.1.2 Creating functions | two-parameter functions
4.5.1.3 Creating functions | three-parameter functions
4.5.1.4 Creating functions | testing triangles
4.5.1.5 Creating functions | right-angle triangles
4.5.1.6 Creating functions | factorials
4.5.1.7 Creating functions | Fibonacci numbers
4.5.1.8 Creating functions | recursion
4.5.1.9 SECTION SUMMARY
4.6. Tuples and dictionaries 
BACK
4.6. TUPLES AND DICTIONARIES
4.6.1.1 Tuples and dictionaries
4.6.1.2 Tuples and dictionaries
4.6.1.3 Tuples and dictionaries
4.6.1.4 Tuples and dictionaries
4.6.1.5 Tuples and dictionaries
4.6.1.6 Tuples and dictionaries | methods
4.6.1.7 Tuples and dictionaries | methods
4.6.1.8 Tuples and dictionaries
4.6.1.9 Tuples and dictionaries
4.6.1.10 SECTION SUMMARY (1/3)
4.6.1.11 SECTION SUMMARY (2/3)
4.6.1.12 SECTION SUMMARY (3/3)
4.6.2.1 PROJECT: Tic-Tac-Toe Lab
4.6.2.2 Module Completion
Module 4 Quiz Quiz 
BACK
MODULE 4 QUIZ
4.7.1.1 PE1 -- Module 4 Quiz Quiz
Course completion 
BACK
COURSE COMPLETION
Python Essentials 1 Completed 
BACK
PYTHON ESSENTIALS 1 COMPLETED
5.1.1.0 Python Essentials 1 Completed
5.1.1.2 Earn PCEP certification
5.1.1.3 Earn PCEP certification
5.1.1.4 Congratulations
Binary left shift and binary right shift
Python offers yet another operation relating to single bits: shifting. This is applied only to integer values, and you mustn't use floats as arguments for it.

You already apply this operation very often and quite unconsciously. How do you multiply any number by ten? Take a look:

12345 × 10 = 123450


As you can see, multiplying by ten is in fact a shift of all the digits to the left and filling the resulting gap with zero.

Division by ten? Take a look:

12340 ÷ 10 = 1234


Dividing by ten is nothing but shifting the digits to the right.

The same kind of operation is performed by the computer, but with one difference: as two is the base for binary numbers (not 10), shifting a value one bit to the left thus corresponds to multiplying it by two; respectively, shifting one bit to the right is like dividing by two (notice that the rightmost bit is lost).

The shift operators in Python are a pair of digraphs: << and >>, clearly suggesting in which direction the shift will act.

value << bits
value >> bits


The left argument of these operators is an integer value whose bits are shifted. The right argument determines the size of the shift.

It shows that this operation is certainly not commutative.

The priority of these operators is very high. You'll see them in the updated table of priorities, which we'll show you at the end of this section.

Take a look at the shifts in the editor window.

The final print() invocation produces the following output:

17 68 8
output

Note:

17 >> 1 → 17 // 2 (17 floor-divided by 2 to the power of 1) → 8 (shifting to the right by one bit is the same as integer division by two)
17 << 2 → 17 * 4 (17 multiplied by 2 to the power of 2) → 68 (shifting to the left by two bits is the same as integer multiplication by four)

And here is the updated priority table, containing all the operators introduced so far:

Priority	Operator	
1	~, +, -	unary
2	**	
3	*, /, //, %	
4	+, -	binary
5	<<, >>	
6	<, <=, >, >=	
7	==, !=	
8	&	
9	|	
10	=, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=	



2. You can use bitwise operators to manipulate single bits of data. The following sample data:

x = 15, which is 0000 1111 in binary,
y = 16, which is 0001 0000 in binary.
will be used to illustrate the meaning of bitwise operators in Python. Analyze the examples below:

& does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary,
| does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary,
˜  does a bitwise not, e.g., ˜ x = 240*, which is 1111 0000 in binary,
^ does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary,
>> does a bitwise right shift, e.g., y >> 1 = 8, which is 0000 1000 in binary,
<< does a bitwise left shift, e.g., y << 3 = , which is 1000 0000 in binary,



In general, a typical function invocation may look like this:

result = function(arg)


The function takes an argument, does something, and returns a result.



A typical method invocation usually looks like this:

result = data.method(arg)



"""