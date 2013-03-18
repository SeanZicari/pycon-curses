import curses
from getter import get_new_quote, get_new_joke


quote_window = None
quote_text_window = None
stdscr = None
quote_pad = None


def init_curses(main_win):
    curses.curs_set(0)
    main_win.keypad(1)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)


def setup_quote_window():
    pass


def main_loop():
    global stdscr, quote_window, quote_text_window, qw_size

    while True:
        c = quote_window.getch()

        if c == ord('r') or c == ord('R'):
            quote_text_window.clear()
            quote_text_window.addstr("Getting quote...", curses.color_pair(3))
            quote_text_window.refresh()
            quote_text_window.clear()
            quote_text_window.addstr(get_new_joke())

        elif c == ord('q') or c == ord('Q'):
            break

        stdscr.noutrefresh()
        quote_window.noutrefresh()
        quote_text_window.noutrefresh()
        curses.doupdate()


def do_curses(win):
    global stdscr, quote_window, quote_text_window, quote_pad
    stdscr = win

    init_curses(stdscr)

    # Output the current display size in reverse video
    stdscr.addstr("RANDOM QUOTES", curses.A_REVERSE)
    # Change the rest of the line to reverse video
    stdscr.chgat(-1, curses.A_REVERSE)

    # Set the menu up at the very last line of the screen
    stdscr.addstr(curses.LINES-1, 0, "Press 'R' to request a new quote, 'Q' to quit")
    # Change the R to green
    stdscr.chgat(curses.LINES-1,7, 1, curses.A_BOLD | curses.color_pair(2))
    # Change the Q to red
    stdscr.chgat(curses.LINES-1,35, 1, curses.A_BOLD | curses.color_pair(1))

    # Set up the window to hold the random quotes
    quote_window = curses.newwin(curses.LINES-2,curses.COLS, 1,0)
    # Tell the quote window to pay attention to multi-byte key sequences
    quote_window.keypad(1)
    # Create a sub-window so as to cleanly display the quote without worrying
    # about overwriting the quote window's borders
    quote_text_window = quote_window.subwin(curses.LINES-6,curses.COLS-4, 3,2)
    quote_text_window.attron(curses.color_pair(0))
    quote_text_window.addstr("Press 'R' to get your first quote!")
    # Draw a border around it
    quote_window.box()

    stdscr.noutrefresh()
    quote_window.noutrefresh()
    curses.doupdate()

    main_loop()

    curses.endwin()


if __name__ == '__main__':
    curses.wrapper(do_curses)
