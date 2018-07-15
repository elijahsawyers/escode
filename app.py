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

        # Create the label for line numbers.
        self.lines = 2
        self.line_numbers = tk.Text(self, width=5, padx=5, pady=3, highlightthickness=0)
        self.line_numbers.configure(font=("courier", 16), background="#eee", foreground="#aaa", cursor="")
        self.line_numbers.grid(column=0, row=0, sticky="NSEW")
        self.line_numbers.insert(tk.END, "    1")
        self.line_numbers.configure(state="disabled")

        # Create horizontal scroll bar.
        self.horizontal_scroll_bar = tk.Scrollbar(self, orient="horizontal", command=self.text_field.xview)
        self.horizontal_scroll_bar.grid(column=1, row=1, sticky='NSEW')
        self.text_field['xscrollcommand'] = self.horizontal_scroll_bar.set

        # Create vertical scroll bar.
        self.vertical_scroll_bar = tk.Scrollbar(self, orient="vertical", command=self.text_field.yview)
        self.vertical_scroll_bar.grid(column=2, row=0, sticky='NSEW')
        self.text_field['yscrollcommand'] = self.vertical_scroll_bar.set

    def _create_events(self):
        '''
        Binds event listeners to widgets and key presses.
        '''
        self.text_field.bind("<Tab>", self._tab_pressed)
        self.text_field.bind("<{>", self._curly_pressed)
        self.text_field.bind("<[>", self._bracket_pressed)
        self.text_field.bind("<(>", self._parenthesis_pressed)
        self.text_field.bind("<'>", self._single_quote_pressed)
        self.text_field.bind("<\">", self._double_quote_pressed)
        self.text_field.bind("<Return>", self._update_line_number)

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
    
    def _single_quote_pressed(self, event):
        '''
        Method executed when the single quote key is pressed. This method adds another single quote
        and positions the cursor between the quotes.
        '''
        self.text_field.insert(tk.INSERT, "''")
        self.text_field.mark_set(tk.INSERT, f"{self.text_field.index(tk.INSERT).split('.')[0]}.{int(self.text_field.index(tk.INSERT).split('.')[1]) - 1}")
        return "break"

    def _double_quote_pressed(self, event):
        '''
        Method executed when the double quote key is pressed. This method adds another double quote
        and positions the cursor between the quotes.
        '''
        self.text_field.insert(tk.INSERT, '""')
        self.text_field.mark_set(tk.INSERT, f"{self.text_field.index(tk.INSERT).split('.')[0]}.{int(self.text_field.index(tk.INSERT).split('.')[1]) - 1}")
        return "break"

    def _update_line_number(self, event):
        self.line_numbers.configure(state="normal")
        if (self.lines < 10):
            self.line_numbers.insert(tk.END, f"    {self.lines}\n")
        elif (self.lines < 100):
            self.line_numbers.insert(tk.END, f"   {self.lines}\n")
        elif (self.lines < 1000):
            self.line_numbers.insert(tk.END, f"  {self.lines}\n")
        elif (self.lines < 10000):
            self.line_numbers.insert(tk.END, f" {self.lines}\n")
        else: 
            self.line_numbers.insert(tk.END, f" {self.lines}\n")
        self.lines += 1
        self.line_numbers.configure(state="disabled")

if __name__ == "__main__":
    TextEditor.main()
