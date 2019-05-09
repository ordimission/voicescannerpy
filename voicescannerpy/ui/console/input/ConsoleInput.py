import os

KEY_ENTER = 13
KEY_ESC = 27
KEY_SPACE = 32
KEY_UP = '\033[A'
KEY_DOWN = '\033[B'
KEY_RIGHT = '\033[C'
KEY_LEFT = '\033[D'
KEY_LAST = '\033[F'
KEY_FIRST = '\033[H'

if os.name == 'nt':
    import msvcrt

    def getch():
        ch = msvcrt.getch()
        return ch
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            tty.setcbreak(fd)
            ch = ord(sys.stdin.read(1))
            if ch == KEY_ESC:
                ch = ch + 256*ord(sys.stdin.read(1))
                ch = ch + 256*256*ord(sys.stdin.read(1))
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


