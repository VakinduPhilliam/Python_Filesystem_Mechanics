# Python Tarfile
# tarfile — Read and write tar archive files.
# The tarfile module makes it possible to read and write tar archives, including those using gzip, bz2 and lzma compression.
# Use the zipfile module to read or write .zip files, or the higher-level functions in shutil.
#

#
# How to extract a subset of a tar archive with TarFile.extractall() using a generator function instead of a list:
# 

import os
import tarfile

def py_files(members):
    for tarinfo in members:

        if os.path.splitext(tarinfo.name)[1] == ".py":
            yield tarinfo

tar = tarfile.open("sample.tar.gz")
tar.extractall(members=py_files(tar))

tar.close()
