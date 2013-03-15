import urwid
from getter import get_new_joke, get_new_quote


palette = [('titlebar', 'black', 'white'),
           ('refresh button', 'dark green,bold', 'black'),
           ('quit button', 'dark red,bold', 'black'),
           ('getting quote', 'dark blue', 'black')]


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
    text = urwid.Text(u"Press (R) for a new quote!")
    filler = urwid.Filler(text, valign='top', top=1, bottom=1)
    v_padding = urwid.Padding(filler, left=1, right=1)
    return urwid.LineBox(v_padding)


def create_gui(body):
    return urwid.Frame(header=create_header(), body=body, footer=create_footer())


def run():
    def handle_input(key):
        if key == 'Q' or key == 'q':
            raise urwid.ExitMainLoop()
        elif key == 'R' or key == 'r':
            quote_box.base_widget.set_text(('getting quote',
                                                   'Getting new quote...'))
            main_loop.draw_screen()
            quote_box.base_widget.set_text(get_new_joke())

    quote_box = create_quotebox()
    main_loop = urwid.MainLoop(create_gui(quote_box), palette, unhandled_input=handle_input)
    main_loop.run()


if __name__ == '__main__':
    run()
