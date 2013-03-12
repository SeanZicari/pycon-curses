import curses
from bpython.cli import stdscr

def do_curses(main_win):
	curses.cbreak()
	quote_window = curses.newwin(20, 50, 2, 0)
	quote_window.box()
	curses.doupdate()
	curses.noecho()
	main_win.keypad(1)
	curses.endwin()


if __name__ == '__main__':
	curses.wrapper(do_curses)
