# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 13:29:25 2024

@author: axpothier
"""

import turtle
from rectangle import rectangle

def route():
    turtle.fillcolor('grey')
    turtle.begin_fill()
    rectangle(0, -300, 800, 80)
    turtle.end_fill()
    position_trait = -400
    for k in range(16):
        turtle.fillcolor('white')
        turtle.begin_fill()
        rectangle(position_trait, -260, 30, 10)
        turtle.end_fill()
        position_trait += 65
    
