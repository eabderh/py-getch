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
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
