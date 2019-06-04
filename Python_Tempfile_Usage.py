# Python Tempfile
# tempfile — Generate temporary files and directories
# This module creates temporary files and directories. It works on all supported platforms.
# TemporaryFile, NamedTemporaryFile, TemporaryDirectory, and SpooledTemporaryFile are high-level interfaces which provide automatic cleanup and can be used
# as context managers.
# mkstemp() and mkdtemp() are lower-level functions which require manual cleanup.
# 
# All the user-callable functions and constructors take additional arguments which allow direct control over the location and name of temporary files and
# directories.
# Files names used by this module include a string of random characters which allows those files to be securely created in shared temporary directories.
# To maintain backward compatibility, the argument order is somewhat odd; it is recommended to use keyword arguments for clarity.
#

#
# Here are some examples of typical usage of the tempfile module:
# 

import tempfile

# create a temporary file and write some data to it

fp = tempfile.TemporaryFile()
fp.write(b'Hello world!')

# read data from file

fp.seek(0)
fp.read()

# OUTPUT: 'b'Hello world!''

# close the file, it will be removed

fp.close()

# create a temporary file using a context manager

with tempfile.TemporaryFile() as fp:

        fp.write(b'Hello world!')

        fp.seek(0)

        fp.read()

# OUTPUT: 'b'Hello world!''

# file is now closed and removed

# create a temporary directory using the context manager

with tempfile.TemporaryDirectory() as tmpdirname:

           print('created temporary directory', tmpdirname)

# directory and contents have been removed
