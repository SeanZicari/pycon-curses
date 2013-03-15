import urwid
from getter import get_new_joke, get_new_quote


palette = [('titlebar', 'black', 'white'),
           ('refresh button', 'dark green,bold', 'black'),
           ('quit button', 'dark red,bold', 'black'),
           ('getting quote', 'dark blue', 'black')]

quote_box = None
main_loop = None


def create_header():
    text = urwid.Text(u'RANDOM QUOTES')
    return urwid.AttrMap(text, 'titlebar')


def create_footer():
    return urwid.Text([u'Press (',
                       ('refresh button', u'R'),
                       u') to get a new quote, Press (',
                       ('quit button', u'Q'),
                       u') to quit'])


def create_quotebox():
    global quote_box
    text = urwid.Text(u"Press (R) for a new quote!")
    filler = urwid.Filler(text, valign='top', top=1, bottom=1)
    v_padding = urwid.Padding(filler, left=1, right=1)
    quote_box = urwid.LineBox(v_padding)
    return quote_box


def create_gui():
    return urwid.Frame(header=create_header(), body=create_quotebox(), footer=create_footer())


def handle_input(key):
    if key == 'Q' or key == 'q':
        raise urwid.ExitMainLoop()
    elif key == 'R' or key == 'r':
        quote_box.base_widget.set_text(('getting quote',
                                               'Getting new quote...'))
        main_loop.draw_screen()
        quote_box.base_widget.set_text(get_new_joke())


if __name__ == '__main__':
    global main_loop
    main_loop = urwid.MainLoop(create_gui(), palette, unhandled_input=handle_input)
    main_loop.run()
