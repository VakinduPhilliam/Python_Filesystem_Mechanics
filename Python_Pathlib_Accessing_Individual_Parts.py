# Python Pathlib
# pathlib — Object-oriented filesystem paths
# This module offers classes representing filesystem paths with semantics appropriate for different operating systems.
# Path classes are divided between 'pure paths', which provide purely computational operations without I/O, and 'concrete paths', which inherit from pure
# paths but also provide I/O operations.

#
# Accessing individual parts
#

# 
# To access the individual “parts” (components) of a path, use the following property:
# PurePath.parts 
# A tuple giving access to the path’s various components:
# 

p = PurePath('/usr/bin/python3')

p.parts

# OUTPUT: '('/', 'usr', 'bin', 'python3')'

p = PureWindowsPath('c:/Program Files/PSF')

p.parts

# OUTPUT: '('c:\\', 'Program Files', 'PSF')'

# 
# (note how the drive and local root are regrouped in a single part)
#