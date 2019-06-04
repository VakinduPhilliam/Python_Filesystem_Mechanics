# Python Pathlib
# pathlib — Object-oriented filesystem paths
# This module offers classes representing filesystem paths with semantics appropriate for different operating systems.
# Path classes are divided between 'pure paths', which provide purely computational operations without I/O, and 'concrete paths', which inherit from pure
# paths but also provide I/O operations.
#

#
# Methods and properties
# Pure paths provide the following methods and properties:
#

#
# PurePath.drive 
# A string representing the drive letter or name, if any:
# 

PureWindowsPath('c:/Program Files/').drive

# OUTPUT: 'c:'

PureWindowsPath('/Program Files/').drive

# OUTPUT: ''

PurePosixPath('/etc').drive

# OUTPUT: ''
 
#
# UNC shares are also considered drives:
# 

PureWindowsPath('//host/share/foo.txt').drive

# OUTPUT: '\\\\host\\share'

#
# PurePath.root 
# A string representing the (local or global) root, if any:
# 

PureWindowsPath('c:/Program Files/').root

# OUTPUT: '\\'

PureWindowsPath('c:Program Files/').root

# OUTPUT: ''

PurePosixPath('/etc').root

# OUTPUT: '/'
 
#
# UNC shares always have a root:
# 

PureWindowsPath('//host/share').root

# OUTPUT: '\\'

#
# PurePath.anchor 
# The concatenation of the drive and root:
# 

PureWindowsPath('c:/Program Files/').anchor

# OUTPUT: 'c:\\'

PureWindowsPath('c:Program Files/').anchor

# OUTPUT: 'c:'

PurePosixPath('/etc').anchor

# OUTPUT: '/'

PureWindowsPath('//host/share').anchor

# OUTPUT: '\\\\host\\share\\'

#
# PurePath.parents 
# An immutable sequence providing access to the logical ancestors of the path:
# 

p = PureWindowsPath('c:/foo/bar/setup.py')
p.parents[0]

# OUTPUT: 'PureWindowsPath('c:/foo/bar')'

p.parents[1]

# OUTPUT: 'PureWindowsPath('c:/foo')'

p.parents[2]

# OUTPUT: 'PureWindowsPath('c:/')'

#
# PurePath.parent 
# The logical parent of the path:
# 

p = PurePosixPath('/a/b/c/d')
p.parent

# OUTPUT: PurePosixPath('/a/b/c')'

# 
# You cannot go past an anchor, or empty path:
# 

p = PurePosixPath('/')
p.parent

# OUTPUT: 'PurePosixPath('/')'

p = PurePosixPath('.')
p.parent

# OUTPUT: 'PurePosixPath('.')'
 
#
# Note:
# This is a purely lexical operation, hence the following behaviour:
# 

p = PurePosixPath('foo/..')
p.parent

# OUTPUT: PurePosixPath('foo')'
 
#
# If you want to walk an arbitrary filesystem path upwards, it is recommended to first call Path.resolve() so as to resolve symlinks and eliminate “..” 
# components.

#
# PurePath.name 
# A string representing the final path component, excluding the drive and root, if any:
# 

PurePosixPath('my/library/setup.py').name

# OUTPUT: 'setup.py'
 
#
# UNC drive names are not considered:
# 

PureWindowsPath('//some/share/setup.py').name

# OUTPUT: 'setup.py'

PureWindowsPath('//some/share').name

# OUTPUT: ''

#
# PurePath.suffix 
# The file extension of the final component, if any:
# 

PurePosixPath('my/library/setup.py').suffix

# OUTPUT: '.py'

PurePosixPath('my/library.tar.gz').suffix

# OUTPUT: '.gz'

PurePosixPath('my/library').suffix

# OUTPUT: ''

#
# PurePath.suffixes 
# A list of the path’s file extensions:
# 

PurePosixPath('my/library.tar.gar').suffixes

# OUTPUT: '['.tar', '.gar']'

PurePosixPath('my/library.tar.gz').suffixes

# OUTPUT: '['.tar', '.gz']'

PurePosixPath('my/library').suffixes

# OUTPUT: '[]'

#
# PurePath.stem 
# The final path component, without its suffix:
# 

PurePosixPath('my/library.tar.gz').stem

# OUTPUT: 'library.tar'

PurePosixPath('my/library.tar').stem

# OUTPUT: 'library'

PurePosixPath('my/library').stem

# OUTPUT: 'library'

#
# PurePath.as_posix() 
# Return a string representation of the path with forward slashes (/):
# 

