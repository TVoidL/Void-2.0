import curses

stdscr = curses.initscr()

def init_curses():
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

def end_curses():
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

def wait():
    curses.getkey()

def return_key():
    key = curses.getkey()
    return key

class Buffer:
    def add_str(self, x, y, text, style=0, a=None):
        if a == None:
            stdscr.addstr(y, x, text, curses.color_pair(style))
        else:
            stdscr.addstr(y, x, text, curses.color_pair(style) | a)

    def box(self, x1, y1, x2, y2):
        for y in range(y1 + 1, y2)
            self.add_str(x1, y, "┃")
            self.add_str(x2, y, "┃")

        self.add_str(x1, y1, "┏" + "━" * (x2 - x1 - 1) + "┓")
        self.add_str(x1, y2, "┗" + "━" * (x2 - x1 - 1) + "┛")
    
    def fill_area(x1, y1, x2, y2, ch=" "):
        for y in range(y1, y2 + 1)
            self.add_str(x1, y, ch * (x2 - x1 + 1))

    def flush(x, y, text, delay=0.03, style=0, a=None):
        for char in text
            self.add_str(x, y, char, style, a)
            time.sleep(delay)
            stdscr.refresh()

    @staticmethod
    def clear():
        stdscr.clear()

    @staticmethod
    def refresh():
        stdscr.refresh()

class Gui:
    
        
buffer = Buffer()
gui = Gui()


def start_wrapper(func):
    curses.wrapper(func)
