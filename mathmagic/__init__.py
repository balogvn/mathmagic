# This is like the front door of our package!

from . import calculator

# lets's make it easy to use our functions

from .calculator import add, subtract, multiply, divide, average, power

# Tell people what version this is 
__version__ = "0.1"