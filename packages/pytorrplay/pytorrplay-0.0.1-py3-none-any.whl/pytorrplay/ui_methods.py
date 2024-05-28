# ui_methods.py

import subprocess
import curses


class RofiUI:
    @staticmethod
    def history_menu(history):
        options = ["Search for a new torrent"]
        options.extend([f"{item['title']}" for item in history])
        result = subprocess.run(['rofi', '-dmenu', '-i', '-p', 'Select from History'],
                                input='\n'.join(options), capture_output=True, text=True)
        selected_title = result.stdout.strip()

        if selected_title == "Search for a new torrent" or not selected_title:
            return selected_title

        # Find the selected item in history
        selected_item = next(
            (item for item in history if item['title'] == selected_title), None)
        return selected_item['magnet'] if selected_item else None

    @staticmethod
    def input(prompt):
        result = subprocess.run(['rofi', '-dmenu', '-i', '-p', prompt],
                                capture_output=True, text=True)
        return result.stdout.strip()

    @staticmethod
    def menu(options):
        result = subprocess.run(['rofi', '-dmenu', '-i', '-p', 'Select Torrent'],
                                input='\n'.join(options), capture_output=True, text=True)
        return result.stdout.strip()


class CursesUI:
    @staticmethod
    def history_menu(history):
        def menu(stdscr):
            curses.curs_set(0)
            stdscr.clear()
            options = ["Search for a new torrent"]
            options.extend([f"{item['title']}" for item in history])
            current_row = 0

            while True:
                stdscr.clear()
                h, w = stdscr.getmaxyx()
                for idx, row in enumerate(options):
                    x = 0
                    y = idx
                    if y >= h:
                        break  # Avoid writing outside of the screen bounds
                    if idx == current_row:
                        stdscr.attron(curses.color_pair(1))
                        try:
                            stdscr.addstr(y, x, row)
                        except curses.error:
                            pass  # Handle writing out of bounds gracefully
                        stdscr.attroff(curses.color_pair(1))
                    else:
                        try:
                            stdscr.addstr(y, x, row)
                        except curses.error:
                            pass  # Handle writing out of bounds gracefully
                stdscr.refresh()

                key = stdscr.getch()
                if key == curses.KEY_UP and current_row > 0:
                    current_row -= 1
                elif key == curses.KEY_DOWN and current_row < len(options) - 1:
                    current_row += 1
                elif key in [curses.KEY_ENTER, ord('\n')]:
                    return options[current_row]

        selected_option = curses.wrapper(menu)
        if selected_option == "Search for a new torrent":
            return selected_option

        # Find the selected item in history
        selected_item = next(
            (item for item in history if item['title'] == selected_option), None)
        return selected_item['magnet'] if selected_item else None

    @staticmethod
    def input(prompt):
        def get_input(stdscr):
            curses.echo()
            stdscr.clear()
            stdscr.addstr(0, 0, prompt)
            stdscr.refresh()
            input_value = stdscr.getstr(1, 0).decode('utf-8')
            return input_value

        return curses.wrapper(get_input)

    @staticmethod
    def menu(options):
        def menu(stdscr):
            curses.curs_set(0)
            stdscr.clear()
            current_row = 0

            while True:
                stdscr.clear()
                h, w = stdscr.getmaxyx()
                for idx, row in enumerate(options):
                    x = 0
                    y = idx
                    if y >= h:
                        break  # Avoid writing outside of the screen bounds
                    if idx == current_row:
                        stdscr.attron(curses.color_pair(1))
                        try:
                            stdscr.addstr(y, x, row)
                        except curses.error:
                            pass  # Handle writing out of bounds gracefully
                        stdscr.attroff(curses.color_pair(1))
                    else:
                        try:
                            stdscr.addstr(y, x, row)
                        except curses.error:
                            pass  # Handle writing out of bounds gracefully
                stdscr.refresh()

                key = stdscr.getch()
                if key == curses.KEY_UP and current_row > 0:
                    current_row -= 1
                elif key == curses.KEY_DOWN and current_row < len(options) - 1:
                    current_row += 1
                elif key in [curses.KEY_ENTER, ord('\n')]:
                    return options[current_row]

        return curses.wrapper(menu)


def get_ui(ui_type):
    if ui_type == 'rofi':
        return RofiUI()
    elif ui_type == 'curses':
        return CursesUI()
    else:
        raise ValueError("Invalid UI type. Choose 'rofi' or 'curses'.")
