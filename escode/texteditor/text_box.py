'''
Author: Elijah Sawyers
Date: 11/11/2019
'''

import pygments
import tkinter as tk
from pygments.lexers import PythonLexer

class TextBox(tk.Frame):
    '''A text box widget.'''

    def __init__(self, *args, **kwargs):
        '''Initialize the text box widget.'''

        super().__init__(*args, **kwargs)

        # Create widgets.
        self.text = tk.Text(self)
        self.vsb = tk.Scrollbar(self, orient='vertical', command=self.text.yview)
        self.hsb = tk.Scrollbar(self, orient='horizontal', command=self.text.xview)

        # Configure widgets.
        self.text.config(highlightthickness=0, wrap='none')
        self.text.config(yscrollcommand=self.vsb.set)
        self.text.config(xscrollcommand=self.hsb.set)
        self.text.tag_configure('Token.Keyword', foreground='#0000ff')
        self.text.tag_configure('Token.Name.Builtin.Pseudo', foreground='#0000ff')
        self.text.tag_configure('Token.Literal.Number.Integer', foreground='#008000')
        self.text.tag_configure('Token.Literal.Number.Float', foreground='#008000')
        self.text.tag_configure('Token.Literal.String.Single', foreground='#b77600')
        self.text.tag_configure('Token.Literal.String.Double', foreground='#b77600')
        self.text.tag_configure('Token.Literal.String.Doc', foreground='#b77600')
        self.text.tag_configure('Token.Comment.Single', foreground='#008000')
        self.text.tag_configure('Token.Comment.Hashbang', foreground='#008000')

        # Geometry management.
        self.text.grid(column=0, row=0, sticky='NSEW')
        self.vsb.grid(column=1, row=0, sticky='NS')
        self.hsb.grid(column=0, row=1, sticky='EW')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Event handlers.
        self.text.bind("<Tab>", self._tab)

        # Create a proxy for the underlying Tk widget to generate a <<Change>> event.
        self.text._orig = self.text._w + '_orig'
        self.text.tk.call('rename', self.text._w, self.text._orig)
        self.text.tk.createcommand(self.text._w, self._proxy)

    def _proxy(self, *args):
        '''Event proxy.'''

        # Let the actual widget perform the requested action.
        cmd = (self.text._orig,) + args
        try:
            result = self.tk.call(cmd)
        except Exception:
            return None

        # Generate a <<Change>> event on-add, on-delete, or on-scroll.
        if (args[0] in ('insert', 'replace', 'delete') or
            args[0:2] == ('xview', 'scoll') or
            args[0:2] == ('yview', 'scroll') or
            args[0:2] == ('xview', 'moveto') or
            args[0:2] == ('yview', 'moveto')
        ):

            # Highlight text on insert and delete.
            if (
                args[0:2] == ('insert', 'insert') or
                args[0] == 'delete'
            ):
                self._highlight_text()

            self.event_generate('<<Change>>', when='tail')

        # Return what the actual widget returned.
        return result

    def _tab(self, *args):
        '''Insert four spaces on tab press.'''

        self.text.insert(tk.INSERT, ' ' * 4)
        return 'break'

    def _highlight_text(self):
        '''Highlight the text in the text box.'''

        start_index = self.text.index('@0,0')
        end_index = self.text.index(tk.END)

        for tag in self.text.tag_names():
            self.text.tag_remove(tag, self.text.index('@0,0'), end_index)

        code = self.text.get(start_index, end_index)

        for index, line in enumerate(code):
            if index == 0 and line != '\n':
                break
            elif line == '\n':
                start_index = self.text.index(f'{start_index}+1line')
            else:
                break

        self.text.mark_set('range_start', start_index)
        for token, content in pygments.lex(code, PythonLexer()):
            self.text.mark_set('range_end', f'range_start + {len(content)}c')
            self.text.tag_add(str(token), 'range_start', 'range_end')
            self.text.mark_set('range_start', 'range_end')
