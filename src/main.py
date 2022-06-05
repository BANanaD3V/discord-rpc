import asyncio
import curses
import time
import os
from pypresence import Presence

from config import *
from dotenv import load_dotenv

load_dotenv()  
client_id = os.getenv("client_id")  
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() 
class MenuDisplay:

    def __init__(self, menu):
        # set menu parameter as class property
        self.menu = menu
        # run curses application
        curses.wrapper(self.mainloop)

    def mainloop(self, stdscr):
        # turn off cursor blinking
        curses.curs_set(0)

        # color scheme for selected row
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        # set screen object as class property
        self.stdscr = stdscr

        # get screen height and width
        self.screen_height, self.screen_width = self.stdscr.getmaxyx()

        # specify the current selected row
        current_row = 0

        # print the menu
        self.print_menu(current_row)

        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(self.menu) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_row == len(self.menu) - 1:
                    self.print_center("You selected '{}'. Press enter to confirm.".format(list(activity_choices.values())[current_row]['action']))
                else:
                    self.print_center("You selected '{}'. Press enter to return to activity selection.".format(list(activity_choices.values())[current_row]['action']))
                RPC.update(
                    state=list(map(lambda v: v["action"], activity_choices.values()))[current_row], 
                    details=details,
                    start=time.time(),
                    large_image=large_image,
                    small_image=list(map(lambda v: v["icon"], activity_choices.values()))[current_row],
                    buttons=buttons_list,
                    large_text = large_text,
                    small_text = small_text
                    
                )
                self.stdscr.getch()
                # if user selected last row (Exit), confirm before exit the program
                if current_row == len(self.menu) - 1:
                    if self.confirm("Are you sure you want to exit? (use right and left arrows to select)"):
                        RPC.close()
                        break

            self.print_menu(current_row)

    def print_menu(self, selected_row_idx):
        self.stdscr.clear()
        for idx, row in enumerate(self.menu):
            x = self.screen_width // 2 - len(row) // 2
            y = self.screen_height // 2 - len(menu) // 2 + idx
            if idx == selected_row_idx:
                self.color_print(y, x, row, 1)
            else:
                self.stdscr.addstr(y, x, row)
        self.stdscr.addstr(1, 0, "use up and down arrows to cycle through activities.")
        self.stdscr.addstr(2, 0, "use enter to select activity.")
        self.stdscr.refresh()

    def color_print(self, y, x, text, pair_num):
        self.stdscr.attron(curses.color_pair(pair_num))
        self.stdscr.addstr(y, x, text)
        self.stdscr.attroff(curses.color_pair(pair_num))

    def print_confirm(self, selected="yes"):
        # clear yes/no line
        curses.setsyx(self.screen_height // 2 + 1, 0)
        self.stdscr.clrtoeol()

        y = self.screen_height // 2 + 1
        options_width = 10

        # print yes
        option = "yes"
        x = self.screen_width // 2 - options_width // 2 + len(option)
        if selected == option:
            self.color_print(y, x, option, 1)
        else:
            self.stdscr.addstr(y, x, option)

        # print no
        option = "no"
        x = self.screen_width // 2 + options_width // 2 - len(option)
        if selected == option:
            self.color_print(y, x, option, 1)
        else:
            self.stdscr.addstr(y, x, option)

        self.stdscr.refresh()

    def confirm(self, confirmation_text):
        self.print_center(confirmation_text)

        current_option = "yes"
        self.print_confirm(current_option)

        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_RIGHT and current_option == "yes":
                current_option = "no"
            elif key == curses.KEY_LEFT and current_option == "no":
                current_option = "yes"
            elif key == curses.KEY_ENTER or key in [10, 13]:
                return True if current_option == "yes" else False

            self.print_confirm(current_option)

    def print_center(self, text):
        self.stdscr.clear()
        x = self.screen_width // 2 - len(text) // 2
        y = self.screen_height // 2
        self.stdscr.addstr(y, x, text)
        self.stdscr.refresh()


if __name__ == "__main__":
    menu = list(activity_choices.keys())
    MenuDisplay(menu)
