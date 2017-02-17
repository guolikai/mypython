#!/usr/bin/env python

import re

def count_patt(fname, patt):
    patt_dict = {}
    cpatt = re.compile(patt)
    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                key = m.group()
                if key in patt_dict:
                    patt_dict[key] += 1
                else:
                    patt_dict[key] = 1

    return patt_dict

def sort(adict):
    alist = adict.items()
    result = []
    for i in range(len(alist)):
        greater = alist[0]
        for item in alist[1:]:
            if item[1] > greater[1]:
                greater = item
        result.append(greater)
        alist.remove(greater)

    return result

if __name__ == '__main__':
    httpd_log = '/var/log/httpd/access_log'
    ip_patt = '^(\d+\.){3}\d+'
    br_patt = 'Firefox|MSIE'
    a = count_patt(httpd_log, ip_patt)
    print a
    print sort(a)
    print count_patt(httpd_log, br_patt)
