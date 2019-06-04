# Python Tarfile
# tarfile — Read and write tar archive files.
# The tarfile module makes it possible to read and write tar archives, including those using gzip, bz2 and lzma compression.
# Use the zipfile module to read or write .zip files, or the higher-level functions in shutil.
#

#
# How to create an archive and reset the user information using the filter parameter in TarFile.add():
# 

import tarfile

def reset(tarinfo):
    tarinfo.uid = tarinfo.gid = 0

    tarinfo.uname = tarinfo.gname = "root"

    return tarinfo

tar = tarfile.open("sample.tar.gz", "w:gz")
tar.add("foo", filter=reset)

tar.close()
