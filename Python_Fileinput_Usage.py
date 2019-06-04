# Python Fileinput
# fileinput — Iterate over lines from multiple input streams.
# This module implements a helper class and functions to quickly write a loop over standard input or a list of files.
# If you just want to read or write one file see open().
#

# 
# The typical use is:
# 

import fileinput

for line in fileinput.input():

          process(line)
