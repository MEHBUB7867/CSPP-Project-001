"""Implementing the tac shell command in python."""

import sys
from lib.helper import tac, readfile

TEXT = ""
ARG_CNT = len(sys.argv) - 1

if ARG_CNT == 0:
    TEXT = sys.stdin.read()

if ARG_CNT == 1:
    TEXT = readfile(sys.argv[1])

if ARG_CNT > 1:
    print(sys.argv[0], "doesn't handle more than one argument")

tac(TEXT)