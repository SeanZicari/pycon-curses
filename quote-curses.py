import curses
from urllib2 import urlopen, unquote

quote_window = None
quote_text_window = None
main_window = None
quote_pad = None


def init_curses(main_win):
    curses.curs_set(0)
    main_win.keypad(1)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)


def setup_quote_window():
    pass


def main_loop():
    global main_window, quote_window, quote_text_window, qw_size

    while True:
        c = quote_window.getch()

        if c == ord('r') or c == ord('R'):
            quote_text_window.clear()
            quote_text_window.addstr(0,0, get_new_quote())

        elif c == ord('q') or c == ord('Q'):
            break

        main_window.noutrefresh()
        quote_window.noutrefresh()
        quote_text_window.noutrefresh()
        curses.doupdate()


def get_new_quote():
    return unquote(urlopen('http://www.iheartquotes.com/api/v1/random').read())


def do_curses(win):
    global main_window, quote_window, quote_text_window, quote_pad, qw_size
    main_window = win
    qw_size = {'height': 15, 'width': curses.COLS}

    init_curses(main_window)

    # Output the current display size in reverse video
    main_window.addstr("RANDOM QUOTES", curses.A_REVERSE)
    # Change the rest of the line to reverse video
    main_window.chgat(-1, curses.A_REVERSE)

    # Set the menu up at the very last line of the screen
    main_window.addstr(16, 0, "Press 'R' to request a new quote, 'Q' to quit", curses.COLOR_BLUE)
    # Change the R to green
    main_window.chgat(16,7, 1, curses.A_BOLD | curses.color_pair(2))
    # Change the Q to red
    main_window.chgat(16,35, 1, curses.A_BOLD | curses.color_pair(1))

    # Set up the window to hold the random quotes
    quote_window = curses.newwin(qw_size['height'],qw_size['width'], 1,0)
    # Tell the quote window to pay attention to multi-byte key sequences
    quote_window.keypad(1)
    # Create a sub-window so as to cleanly display the quote without worrying
    # about overwriting the quote window's borders
    quote_text_window = quote_window.subwin(qw_size['height']-2, qw_size['width']-2, 2,1)
    quote_text_window.addstr(get_new_quote())
    # Draw a border around it
    quote_window.box()

    main_window.noutrefresh()
    quote_window.noutrefresh()
    curses.doupdate()

    main_loop()

    curses.endwin()


if __name__ == '__main__':
    curses.wrapper(do_curses)
