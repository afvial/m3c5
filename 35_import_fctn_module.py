# How to import a Single Function from  a Python Module

# from math import sqrt
# sqrt(4)

# To be copied on main.py
import sys
sys.path.insert(0, './libs')
from helper import greeting

def render():
    print(greeting('Tiffany', 'Hudgens'))

render()


