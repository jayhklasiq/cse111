# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

import random
def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    # 550 = center of tree - 150 = button of tree - 250 = 400 - 150 height of tree
    # Draw the clouds
    draw_clouds(canvas, 450, 300, 600, 400)
    draw_clouds(canvas, 350, 350, 550, 450)
    draw_clouds(canvas, 500, 325, 700, 425)
   

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_clouds(canvas, x, x0, y0, y1):
    left = x
    right = x0
    bottom = y0
    top = y1 

    draw_oval(canvas, left, right, bottom, top, fill="gray74", outline="gray74")

    
main()