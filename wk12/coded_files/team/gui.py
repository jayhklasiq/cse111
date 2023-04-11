import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
from math import pi

def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Area of a Cricle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()
    
def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Radius:"
    lbl_rad = Label(frm_main, text="Radius:")

    # Create an integer entry box where the user will enter the radius of circle.
    ent_rad = IntEntry(frm_main, width=4, lower_bound=0, upper_bound=20)

    # Create a label that displays "Area:"
    lbl_area = Label(frm_main, text="Area:")

    # Create labels that will display the results.
    lbl_result = Label(frm_main, width=3)

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_rad.grid(      row=0, column=0, padx=3, pady=3)
    ent_rad.grid(      row=0, column=1, padx=3, pady=3)

    lbl_area.grid(     row=1, column=0, padx=(30,3), pady=3)
    lbl_result.grid(      row=1, column=1, padx=3, pady=3)

    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")
    
    
    # This function will be called each time the user releases a key.
    def calculate():
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            # Get the radius.
            rad = ent_rad.get()

            # Compute the area of circle using the radius given
            area = pi * (rad ** 2)

            # Display the area of circle
            lbl_area.config(text=f"{area:.0f}")
            

        except ValueError:
            # When the user deletes all the digits in the radius
            # entry box, clear the area label.
            lbl_area.config(text="")

    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_rad.clear()
        lbl_area.config(text="")
        ent_rad.focus()

    # Bind the calculate function to the radius entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_rad.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_rad.focus()

if __name__ == "__main__":
    main()