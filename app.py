'''
Author: Elijah Sawyers
Date: 2018
Overview: A text editor using tkinter to open/edit/write/save .py files.
'''

import tkinter as tk
from tkinter import ttk

class TextEditor(ttk.Frame):
    '''
    The TextEditor class holds all relevant widgets/data of the text editor application.
    '''
    @classmethod
    def main(cls):
        '''
        Creates the main window, and starts the main loop.
        '''
        # Create the main window.
        root = tk.Tk()
        root.minsize(width=750, height=400)
        root.title("ES Code")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Create the application's widgets, and start the main loop.
        cls(root)
        root.mainloop()

    def __init__(self, root=None):
        """
        Initializes the TextEditor class.
        """
        # Create the main frame to contain all widgets.
        super().__init__(root)
        self.grid(column=0, row=0, sticky="NSEW")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        # Create widgets and bindings.
        self._create_widgets()
        self._create_events()

    def _create_widgets(self):
        '''
        Initializes all widgets, and adds them to the screen using the grid geometry manager.
        '''
        # Create the main text field.
        self.text_field = tk.Text(self, padx=5, pady=3, wrap="none")
        self.text_field.configure(highlightthickness=0, font=("courier", 16))
        self.text_field.grid(column=1, row=0, sticky="NSEW")

        #Create the label for line numbers.
        self.lines = tk.StringVar()
        self.lines.set("1\n")
        self.line_numbers = tk.Label(self, padx=5, pady=5, width=4, textvariable=self.lines, anchor="ne")
        self.line_numbers.configure(font=("courier", 16), background="#eee", foreground="#aaa")
        self.line_numbers.grid(column=0, row=0, sticky="NSEW")

        # Create horizontal scroll bar.
        scroll_bar = tk.Scrollbar(self, orient="horizontal", command=self.text_field.xview)
        scroll_bar.grid(column=1, row=1, sticky='NSEW')
        self.text_field['xscrollcommand'] = scroll_bar.set

        # Create vertical scroll bar.
        scroll_bar = tk.Scrollbar(self, orient="vertical", command=self.text_field.yview)
        scroll_bar.grid(column=2, row=0, sticky='NSEW')
        self.text_field['yscrollcommand'] = scroll_bar.set

    def _create_events(self):
        '''
        Binds event listeners to widgets and key presses.
        '''
        self.text_field.bind("<Tab>", self._tab_pressed)
        self.text_field.bind("<{>", self._curly_pressed)
        self.text_field.bind("<[>", self._bracket_pressed)
        self.text_field.bind("<(>", self._parenthesis_pressed)

    def _tab_pressed(self, event):
        '''
        Method executed when the tab key is press. Inserts four spaces rather than a tab character.
        '''
        self.text_field.insert(tk.INSERT, " " * 4)
        return "break"

    def _curly_pressed(self, event):
        '''
        Method executed when the left-curlybrace key is pressed. This method autocompletes the right
        curly brace and positions the cursor between the braces.
        '''
        self.text_field.insert(tk.INSERT, "{}")
        self.text_field.mark_set(tk.INSERT, f"{self.text_field.index(tk.INSERT).split('.')[0]}.{int(self.text_field.index(tk.INSERT).split('.')[1]) - 1}")
        return "break"

    def _bracket_pressed(self, event):
        '''
        Method executed when the left-bracket key is pressed. This method autocompletes the right bracket
        and positions the cursor between the brackets.
        '''
        self.text_field.insert(tk.INSERT, "[]")
        self.text_field.mark_set(tk.INSERT, f"{self.text_field.index(tk.INSERT).split('.')[0]}.{int(self.text_field.index(tk.INSERT).split('.')[1]) - 1}")
        return "break"

    def _parenthesis_pressed(self, event):
        '''
        Method executed when the left-parenthesis key is pressed. This method autocompletes the right parenthesis
        and positions the cursor between the parenthesis.
        '''
        self.text_field.insert(tk.INSERT, "()")
        self.text_field.mark_set(tk.INSERT, f"{self.text_field.index(tk.INSERT).split('.')[0]}.{int(self.text_field.index(tk.INSERT).split('.')[1]) - 1}")
        return "break"

if __name__ == "__main__":
    TextEditor.main()
