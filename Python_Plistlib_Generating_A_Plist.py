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
# Generating a plist:
# 

pl = dict(
    aString = "Doodah",
    aList = ["A", "B", 12, 32.1, [1, 2, 3]],
    aFloat = 0.1,
    anInt = 728,
    aDict = dict(
        anotherString = "<hello & hi there!>",
        aThirdString = "M\xe4ssig, Ma\xdf",
        aTrueValue = True,
        aFalseValue = False,
    ),
    someData = b"<binary gunk>",
    someMoreData = b"<lots of binary gunk>" * 10,
    aDate = datetime.datetime.fromtimestamp(time.mktime(time.gmtime())),
)

with open(fileName, 'wb') as fp:
    dump(pl, fp)
