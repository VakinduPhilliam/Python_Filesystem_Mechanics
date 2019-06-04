# Python Pathlib
# pathlib — Object-oriented filesystem paths
# This module offers classes representing filesystem paths with semantics appropriate for different operating systems.
# Path classes are divided between 'pure paths', which provide purely computational operations without I/O, and 'concrete paths', which inherit from pure
# paths but also provide I/O operations.

#
# Concrete Path Methods
# 
# Concrete paths provide the following methods in addition to pure paths methods.
# Many of these methods can raise an OSError if a system call fails (for example because the path doesn’t exist):

#
# classmethod Path.cwd() 
# Return a new path object representing the current directory (as returned by os.getcwd()):
# 

Path.cwd()

# OUTPUT: 'PosixPath('/home/antoine/pathlib')'

#
# classmethod Path.home() 
# Return a new path object representing the user’s home directory (as returned by os.path.expanduser() with ~ construct):
# 

Path.home()

# OUTPUT: 'PosixPath('/home/antoine')'
 
#
# Path.stat() 
# Return information about this path (similarly to os.stat()).
# The result is looked up at each call to this method.
# 

p = Path('setup.py')
p.stat().st_size

# OUTPUT: '956'

p.stat().st_mtime

# OUTPUT: '1327883547.852554'

#
# Path.chmod(mode) 
# Change the file mode and permissions, like os.chmod():
# 

p = Path('setup.py')
p.stat().st_mode

# OUTPUT: '33277'

p.chmod(0o444)
p.stat().st_mode

# OUTPUT: '33060'

#
# Path.exists() 
# Whether the path points to an existing file or directory:
# 

Path('.').exists()

# OUTPUT: 'True'

Path('setup.py').exists()

# OUTPUT: 'True'

Path('/etc').exists()

# OUTPUT: 'True'

Path('nonexistentfile').exists()

# OUTPUT: 'False'
 
#
# Note:
# If the path points to a symlink, exists() returns whether the symlink points to an existing file or directory.
#

#
# Path.expanduser() 
# Return a new path with expanded ~ and ~user constructs, as returned by os.path.expanduser():
# 

p = PosixPath('~/films/Monty Python')

p.expanduser()

# OUTPUT: 'PosixPath('/home/eric/films/Monty Python')'
 
#
# Path.glob(pattern) 
# Glob the given pattern in the directory represented by this path, yielding all matching files (of any kind):
# 

sorted(Path('.').glob('*.py'))

# OUTPUT: '[PosixPath('pathlib.py'), PosixPath('setup.py'), PosixPath('test_pathlib.py')]'

sorted(Path('.').glob('*/*.py'))

# OUTPUT: '[PosixPath('docs/conf.py')]'
 
#
# The “**” pattern means “this directory and all subdirectories, recursively”.
# In other words, it enables recursive globbing:
# 

sorted(Path('.').glob('**/*.py'))

#
# Path.iterdir() 
# When the path points to a directory, yield path objects of the directory contents:
# 

p = Path('docs')

for child in p.iterdir(): child

#
# Path.open(mode='r', buffering=-1, encoding=None, errors=None, newline=None) 
# Open the file pointed to by the path, like the built-in open() function does:
# 

p = Path('setup.py')

    with p.open() as f:

         f.readline()

# OUTPUT: '#!/usr/bin/env python3\n'

#
# Path.read_bytes() 
# Return the binary contents of the pointed-to file as a bytes object:
# 

p = Path('my_binary_file')
p.write_bytes(b'Binary file contents')

# OUTPUT: '20'

p.read_bytes()

# OUTPUT: 'b'Binary file contents''
 
#
# Path.read_text(encoding=None, errors=None) 
# Return the decoded contents of the pointed-to file as a string:
# 

p = Path('my_text_file')
p.write_text('Text file contents')

# OUTPUT: '18'

p.read_text()

# OUTPUT: 'Text file contents'

#
# Path.rename(target) 
# Rename this file or directory to the given target.
# On Unix, if target exists and is a file, it will be replaced silently if the user has permission.
# 'target' can be either a string or another path object:
# 

p = Path('foo')
p.open('w').write('some text')

# OUTPUT: '9'

target = Path('bar')
p.rename(target)

target.open().read()

# OUTPUT: 'some text'

#
# Path.resolve(strict=False) 
# Make the path absolute, resolving any symlinks. A new path object is returned:
# 

p = Path()
p

# OUTPUT: 'PosixPath('.')
p.resolve()

# OUTPUT: 'PosixPath('/home/antoine/pathlib')'
 
#
# “..” components are also eliminated (this is the only method to do so):
# 

p = Path('docs/../setup.py')
p.resolve()

# OUTPUT: 'PosixPath('/home/antoine/pathlib/setup.py')'

#
# Path.rglob(pattern) 
# This is like calling Path.glob() with “**” added in front of the given pattern:
# 

sorted(Path().rglob("*.py"))

#
# Path.samefile(other_path) 
# Return whether this path points to the same file as other_path, which can be either a Path object, or a string.
# The semantics are similar to os.path.samefile() and os.path.samestat().
#

# 
# An OSError can be raised if either file cannot be accessed for some reason.
# 

p = Path('spam')
q = Path('eggs')

p.samefile(q)

# OUTPUT: 'False'

p.samefile('spam')

# OUTPUT: 'True'

#
# Path.symlink_to(target, target_is_directory=False) 
# Make this path a symbolic link to target. Under Windows, target_is_directory must be true (default False) if the link’s target is a directory.
# Under POSIX, target_is_directory’s value is ignored.
# 

p = Path('mylink')

p.symlink_to('setup.py')
p.resolve()

# OUTPUT: 'PosixPath('/home/antoine/pathlib/setup.py')'

p.stat().st_size

# OUTPUT: '956'

p.lstat().st_size

# OUTPUT: '8'

#
# Path.write_bytes(data) 
# Open the file pointed to in bytes mode, write data to it, and close the file:
# 

p = Path('my_binary_file')

p.write_bytes(b'Binary file contents')

# OUTPUT: '20'

p.read_bytes()

# OUTPUT: 'b'Binary file contents''
 
#
# An existing file of the same name is overwritten.
# 

#
# Path.write_text(data, encoding=None, errors=None) 
# Open the file pointed to in text mode, write data to it, and close the file:
# 

p = Path('my_text_file')
p.write_text('Text file contents')

# OUTPUT: '18'

p.read_text()

# OUTPUT: 'Text file contents'
