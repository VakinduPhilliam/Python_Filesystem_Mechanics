# Python Tarfile
# tarfile — Read and write tar archive files.
# The tarfile module makes it possible to read and write tar archives, including those using gzip, bz2 and lzma compression.
# Use the zipfile module to read or write .zip files, or the higher-level functions in shutil.
#

#
# How to read a gzip compressed tar archive and display some member information:
# 

import tarfile

tar = tarfile.open("sample.tar.gz", "r:gz")

for tarinfo in tar:
    print(tarinfo.name, "is", tarinfo.size, "bytes in size and is", end="")

    if tarinfo.isreg():
        print("a regular file.")

    elif tarinfo.isdir():
        print("a directory.")

    else:
        print("something else.")

tar.close()
