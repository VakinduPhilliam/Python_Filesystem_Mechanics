# Python Plistlib
# plistlib — Generate and parse Mac OS X .plist files
# This module provides an interface for reading and writing the “property list” files used mainly by Mac OS X and supports both binary and XML plist files.
# The property list (.plist) file format is a simple serialization supporting basic object types, like dictionaries, lists, numbers and strings. Usually the
# top level object is a dictionary.
# To write out and to parse a plist file, use the dump() and load() functions.
# To work with plist data in bytes objects, use dumps() and loads().
# Values can be strings, integers, floats, booleans, tuples, lists, dictionaries (but only with string keys), Data, bytes, bytesarray or datetime.datetime 
# objects.

#
# Parsing a plist:
# 

with open(fileName, 'rb') as fp:

        pl = load(fp)

print(pl["aKey"])
