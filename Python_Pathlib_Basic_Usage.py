# Python Pathlib
# pathlib — Object-oriented filesystem paths
# This module offers classes representing filesystem paths with semantics appropriate for different operating systems.
# Path classes are divided between 'pure paths', which provide purely computational operations without I/O, and 'concrete paths', which inherit from pure
# paths but also provide I/O operations.

#
# Basic use:
#

# 
# Importing the main class:
# 

from pathlib import Path
 
#
# Listing subdirectories:
# 

p = Path('.')

[x for x in p.iterdir() if x.is_dir()]

# OUTPUT: '[PosixPath('.hg'), PosixPath('docs'), PosixPath('dist'),
#          PosixPath('__pycache__'), PosixPath('build')]'
 
#
# Listing Python source files in this directory tree:
# 

list(p.glob('**/*.py'))

[PosixPath('test_pathlib.py'), PosixPath('setup.py'),

# OUTPUT: ' PosixPath('pathlib.py'), PosixPath('docs/conf.py'),
#           PosixPath('build/lib/pathlib.py')]'
 
#
# Navigating inside a directory tree:
# 

p = Path('/etc')

q = p / 'init.d' / 'reboot'
q


# OUTPUT: 'PosixPath('/etc/init.d/reboot')'

q.resolve()

# OUTPUT: 'PosixPath('/etc/rc.d/init.d/halt')'
 
#
# Querying path properties:
# 

q.exists()

# OUTPUT: 'True'

q.is_dir()

# OUTPUT: 'False'
 
#
# Opening a file:
# 

with q.open() as f: f.readline()

# ...

# OUTPUT: '#!/bin/bash\n'
