# This is a sample Python script.
import time

from physities.src.unit import *


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    Ms = Meter / Second
    Kh = Kilometer / Hour
    v1 = Ms(40)
    v2 = Kh(144)
    v3 = v2.convert(Ms)
    l = v3 * v1
    c = v1 == v2
    print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
