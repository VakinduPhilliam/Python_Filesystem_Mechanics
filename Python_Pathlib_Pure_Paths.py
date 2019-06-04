# Python Pathlib
# pathlib — Object-oriented filesystem paths
# This module offers classes representing filesystem paths with semantics appropriate for different operating systems.
# Path classes are divided between 'pure paths', which provide purely computational operations without I/O, and 'concrete paths', which inherit from pure
# paths but also provide I/O operations.

#
# Pure paths:
# Pure path objects provide path-handling operations which don’t actually access a filesystem.
# There are three ways to access these classes, which we also call flavours:
#

#
# class pathlib.PurePath(*pathsegments) 
# A generic class that represents the system’s path flavour (instantiating it creates either a PurePosixPath or a PureWindowsPath):
# 

PurePath('setup.py')      # Running on a Unix machine

# OUTPUT: 'PurePosixPath('setup.py')'

# 
# Each element of pathsegments can be either a string representing a path segment, an object implementing the os.PathLike interface which returns a string,
# or another path object:
# 

PurePath('foo', 'some/path', 'bar')

# OUTPUT: 'PurePosixPath('foo/some/path/bar')'

PurePath(Path('foo'), Path('bar'))

# OUTPUT: 'PurePosixPath('foo/bar')'

# 
# When pathsegments is empty, the current directory is assumed:
# 

PurePath()

# OUTPUT: 'PurePosixPath('.')'
 
#
# When several absolute paths are given, the last is taken as an anchor (mimicking os.path.join()’s behaviour):
# 

PurePath('/etc', '/usr', 'lib64')

# OUTPUT: 'PurePosixPath('/usr/lib64')'

PureWindowsPath('c:/Windows', 'd:bar')

# OUTPUT: 'PureWindowsPath('d:bar')'

# 
# However, in a Windows path, changing the local root doesn’t discard the previous drive setting:
# 

PureWindowsPath('c:/Windows', '/Program Files')

# OUTPUT: 'PureWindowsPath('c:/Program Files')'
 
#
# Spurious slashes and single dots are collapsed, but double dots ('..') are not, since this would change the meaning of a path in the face of symbolic
# links:
# 

PurePath('foo//bar')

# OUTPUT: 'PurePosixPath('foo/bar')'

PurePath('foo/./bar')

# OUTPUT: 'PurePosixPath('foo/bar')'

PurePath('foo/../bar')

# OUTPUT: 'PurePosixPath('foo/../bar')'
 
#
# (a naïve approach would make PurePosixPath('foo/../bar') equivalent to PurePosixPath('bar'), which is wrong if foo is a symbolic link to another directory)
# 
# Pure path objects implement the os.PathLike interface, allowing them to be used anywhere the interface is accepted.
# 


#
# class pathlib.PurePosixPath(*pathsegments): 
# A subclass of PurePath, this path flavour represents non-Windows filesystem paths:
# 

PurePosixPath('/etc')

# OUTPUT: 'PurePosixPath('/etc')'
 
#
# pathsegments is specified similarly to PurePath.

#
# class pathlib.PureWindowsPath(*pathsegments) 
# A subclass of PurePath, this path flavour represents Windows filesystem paths:
 

PureWindowsPath('c:/Program Files/')

# OUTPUT: 'PureWindowsPath('c:/Program Files')'
 
#
# pathsegments is specified similarly to PurePath.
# 
# Regardless of the system you’re running on, you can instantiate all of these classes, since they don’t provide any operation that does system calls.
#
