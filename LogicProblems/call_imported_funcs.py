'''
File: call_imported_funcs.py
Author: Rohan O'Malley
Purpose: The purpose of this program is to import a functions
from the short1_thing.py. Those functions are then called in 
and what they return is printed out. The content they produce
is kept in variables that are used in parameters for the
baz function.
Course: Fall CS 120
'''
import short1_thing

user = input()

# call foo
foo_var = (short1_thing.foo(user))

print(foo_var)

second_user = input()
third_user =input()

# call bar
bar_var = short1_thing.bar(user,second_user,third_user)

print(bar_var)

# call baz
baz_var = short1_thing.baz(foo_var,bar_var,)

print(baz_var)



