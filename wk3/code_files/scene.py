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
    draw_clouds(canvas, 300, 250 , 450, 300)
    draw_clouds(canvas, 350, 300 , 550, 400)
    draw_clouds(canvas, 400, 250 , 600, 350)
    draw_pine_tree(canvas, 200, 350)
    draw_pine_tree(canvas, 250, 320)
    draw_pine_tree(canvas, 320, 300)
    
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

def draw_clouds(canvas, x, y, x0, y0):
    left = x
    right = x0
    top = y0
    bottom = y
    draw_oval(canvas, left, bottom, right, top, fill='white', outline='white')
    
def draw_pine_tree(canvas, peak_x, peak_y):
    """Draw one pine tree at location (peak_x, peak_y)"""

    # Compute the coordinates of the skirt and trunk.
    skirt_left  = peak_x - 70
    skirt_right = peak_x + 70
    skirt_bottom = peak_y - 210
    trunk_left  = peak_x - 20
    trunk_right = peak_x + 10
    trunk_bottom = peak_y - 260

    # Draw the tree trunk.
    draw_rectangle(canvas, trunk_left, trunk_bottom,
            trunk_right, skirt_bottom, fill="brown")

    # Draw the tree skirt.
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y,
            skirt_right, skirt_bottom, fill="forestGreen")

# Call the main function so that
# this program will start executing.
main()