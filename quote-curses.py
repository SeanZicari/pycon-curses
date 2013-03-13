import curses


quote_window = None
main_window = None


def init_curses(main_win):
	quote_window = curses.newwin(10,10, 5,1)
	curses.curs_set(0)
	main_win.keypad(1)
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)


def setup_quote_window():
	pass
	

def main_loop():
	global main_window, quote_window

	while True:
		c = main_window.getch()

		if c == ord('r') or c == ord('R'):
			quote_window.clear()
			quote_window.box()
			quote_window.addstr(1,1, "Yo!")
		
		if c == curses.KEY_F1:
			main_window.addstr(2,0, "You pressed F1")
		else:
			main_window.move(2,0)
			main_window.clrtoeol()

		if c == ord('q') or c == ord('Q'):
			break

		quote_window.noutrefresh()
		curses.doupdate()


def do_curses(win):
	global main_window, quote_window
	main_window = win
	
	init_curses(main_window)

	# Output the current display size
	main_window.addstr("RANDOM QUOTES", curses.A_REVERSE)
	main_window.chgat(-1, curses.A_REVERSE)
	main_window.addstr(curses.LINES-1, 0, "Press 'R' to request a new quote, 'Q' to quit", curses.COLOR_BLUE)
	main_window.chgat(curses.LINES-1,7, 1, curses.A_BOLD | curses.color_pair(2))
	main_window.chgat(curses.LINES-1,35, 1, curses.A_BOLD | curses.color_pair(1))
	
	quote_window = curses.newwin(10,curses.COLS, 3,0)
	quote_window.box()
	quote_window.addstr(1,1, "Testing")
	
	curses.doupdate()
	
	main_loop()

	curses.endwin()


if __name__ == '__main__':
	curses.wrapper(do_curses)
