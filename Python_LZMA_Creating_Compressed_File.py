# Python LZMA
# lzma � Compression using the LZMA algorithm.
# This module provides classes and convenience functions for compressing and decompressing data using the LZMA compression algorithm.
# Also included is a file interface supporting the .xz and legacy .lzma file formats used by the xz utility, as well as raw compressed streams.
# The interface provided by this module is very similar to that of the bz2 module.
# However, note that LZMAFile is not thread-safe, unlike bz2.BZ2File, so if you need to use a single LZMAFile instance from multiple threads, it is
# necessary to protect it with a lock.

#
# Creating a compressed file:
# 

import lzma

data = b"Insert Data Here"

with lzma.open("file.xz", "w") as f:

         f.write(data)
