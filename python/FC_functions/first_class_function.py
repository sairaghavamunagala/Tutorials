"""
First class functions

```
Functions are first-class objects in the Python programming language, 
which means they can be used in the same ways as other objects. 
Assigning functions to variables, passing them as arguments to other functions, 
and returning functions as values all fall under this category. 
First-class functions are those that can handle functions in this manner.
```

Properties of first class functions:

    1.A function is an instance of the Object type.
    2.You can store the function in a variable.
    3.You can pass the function as a parameter to another function.
    4.You can return the function from a function.
    5.You can store them in data structures such as hash tables, lists
"""
# Example
"""
- Functions are objects
- can store the function in a variable
"""
def square(x):
    return x*x
f=square
print(square)
print(f)
"""
Example for passing the function as a parameter to another function
"""
def my_map(func,arg_list):
    result=[]
    for i in arg_list:
        result.append(func(i))
    return result


"""
return the function from a function
"""
def logger(msg):

    def log_msg():
        print("Log:",msg)

    return log_msg

log_hi=logger('Hi!')
log_hi()

"""
return the function from a function
"""
def html_tag(tag):

    def wrap_text(msg)->None:
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline!')
# print_h1('Another Headline!')

# print_p = html_tag('p')
# print_p('Test Paragraph!')
