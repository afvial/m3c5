# How to Import a Module and Assign an Alias in Python

import sys
sys.path.insert(0, './libs')
import helper as h

def render():
    print(h.greeting('Tiffany', 'Hudgens'))

render()

import math as m
m.sqrt(4)
