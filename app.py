'''
Author: Elijah Sawyers
Date: 2018
Overview: A text editor using tkinter to open/edit/write/save .py files.

TODO: 
    1) Add text highlighting.
    2) Add file I/O.
    2) Fix line number resize problem.
    3) Add event binding for window resize with cmd+ and cmd-.
    4) Code cleanup.
'''

import tkinter as tk
from tkinter import ttk

class TextEditor(tk.Frame):
    '''
    The TextEditor class holds all widgets and functionality of the text editor application.
    '''
    @classmethod
    def main(cls):
        '''
        This method creates the main window, and starts the main loop.
        '''
        # Create the application's main window.
        root = tk.Tk()
        root.minsize(width=1000, height=612)
        root.maxsize(width=1000, height=612)
        root.title("ES Code")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Create the application's widgets, and start the event loop.
        cls(root)
        root.mainloop()

    def __init__(self, root=None):
        """
        This method initializes the TextEditor class.
        """
        # Create the main frame to contain all widgets.
        super().__init__(root)
        self.grid(column=0, row=0, sticky="NSEW")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.config(background="#c1c5d0")

        # Create widgets and bindings.
        self.create_widgets()
        self.create_events()

        # Start tracking ln/col number changes.
        self.update_line_numbers()

    def create_widgets(self):
        '''
        This method initializes all widgets, and adds them to the screen using the grid geometry manager.
        '''
        # Create the main text field.
        self.text_field = tk.Text(
                    self, 
                    padx=5,
                    pady=3,
                    wrap="none",
                    highlightthickness=0,
        )
        self.text_field.grid(column=1, row=0, sticky="NSEW")

        # Create the text widget for line numbers.
        self.lines = ""
        self.line_numbers = tk.Text(
                    self,
                    width=5,
                    padx=5,
                    pady=3,
                    highlightthickness=0,
                    background="#c1c5d0",
                    foreground="#64708b",
                    cursor="",
                    state="disabled"
        )
        self.line_numbers.grid(column=0, row=0, sticky="NSEW")

        # Create the current line and column labels.
        self.cursor_location = tk.StringVar()
        self.cursor_location.set("Ln 1, Col 1")
        self.cursor_location_label = tk.Label(
                    self, 
                    background="#6cc3b7",
                    foreground="#fff",
                    height=1,        
                    textvariable=self.cursor_location,
                    anchor="w",
                    padx=50,      
        )
        self.cursor_location_label.grid(column=0, row=2, columnspan=3, sticky="NSEW")

        # Create horizontal scroll bar.
        self.horizontal_scroll_bar = tk.Scrollbar(
                    self,
                    orient="horizontal",
                    command=self.text_field.xview
        )
        self.horizontal_scroll_bar.grid(column=1, row=1, sticky='NSEW')
        self.text_field['xscrollcommand'] = self.horizontal_scroll_bar.set

        # Create vertical scroll bar.
        self.vertical_scroll_bar = tk.Scrollbar(
                    self,
                    orient="vertical",
                    command=self.text_field.yview
        )
        self.vertical_scroll_bar.grid(column=2, row=0, sticky='NSEW')
        self.text_field['yscrollcommand'] = self.vertical_scroll_bar.set

    def create_events(self):
        '''
        This method binds event listeners to widgets and key presses.
        '''
        self.text_field.bind("<Tab>", self.tab_pressed)
        self.text_field.bind("<{>", self.curly_pressed)
        self.text_field.bind("<[>", self.bracket_pressed)
        self.text_field.bind("<(>", self.parenthesis_pressed)
        self.text_field.bind("<'>", self.single_quote_pressed)
        self.text_field.bind("<\">", self.double_quote_pressed)

    def tab_pressed(self, event):
        '''
        This method is executed when the tab key is press.
        Inserts four spaces rather than a tab character.
        '''
        self.text_field.insert(tk.INSERT, " " * 4)
        return "break"

    def curly_pressed(self, event):
        '''
        This method is executed when the left-curlybrace key is pressed. This method autocompletes
        the right curly brace and positions the cursor between the braces.
        '''
        self.text_field.insert(tk.INSERT, "{}")
        self.text_field.mark_set(tk.INSERT, f"{self.text_field.index(tk.INSERT).split('.')[0]}.{int(self.text_field.index(tk.INSERT).split('.')[1]) - 1}")
        return "break"

    def bracket_pressed(self, event):
        '''
        This method is executed when the left-bracket key is pressed. This method
        autocompletes the right bracket and positions the cursor between the brackets.
        '''
        self.text_field.insert(tk.INSERT, "[]")
        self.text_field.mark_set(tk.INSERT, f"{self.text_field.index(tk.INSERT).split('.')[0]}.{int(self.text_field.index(tk.INSERT).split('.')[1]) - 1}")
        return "break"

    def parenthesis_pressed(self, event):
        '''
        This method is executed when the left-parenthesis key is pressed. This method
        autocompletes the right parenthesis and positions the cursor between the parenthesis.
        '''
        self.text_field.insert(tk.INSERT, "()")
        self.text_field.mark_set(tk.INSERT, f"{self.text_field.index(tk.INSERT).split('.')[0]}.{int(self.text_field.index(tk.INSERT).split('.')[1]) - 1}")
        return "break"

    def single_quote_pressed(self, event):
        '''
        This method is executed when the single quote key is pressed. This method adds
        another single quote and positions the cursor between the quotes.
        '''
        self.text_field.insert(tk.INSERT, "''")
        self.text_field.mark_set(tk.INSERT, f"{self.text_field.index(tk.INSERT).split('.')[0]}.{int(self.text_field.index(tk.INSERT).split('.')[1]) - 1}")
        return "break"

    def double_quote_pressed(self, event):
        '''
        This method is executed when the double quote key is pressed. This method adds
        another double quote and positions the cursor between the quotes.
        '''
        self.text_field.insert(tk.INSERT, '""')
        self.text_field.mark_set(tk.INSERT, f"{self.text_field.index(tk.INSERT).split('.')[0]}.{int(self.text_field.index(tk.INSERT).split('.')[1]) - 1}")
        return "break"

    def get_line_numbers(self):
        '''
        This method determines which line numbers are currently on the screen.

        :returns: This method returns the line numbers on screen.
        '''
        last_line = "0"
        lines_on_screen = ""

        # Loop over the size of the Text widget in 10 pixel increments.
        for i in range(0, self.text_field.winfo_height(), 10):
            # Grab the line of the character closest to the current pixel's coordinates.
            current_line = self.text_field.index(f"@0,{i}").split('.')[0]

            # If the last iterated character's line is != to the current character's line, add it to
            if last_line != current_line:
                last_line = current_line
                lines_on_screen += (f"    {current_line}\n")[-6:]
        return lines_on_screen


    def update_line_numbers(self):
        '''
        After being called once, this method will update the line numbers and the
        ln/col footer every 10ms. 
        '''
        # Get lines on screen.
        lines_on_screen = self.get_line_numbers()

        # If lines on screen are different from the last update, change which lines are displayed.
        if self.lines != lines_on_screen:
            self.lines = lines_on_screen
            self.line_numbers.config(state='normal')
            self.line_numbers.delete('1.0', 'end')
            self.line_numbers.insert('1.0', lines_on_screen)
            self.line_numbers.config(state='disabled')

        # Update the ln and col number footer. 
        self.cursor_location.set(f"Ln {self.text_field.index(tk.INSERT).split('.')[0]}, Col {self.text_field.index(tk.INSERT).split('.')[1]}")

        # Update the line numbers after every 10 milliseconds.
        self.text_field.after(10, self.update_line_numbers)

if __name__ == "__main__":
    TextEditor.main()
