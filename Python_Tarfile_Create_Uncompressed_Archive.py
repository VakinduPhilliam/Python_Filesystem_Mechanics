# Python Tarfile
# tarfile — Read and write tar archive files.
# The tarfile module makes it possible to read and write tar archives, including those using gzip, bz2 and lzma compression.
# Use the zipfile module to read or write .zip files, or the higher-level functions in shutil.
#

#
# How to create an uncompressed tar archive from a list of filenames:
# 

import tarfile

tar = tarfile.open("sample.tar", "w")

for name in ["foo", "bar", "quux"]:
    tar.add(name)

tar.close()
 
#
# The same example using the with statement:
# 

import tarfile

with tarfile.open("sample.tar", "w") as tar:
    for name in ["foo", "bar", "quux"]:

        tar.add(name)
