'''
Author: Elijah Sawyers
Date: 11/11/2019
Overview: Creates the main window, adds the TextEditor widget to the window,
and starts the event loop.
'''

import tkinter as tk

from texteditor import TextEditor

if __name__ == '__main__':
    root = tk.Tk()
    root.title('escode')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    te = TextEditor().grid(column=0, row=0, sticky='NSEW')
    root.mainloop()
