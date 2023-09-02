#Variable scope - Local, Global & Enclosing or non-local

#local -Variables defined within a function have local scope.
#They are only accessible within the function in which they are defined.
#Once the function execution is complete, the local variables are destroyed, and their values are no longer accessible.

def my_function():
    x = 10  # x is a variable with local scope
    print(x)

my_function()
#print(x)  # This will raise an error because x is not defined in this scope


'''
Enclosing scope/Non-local variable
In Python, nested functions can access variables from their containing (enclosing) functions.
Variables from the enclosing function's scope are considered non-local variables within the nested function.
To modify non-local variables from within a nested function, you can use the nonlocal keyword.'''

def outer_function():
    y = 20  # y is in the enclosing scope

    def inner_function():
        nonlocal y
        y = 30  # Modify the non-local variable y
        print(y)

    inner_function()
    print(y)  # y has been modified by inner_function

outer_function()


#Global Scope:
'''
Variables defined at the top level of a Python script or module have global scope.
They are accessible from anywhere in the script or module, including within functions.
To modify global variables from within a function, you need to use the global keyword.
'''
global_variable = 50  # This is a variable with global scope

def modify_global():
    global global_variable
    global_variable = 60  # Modify the global variable
    print(global_variable)

modify_global()
print(global_variable)  # global_variable has been modified by modify_global
