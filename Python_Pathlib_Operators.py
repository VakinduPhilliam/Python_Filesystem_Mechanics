# Python Pathlib
# pathlib — Object-oriented filesystem paths
# This module offers classes representing filesystem paths with semantics appropriate for different operating systems.
# Path classes are divided between 'pure paths', which provide purely computational operations without I/O, and 'concrete paths', which inherit from pure
# paths but also provide I/O operations.

#
# Operators:
# The slash operator helps create child paths, similarly to os.path.join():
 
p = PurePath('/etc')
p

# OUTPUT: 'PurePosixPath('/etc')'

p / 'init.d' / 'apache2'

# OUTPUT: 'PurePosixPath('/etc/init.d/apache2')'

q = PurePath('bin')

'/usr' / q

# OUTPUT: 'PurePosixPath('/usr/bin')'

#
# A path object can be used anywhere an object implementing os.PathLike is accepted:
# 

import os

p = PurePath('/etc')

os.fspath(p)

# OUTPUT: '/etc'
 
#
# The string representation of a path is the raw filesystem path itself (in native form, e.g. with backslashes under Windows), which you can pass to any
# function taking a file path as a string:
# 

p = PurePath('/etc')

str(p)

# OUTPUT: '/etc'

p = PureWindowsPath('c:/Program Files')

str(p)

# OUTPUT: 'c:\\Program Files'

# 
# Similarly, calling bytes on a path gives the raw filesystem path as a bytes object, as encoded by os.fsencode():
# 

bytes(p)

# OUTPUT: 'b'/etc''
 
#
# Note:
# Calling bytes is only recommended under Unix. Under Windows, the unicode form is the canonical representation of filesystem paths.
#
 