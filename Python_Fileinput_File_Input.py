# Python Fileinput
# fileinput — Iterate over lines from multiple input streams.
# This module implements a helper class and functions to quickly write a loop over standard input or a list of files.
# If you just want to read or write one file see open().
#

#
# class fileinput.FileInput(files=None, inplace=False, backup='', bufsize=0, mode='r', openhook=None):
# Class FileInput is the implementation; its methods filename(), fileno(), lineno(), filelineno(), isfirstline(), isstdin(), nextfile() and close()
# correspond to the functions of the same name in the module.
#
# In addition it has a readline() method which returns the next input line, and a __getitem__() method which implements the sequence behavior.
# The sequence must be accessed in strictly sequential order; random access and readline() cannot be mixed.
# 
# With mode you can specify which file mode will be passed to open(). It must be one of 'r', 'rU', 'U' and 'rb'.
# 
# The openhook, when given, must be a function that takes two arguments, filename and mode, and returns an accordingly opened file-like object.
# You cannot use inplace and openhook together.
# 
# A FileInput instance can be used as a context manager in the with statement.
#

#
# In this example, input is closed after the with statement is exited, even if an exception occurs:
# 

with FileInput(files=('spam.txt', 'eggs.txt')) as input:

            process(input)
