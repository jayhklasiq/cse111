import os
os.system('cls')
# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_grid(canvas, scene_width, scene_height, 50)
    draw_ground(canvas, scene_width, scene_height)
    draw_sky(canvas, scene_width, scene_height)
    draw_clouds(canvas)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_grid(canvas, width, height, interval):
    #draw a vertical line
    label_y = 10
    for x in range(interval, width, interval):
     draw_line(canvas, x, 0, x, height)
     draw_text(canvas, x, label_y, f'{x}')
     
    #draw a horizontal line
    label_x = 10
    for y in range(interval, height, interval):
     draw_line(canvas, 0, y, width, y)
     draw_text(canvas, label_x, y, f'{y}')
     
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill='sky blue')
    
def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill='tan4')    

def draw_clouds(canvas):
    draw_oval(canvas, 300, 350, 500, 450, width= 0, fill='white')
    draw_oval(canvas, 200, 300, 400, 400, width= 0, fill='white')
    draw_oval(canvas, 450, 350, 550, 400, width= 0, fill='white')
    

      

# Call the main function so that
# this program will start executing.
main()