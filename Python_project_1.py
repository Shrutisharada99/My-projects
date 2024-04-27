def myself (name):
    try:
        print('My name is'+ str(name))
    except ValueError:
        print("That's not a name")
myself ('Shruti')
myself (3)

#importing statements
import random #1
random.randint(1,10)
import random, sys, os, math #2
from random import *
randint(1,10) #3


