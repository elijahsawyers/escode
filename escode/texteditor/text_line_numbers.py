'''
Author: Elijah Sawyers
Date: 11/11/2019
'''

import tkinter as tk

class TextLineNumbers(tk.Canvas):
    '''TODO'''

    def __init__(self, *args, **kwargs):
        '''Initializes '''

        super().__init__(*args, **kwargs)

        self.text_box = None
        self.config(
            background='#c1c5d0',
            highlightthickness=0
        )

    def redraw(self):
        '''Redraws all line numbers.'''

        # Remove all line numbers.
        self.delete('all')

        # Sets the initial index to window coordinate (0, 0).
        index = self.text_box.text.index('@0,0')

        while True:
            # dlineinfo returns where a line of text starts and ends.
            dline = self.text_box.text.dlineinfo(index)

            # If None is returned, the line isn't visible, so break out of the loop.
            if dline is None:
                break

            # Grab the y-value of the line of text.
            y = dline[1]

            # Grab the line_number. The index is in the form 'line.column'.
            line_number = str(index).split('.')[0]

            # Actually write the line number onto the canvas.
            self.create_text(2, y, anchor='nw', text=line_number, fill='#64708b')

            # Go to the next line.
            index = self.text_box.text.index(f'{index}+1line')
