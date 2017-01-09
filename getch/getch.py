import os
if os.name is 'nt':
    try:
        from msvcrt import getch
    except ImportError:
        print('Missing package for assumed windows platform: msvcrt')
        raise
elif os.name is 'posix':
    def getch():
        """
        Gets a single character from STDIO.
        """
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd) # save termios settings
        try:
            # set termios settings to turn off echo, newlines, etc..
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            # restore termios settings
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
