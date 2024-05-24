"""
a simple class to change text colors in a terminal
only works on supported terminals eg. xterm-256color
usage: fgcolors.WARNING + "some text" + fgcolors.ENDC
"""
__author__ = "(AA)"
__copyright__ = "C8"

class fgcolors:
    OKBLUE = '\033[94m'
    OK = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

