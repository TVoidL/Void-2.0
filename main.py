from time import sleep
from core import engine
import plataform

try:
    engine.init_curses()

    buffer.add_str(1, 1, "Press: Alt + Enter")

    while:
        sleep(0.08)
        key = stdscr.getch()
        if key == 27:  # Código de ESC/ALT
            next_key = stdscr.getch()  # Captura a próxima tecla
            if next_key in (10, 13):  # ENTER (\n ou \r)
                break

    engine.end_curses()
    engine.wrapper()
except Exception as e:
    print(e)
    input()
