'''
Author: Elijah Sawyers
Date: 11/11/2019
'''

import tkinter as tk
import tkinter.filedialog
from idlelib.redirector import WidgetRedirector

from .footer import Footer
from .text_box import TextBox
from .text_line_numbers import TextLineNumbers

class TextEditor(tk.Frame):
    '''TODO'''

    def __init__(self, *args, **kwargs):
        '''TODO'''

        super().__init__(*args, **kwargs)

        self.file_name = None

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

        # Setup menubar.
        self.menubar = tk.Menu(args[0])
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label='New', command=self._new)
        self.file_menu.add_command(label='Open', command=self._open)
        self.file_menu.add_command(label='Save', command=self._save)
        self.menubar.add_cascade(label='File', menu=self.file_menu)
        args[0].config(menu=self.menubar)

    def _on_change(self, event):
        '''TODO'''

        self.line_numbers.redraw()
        self.text_box.highlight_text()

        cursor_position = self.text_box.text.index(tk.INSERT)
        self.footer.update_ln_col_number(
            cursor_position.split('.')[0],
            cursor_position.split('.')[1]
        )

    def _new(self):
        '''TODO'''
        
        self.text_box.text.delete('0.0', tk.END)

    def _open(self):
        '''TODO'''
        
        self.filename = tk.filedialog.askopenfilename(initialdir = '~/')

        with open(self.filename, 'r') as file:
            self.text_box.text.delete('0.0', tk.END)
            self.text_box.text.insert('0.0', file.read())

    def _save(self):
        '''TODO'''

        if not self.filename:
            self.filename = tk.filedialog.asksaveasfilename(initialdir = '~/')

        with open(self.filename, 'w') as file:
            file.write(self.text_box.text.get('0.0', tk.END))
