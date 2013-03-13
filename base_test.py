import curses

def the_program(stdscr):
    test_window = curses.newwin(5,5, 2,0)
    test_window.addstr(1,1, "E")
    test_window.refresh()
    test_window.getch()
    

curses.wrapper(the_program)