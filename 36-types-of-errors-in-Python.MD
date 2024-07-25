1. Syntax Errors: These occur when the parser detects a syntactical issue in the code.

*************************************************************************************

2. Exceptions
Exceptions are errors that occur during the execution of a program. They can be handled using try-except blocks.

Built-in Exceptions:
Here are some common built-in exceptions:

TypeError: Raised when an operation or function is applied to an object of inappropriate type.
1 + 'a'


ValueError: Raised when a function gets an argument of the right type but inappropriate value.
int('abc')


IndexError: Raised when a sequence subscript is out of range.
my_list = [1, 2, 3]
my_list[5]


KeyError: Raised when a dictionary key is not found.
my_dict = {'a': 1}
my_dict['b']


AttributeError: Raised when an attribute reference or assignment fails.
my_list = [1, 2, 3]
my_list.appendd(4)


ImportError: Raised when an import statement fails.
import non_existent_module


ZeroDivisionError: Raised when division or modulo by zero takes place.
1 / 0


FileNotFoundError: Raised when trying to open a file that does not exist.
open('non_existent_file.txt')


IOError: Raised when an I/O operation fails (not relevant in Python 3.3+ where it is now an alias of OSError).
open('non_existent_file.txt')


OSError: Raised for operating system-related errors.
os.remove('non_existent_file.txt')


*************************************************************************************
3. Custom Exceptions:
You can also define your own exceptions by creating a class that inherits from the built-in Exception class.
class MyCustomError(Exception):
    pass
raise MyCustomError("This is a custom error")
