import os

KEY_ENTER = 13
KEY_ESC = 27
KEY_SPACE = 32
KEY_FIRST = 70
KEY_LAST = 76
KEY_UP = '\033[A'
KEY_DOWN = '\033[B'
KEY_RIGHT = '\033[C'
KEY_LEFT = '\033[D'

if os.name == 'nt':
    import msvcrt

    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.buffer.raw.read(4).decode(sys.stdin.encoding)
            if len(ch) == 1:
                if ord(ch) < 32 or ord(ch) > 126:
                    ch = ord(ch)
            elif ord(ch[0]) == 27:
                ch = '\033' + ch[1:]
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
