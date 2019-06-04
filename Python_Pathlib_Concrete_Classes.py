# Python Pathlib
# pathlib — Object-oriented filesystem paths
# This module offers classes representing filesystem paths with semantics appropriate for different operating systems.
# Path classes are divided between 'pure paths', which provide purely computational operations without I/O, and 'concrete paths', which inherit from pure
# paths but also provide I/O operations.

#
# Concrete paths
# Concrete paths are subclasses of the pure path classes. In addition to operations provided by the latter, they also provide methods to do system calls on
# path objects.
# There are three ways to instantiate concrete paths:
#

#
# class pathlib.Path(*pathsegments) 
# A subclass of PurePath, this class represents concrete paths of the system’s path flavour (instantiating it creates either a PosixPath or a WindowsPath):
# 

Path('setup.py')

# OUTPUT: 'PosixPath('setup.py')'
 
#
# pathsegments is specified similarly to PurePath.
#

#
# class pathlib.PosixPath(*pathsegments) 
# A subclass of Path and PurePosixPath, this class represents concrete non-Windows filesystem paths:
# 

PosixPath('/etc')

# OUTPUT: 'PosixPath('/etc')'
 
#
# pathsegments is specified similarly to PurePath.
#

#
# class pathlib.WindowsPath(*pathsegments) 
# A subclass of Path and PureWindowsPath, this class represents concrete Windows filesystem paths:
# 

WindowsPath('c:/Program Files/')

# OUTPUT: 'WindowsPath('c:/Program Files')'
 
#
# pathsegments is specified similarly to PurePath.
#


#
# 
# You can only instantiate the class flavour that corresponds to your system (allowing system calls on non-compatible path flavours could lead to bugs or
# failures in your application):
# 
#

import os

os.name

# OUTPUT: 'posix'

Path('setup.py')

# OUTPUT: 'PosixPath('setup.py')'

PosixPath('setup.py')

# OUTPUT: 'PosixPath('setup.py')'

WindowsPath('setup.py')
