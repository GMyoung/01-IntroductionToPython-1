"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Yicheng Yang.
"""
########################################################################
# DONE : 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()
my_turtle = rg.SimpleTurtle('turtle')
my_turtle.pen = rg.Pen('red', 5)
my_turtle.speed = 10
size = 300
for k in range(6):
    my_turtle.draw_square(size)
    my_turtle.pen_up()
    my_turtle.right(54)
    my_turtle.forward(100)
    my_turtle.left(60)
    my_turtle.pen_down()
    size=size-13
#my second turtle
window.tracer(50)
my2_turtle=rg.SimpleTurtle ('triangle')
my2_turtle.pen = rg.Pen('midnight blue', 2)
my2_turtle.backward(70)

for k in range(800):
    my2_turtle.left(20)
    my2_turtle.forward(k)

window.close_on_mouse_click()
