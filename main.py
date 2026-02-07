from threading import Thread
from datetime import datetime
# from dateutil.relativedelta import relativedelta
import eel
import pandas as pd
import os.path as pth
import sqlite3
import json
import sys,os
# from pycustomer import *
from Start_screen import StartScreen, select_file_
from tkinter import *
from scripts.util import *


def runner():
    print('EEL  >>>>>> ')
    exit(eel.start('index.html', block=True))
    print('AFTER EEL>>')


if __name__ == "__main__":
    print("WELCOME TO FORMULATO")
    print('Strting..............................')
    mssg = 'صيدلية د. محمد ثروت تتمني لكم دوام الصحة والعافية'
    screen = StartScreen(937, 600)
    screen.title('MTM Pharmacy')
    screen.thr = runner
    screen.wm_attributes('-transparent', True)
    screen.wm_attributes('-topmost', 1)
    screen.config(bg='systemTransparent')
    screen.mainloop()
    print('AFter MAinloop()>>>>>>>>>>>>>')