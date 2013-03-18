import urwid
from urllib2 import urlopen
from HTMLParser import HTMLParser
from simplejson import loads


# Set up our color scheme
palette = [('titlebar', 'black', 'white'),
           ('refresh button', 'dark green,bold', 'black'),
           ('quit button', 'dark red,bold', 'black'),
           ('getting quote', 'dark blue', 'black')]


# Create the "RANDOM QUOTES" header
header_text = urwid.Text(u'RANDOM QUOTES')
header = urwid.AttrMap(header_text, 'titlebar')

# Create the menu (will display on bottom of screen)
menu = urwid.Text([u'Press (', ('refresh button', u'R'),
                   u') to get a new quote. Press (', ('quit button', u'Q'),
                   u') to quit.'])

# Create the actual quote box
quote_text = urwid.Text(u'Press (R) to get your first quote!')
quote_filler = urwid.Filler(quote_text, valign='top', top=1, bottom=1)
v_padding = urwid.Padding(quote_filler, left=1, right=1)
quote_box = urwid.LineBox(v_padding)

# Assemble the widgets into the widget layout
layout = urwid.Frame(header=header, body=quote_box, footer=menu)


def get_new_joke():
    joke_json = loads(urlopen('http://api.icndb.com/jokes/random').read())
    return HTMLParser().unescape(joke_json['value']['joke']).encode('utf-8')


# Handle key presses
def handle_input(key):
    if key == 'R' or key == 'r':
        quote_box.base_widget.set_text(('getting quote', 'Getting new quote...'))
        main_loop.draw_screen()
        quote_box.base_widget.set_text(get_new_joke())

    elif key == 'Q' or key == 'q':
        raise urwid.ExitMainLoop()


# Create the event loop
main_loop = urwid.MainLoop(layout, palette, unhandled_input=handle_input)

# Kick off the program
main_loop.run()
