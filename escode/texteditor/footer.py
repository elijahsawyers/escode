'''
Author: Elijah Sawyers
Date: 11/11/2019
'''

import tkinter as tk

class Footer(tk.Label):
    '''TODO'''

    def __init__(self, *args, **kwargs):
        '''TODO'''

        super().__init__(*args, **kwargs)

        self.config(
            background='#6cc3b7',
            foreground='#fff',
            height=1,
        )
