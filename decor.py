# abilities of functions in Python

# def mult(a, b):
#     return a*b
#
# print(mult(4, 6))
# print(type(mult))

# Example1: Treating the functions as object

# def shout(text):
#     return text.upper()
#
# print(shout('5'))
# yell = shout
# print(yell('kuku'))

# Example2: Passing the function as an argument

# x= map(int,['4', '6', 9])
# print(*x)

# def shout(text):
#     return text.upper()
#
# def whisper(text):
#     return text.lower()
#
# def spl(text):
#     return text.split()
#
# def greeting(func):
#     greet = func("Hi, I am created by a function passes as an ARGUMENT")
#     print(greet)
#
# greeting(shout)
# greeting(whisper)
# greeting(spl)

# Example3: Returning function from another function

# def create_adder(x):
#     def adder(y):
#        return x+y
#     return adder
#
# add_15 = create_adder(85)
# print(add_15(100))

# Decorators

# def func():
#     print("How are you?")
#
# func()

# def mydecorator(fn):
#     def inner_func():
#         print("This will be print first")
#         fn()
#         print("How are you?")
#     return inner_func
#
# @mydecorator
# def greet():
#     print("Hello! ", end='')
#
# # greet = mydecorator(greet)
#
# greet()


# define decorator
# def hello_decorator(func):
# # inner - a wrapper function in which the argument is called
# # inner function can access the outer local functions like in this case "func"
#     def inner():
#         print("Hello, this is before function 'func' execution")
#         # calling tha actual function now inside the wrapper function
#         func()
#         print("This is after function execution")
#     return inner
#
# @hello_decorator
# def function_to_be_used():
#     print("This is inside the passed function!")
#
# function_to_be_used()


# def new_decorator(func):
#     def inner(*args, **kwargs):
#         print("This row is before our function")
#         result = func(*args, **kwargs)
#         print("This row is after our function")
#         return result
#     return inner
# @new_decorator
# def sum_two_nums(a, b):
#     print("Inside the function")
#     return a + b
#
# x, y = 3, 5
# print("Sum=", sum_two_nums(x, y))
#
# @new_decorator
# def mul_three_nums(a, b=4, c=80):
#     print("Inside the function")
#     return a * b * c
#
# x, y, z = 3, 5, 8
# print("Sum=", mul_three_nums(x))

# Chaining decorators

# def decor1(func):
#     def inner():
#         x = func()
#         return x * x
#     return inner
#
# def decor2(func):
#     def inner():
#         x = func()
#         return 2 * x
#     return inner
#
# @decor2
# @decor1
# def num():
#     return 10
#
# print(num())

# def repeat(num_times):
#     def decorator_repeat(func):
#         def wrapper_repeat(*args, **kwargs):
#             for _ in range(num_times):
#                 value = func(*args, **kwargs)
#             return value
#         return wrapper_repeat
#     return decorator_repeat
# if __name__ == "__main__":
#     @repeat(3)
#     def greet(name):
#         print(f"Hello, {name}!")
#
#     greet("Alexander")
#
#
#     @repeat(4)
#     def sum2(x, y):
#         print(x + y)
#
#     sum2(4, 5)
#

# Decorator for measuring of memory usage

import tracemalloc


def measure_memory_usage(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()

        # Call to the original function
        result = func(*args, **kwargs)

        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics("lineno")

        # print the top memory-consuming lines
        print(f"Memory usage of {func.__name__}is:")
        for stat in top_stats[:3]:
            print(stat)

        return result

    return wrapper

# @measure_memory_usage
# def create_list(rn):
#     ls = [i**2 for i in range(1,rn+1)]
#     return ls
#
# create_list(10)

@measure_memory_usage
def calc_fact(n):
    if n == 0:
        return 1
    return n * calc_fact(n-1)

print(calc_fact(5))