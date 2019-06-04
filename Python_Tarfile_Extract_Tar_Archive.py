# Python Trafile
# tarfile — Read and write tar archive files.
# The tarfile module makes it possible to read and write tar archives, including those using gzip, bz2 and lzma compression.
# Use the zipfile module to read or write .zip files, or the higher-level functions in shutil.

#
# How to extract an entire tar archive to the current working directory:
# 

import tarfile

tar = tarfile.open("sample.tar.gz")

tar.extractall()

tar.close()
