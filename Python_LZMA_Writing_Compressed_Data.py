# Python LZMA
# lzma — Compression using the LZMA algorithm.
# This module provides classes and convenience functions for compressing and decompressing data using the LZMA compression algorithm.
# Also included is a file interface supporting the .xz and legacy .lzma file formats used by the xz utility, as well as raw compressed streams.
# The interface provided by this module is very similar to that of the bz2 module.
# However, note that LZMAFile is not thread-safe, unlike bz2.BZ2File, so if you need to use a single LZMAFile instance from multiple threads, it is
# necessary to protect it with a lock.

#
# Writing compressed data to an already-open file:
# 

import lzma

with open("file.xz", "wb") as f:

        f.write(b"This data will not be compressed\n")

    with lzma.open(f, "w") as lzf:

               lzf.write(b"This *will* be compressed\n")

    f.write(b"Not compressed\n")
