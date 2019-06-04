# Python GZIP
# gzip — Support for gzip files.
# This module provides a simple interface to compress and decompress files just like the GNU programs gzip and gunzip would.
# The data compression is provided by the zlib module.
# The gzip module provides the GzipFile class, as well as the open(), compress() and decompress() convenience functions.
# The GzipFile class reads and writes gzip-format files, automatically compressing or decompressing the data so that it looks like an ordinary file object.
# 
# Note that additional file formats which can be decompressed by the gzip and gunzip programs, such as those produced by compress and pack, are not
# supported by this module.
#

#
# Example of how to GZIP compress an existing file:
# 

import gzip
import shutil

with open('/home/joe/file.txt', 'rb') as f_in:

    with gzip.open('/home/joe/file.txt.gz', 'wb') as f_out:

              shutil.copyfileobj(f_in, f_out)
