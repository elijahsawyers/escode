'''
Author: Elijah Sawyers
Date: 11/11/2019
'''

import tkinter as tk

class Footer(tk.Label):
    '''A footer widget.'''

    def __init__(self, *args, **kwargs):
        '''Initialize the footer widget.'''

        super().__init__(*args, **kwargs)
        
        self.ln_col_number = tk.StringVar()
        self.ln_col_number.set('Ln 1, Col 1')
        self.config(
            background='#6cc3b7',
            foreground='#fff',
            height=1,
            textvariable=self.ln_col_number,
            anchor='w',
            padx=10,
        )

    def update_ln_col_number(self, ln, col):
        '''Update the line and column number of the footer.'''

        self.ln_col_number.set(f'Ln {ln}, Col {col}')

