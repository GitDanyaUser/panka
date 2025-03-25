import os
import sys
import curses
from libs import log

class Pyste:
    """
    A simple powerful TUI engine
    """
    def __init__(self, stdscr, cursor_display: bool=False):
        self.stdscr = stdscr
        cursor_displayshow = 1 if cursor_display else 0
        curses.curs_set(cursor_displayshow)
        self.stdscr.keypad(True)
        self.stdscr.timeout(100)

    def clear(self):
        self.stdscr.clear()

    def refresh(self):
        self.stdscr.refresh()

    def print(self, y, x, text):
        self.stdscr.addstr(y, x, text)

    def char_handle(self, w: None | str=None, a: None | str=None, s: None | str=None, d: None | str=None, quit: int | str=curses.KEY_EXIT) -> str | None:
        try:
            key = self.stdscr.getch()
            if key == quit:
                return 'Quit'
            if w is not None and key == ord(w):
                return 'Up w'
            elif a is not None and key == ord(a):
                return 'Left a'
            elif s is not None and key == ord(s):
                return 'Down s'
            elif d is not None and key == ord(d):
                return 'Right d'
            return None
        except KeyboardInterrupt:
            return 'Quit' 

    def example(self) -> None:
        self.clear()
        self.print(5, 5, "Hello!\n")
        self.refresh()
        inpot = self.char_handle()
        while inpot != 'Quit':
            self.clear()
            self.print(5, 5, f'Input: {inpot}')
            self.refresh()
            inpot = self.char_handle()

def example_in_source(stdscr):
    tui: Pyste = Pyste(stdscr)
    tui.example()

if __name__ == "__main__":
    curses.wrapper(example_in_source)


# Under Construction
