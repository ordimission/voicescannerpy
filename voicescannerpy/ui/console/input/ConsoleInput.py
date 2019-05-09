import os

KEY_ENTER = 13
KEY_ESC = 27
KEY_SPACE = 32
KEY_UP = 4283163
KEY_DOWN = 4348699
KEY_RIGHT = 4414235
KEY_LEFT = 4479771
KEY_LAST = 4741915
KEY_FIRST = 4610843

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
                ch2 = ord(sys.stdin.read(1))
                ch = ch + 256 * ch2
                ch3 = ord(sys.stdin.read(1))
                ch = ch + 256 * 256 * ch3
                if ch2 == 91 and ch3 in range(50, 53):
                    ch4 = ord(sys.stdin.read(1))
                    ch = ch + 256 * 256 * ch4
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

#goon = 1
#while goon:
#    ch = getch()
#    print(ch)
#    if ch == KEY_SPACE:
#        goon = 0


