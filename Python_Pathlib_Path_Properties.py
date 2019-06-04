# Python Pathlib
# pathlib — Object-oriented filesystem paths
# This module offers classes representing filesystem paths with semantics appropriate for different operating systems.
# Path classes are divided between 'pure paths', which provide purely computational operations without I/O, and 'concrete paths', which inherit from pure
# paths but also provide I/O operations.

#
# General path properties
# Paths are immutable and hashable. Paths of a same flavour are comparable and orderable.
# These properties respect the flavour’s case-folding semantics:
# 

PurePosixPath('foo') == PurePosixPath('FOO')

# OUTPUT: 'False'

PureWindowsPath('foo') == PureWindowsPath('FOO')

# OUTPUT: 'True'

PureWindowsPath('FOO') in { PureWindowsPath('foo') }

# OUTPUT: 'True'

PureWindowsPath('C:') < PureWindowsPath('d:')

# OUTPUT: 'True'
 
#
# Paths of a different flavour compare unequal and cannot be ordered:
# 

PureWindowsPath('foo') == PurePosixPath('foo')

# OUTPUT: 'False'

PureWindowsPath('foo') < PurePosixPath('foo')