p = PureWindowsPath('c:\\windows')
str(p)

# OUTPUT: 'c:\\windows'

p.as_posix()

# OUTPUT: 'c:/windows'

#
# PurePath.as_uri() 
# Represent the path as a file URI. ValueError is raised if the path isn’t absolute.
# 

p = PurePosixPath('/etc/passwd')
p.as_uri()

# OUTPUT: 'file:///etc/passwd'

p = PureWindowsPath('c:/Windows')
p.as_uri()

# OUTPUT: 'file:///c:/Windows'

#
# PurePath.is_absolute() 
# Return whether the path is absolute or not.
# A path is considered absolute if it has both a root and (if the flavour allows) a drive:
# 


PurePosixPath('/a/b').is_absolute()

# OUTPUT: 'True'

PurePosixPath('a/b').is_absolute()

# OUTPUT: 'False'

PureWindowsPath('c:/a/b').is_absolute()

# OUTPUT: 'True'

PureWindowsPath('/a/b').is_absolute()

# OUTPUT: 'False'

PureWindowsPath('c:').is_absolute()

# OUTPUT: 'False'

PureWindowsPath('//some/share').is_absolute()

# OUTPUT: 'True'

#
# PurePath.is_reserved() 
# With PureWindowsPath, return True if the path is considered reserved under Windows, False otherwise.
# With PurePosixPath, False is always returned.
# 

PureWindowsPath('nul').is_reserved()

# OUTPUT: 'True'

PurePosixPath('nul').is_reserved()

# OUTPUT: 'False'
 
#
# File system calls on reserved paths can fail mysteriously or have unintended effects.
#

#
# PurePath.joinpath(*other) 
# Calling this method is equivalent to combining the path with each of the other arguments in turn:
 

PurePosixPath('/etc').joinpath('passwd')

# OUTPUT: 'PurePosixPath('/etc/passwd')'

PurePosixPath('/etc').joinpath(PurePosixPath('passwd'))

# OUTPUT: 'PurePosixPath('/etc/passwd')'

PurePosixPath('/etc').joinpath('init.d', 'apache2')

# OUTPUT: 'PurePosixPath('/etc/init.d/apache2')'

PureWindowsPath('c:').joinpath('/Program Files')

# OUTPUT: 'PureWindowsPath('c:/Program Files')'

#
# PurePath.match(pattern) 
# Match this path against the provided glob-style pattern. Return True if matching is successful, False otherwise.
#

# 
# If pattern is relative, the path can be either relative or absolute, and matching is done from the right:
# 

PurePath('a/b.py').match('*.py')

# OUTPUT: 'True'

PurePath('/a/b/c.py').match('b/*.py')

# OUTPUT: 'True'

PurePath('/a/b/c.py').match('a/*.py')

# OUTPUT: 'False'

# 
# If pattern is absolute, the path must be absolute, and the whole path must match:
# 

PurePath('/a.py').match('/*.py')

# OUTPUT: 'True'

PurePath('a/b.py').match('/*.py')

# OUTPUT: 'False'

# 
# As with other methods, case-sensitivity is observed:
# 

PureWindowsPath('b.py').match('*.PY')

# OUTPUT: 'True'

#
# PurePath.relative_to(*other) 
# Compute a version of this path relative to the path represented by other.
# If it’s impossible, ValueError is raised:
# 

p = PurePosixPath('/etc/passwd')
p.relative_to('/')

# OUTPUT: 'PurePosixPath('etc/passwd')'

p.relative_to('/etc')

# OUTPUT: 'PurePosixPath('passwd')'

p.relative_to('/usr')

#
# PurePath.with_name(name). 
# Return a new path with the name changed. If the original path doesn’t have a name, ValueError is raised:
# 

p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
p.with_name('setup.py')

# OUTPUT: 'PureWindowsPath('c:/Downloads/setup.py')'

p = PureWindowsPath('c:/')
p.with_name('setup.py')

#
# PurePath.with_suffix(suffix) 
# Return a new path with the suffix changed.
# If the original path doesn’t have a suffix, the new suffix is appended instead.
# If the suffix is an empty string, the original suffix is removed:
# 

p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
p.with_suffix('.bz2')

# OUTPUT: 'PureWindowsPath('c:/Downloads/pathlib.tar.bz2')'

p = PureWindowsPath('README')
p.with_suffix('.txt')

# OUTPUT: 'PureWindowsPath('README.txt')'

p = PureWindowsPath('README.txt')
p.with_suffix('')

# OUTPUT: 'PureWindowsPath('README')'
