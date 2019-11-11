'''
Author: Elijah Sawyers
Date: 11/11/2019
'''

import tkinter as tk

from .footer import Footer
from .text_box import TextBox
from .text_line_numbers import TextLineNumbers

class TextEditor(tk.Frame):
    '''TODO'''

    def __init__(self, *args, **kwargs):
        '''TODO'''

        super().__init__(*args, **kwargs)

        # Create widgets.
        self.footer = Footer(self)
        self.text_box = TextBox(self)
        self.line_numbers = TextLineNumbers(self, width=30)
        self.line_numbers.text_box = self.text_box

        # Geometry management.
        self.line_numbers.grid(column=0, row=0, sticky='NS')
        self.text_box.grid(column=1, row=0, sticky='NSEW')
        self.footer.grid(column=0, row=1, columnspan=2, sticky='NSEW')
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Event handlers.
        self.text_box.bind('<<Change>>', self._on_change)
        self.text_box.bind('<Configure>', self._on_change)

    def _on_change(self, event):
        '''TODO'''

        self.line_numbers.redraw()
        self.text_box.highlight_text()
