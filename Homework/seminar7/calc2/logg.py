import os
import sys
from datetime import datetime as dt


def write_log(*args):
    with open(os.path.join(sys.path[0],'calc.log'), 'a', encoding='utf-8') as logfile:
        logfile.write('\t'.join(list(map(lambda x: str(x), args)))+'\n')


def t():
    return dt.now().strftime('%D\t%H:%M:%S')