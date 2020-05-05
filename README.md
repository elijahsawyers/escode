# escode
> The barebones text editor! 

<p align="center">
  <img src="https://raw.githubusercontent.com/elijahsawyers/escode/master/Demo.png" />
</p>

"escode" is a project that I started during my freshman year of college to learn the python programming language. To build it, I used Tkinter, which I very quickly learned is the absolute worst GUI framework known to man. As a result of this, the project was never "finished" like I would have liked it to be. However, this text editor does have the basic functionality needed to allow you to open, edit, and save files. It also features syntax highlighting for python, line numbers, and the current line and column number of the cursor in the footer.

# Running the text editor

Setup a virtual environment.

```sh
python -m venv venv
```

Install the requirements.

```sh
pip install -r requirements.txt
```

Run the main script.

```
python escode/main.py
```

# Built With
* [Tkinter](https://wiki.python.org/moin/TkInter)
* [Pygments](http://pygments.org/)

# Authors
* [Elijah Sawyers](https://github.com/elijahsawyers)
