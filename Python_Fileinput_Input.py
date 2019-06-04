# Python Fileinput
# fileinput — Iterate over lines from multiple input streams.
# This module implements a helper class and functions to quickly write a loop over standard input or a list of files.
# If you just want to read or write one file see open().
#

#
# fileinput.input(files=None, inplace=False, backup='', bufsize=0, mode='r', openhook=None):
# Create an instance of the FileInput class.
# The instance will be used as global state for the functions of this module, and is also returned to use during iteration.
# The parameters to this function will be passed along to the constructor of the FileInput class.
# 

#
# The FileInput instance can be used as a context manager in the with statement.
#

#
# In this example, input is closed after the with statement is exited, even if an exception occurs:
# 

with fileinput.input(files=('spam.txt', 'eggs.txt')) as f:

       for line in f:
 
            process(line)
