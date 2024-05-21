import curses

screen = curses.initscr()
# print("Screen initialized.")
screen.addstr(0, 0, "This string gets printed at position (0, 0)")
screen.addstr(3, 1, "Try Russian text: Привет")  # Python 3 required for unicode
screen.addstr(4, 4, "X")
screen.addch(5, 5, "Y")
# screen.refresh()

# curses.napms(2000)
# curses.endwin()

# print("Window ended.")
