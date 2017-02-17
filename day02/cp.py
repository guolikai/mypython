#!/usr/bin/env python

src_fname = '/bin/ls'
dst_fname = '/root/ls'

src_fobj = open(src_fname)
dst_fobj = open(dst_fname, 'w')

while True:
    data = src_fobj.read(4096)
    if data == '':
        break
    dst_fobj.write(data)

src_fobj.close()
dst_fobj.close()
