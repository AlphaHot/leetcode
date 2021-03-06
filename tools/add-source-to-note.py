#!/usr/bin/env python3
#
# grep source_base_url ../README.adoc | awk -F\| '{print $2}' | awk -F/ '{print $2}' | awk -F\[ '{print $1}' | tee -a sourcs.txt
#

import os, re

idToFile = {}
for f in os.listdir('../docs/'):
    if f.endswith('.adoc'):
        idToFile[f[0:4]] = "../docs/"+f

with open('./sourcs.txt', 'rb') as fh:
    for nb in fh.readlines():
        name = nb.decode("utf-8").strip()
        id = name[1:5]

#         if int(id) > 5:
#             break

        f = open(idToFile[id], "a")

        f.write("\n\n")
        f.write('[[src-%s]]\n'%(id))
        f.write('[source,{java_source_attr}]\n')
        f.write('----\n')
        f.write('include::{sourcedir}/%s[]\n'%(name))
        f.write('----')
        f.write("\n\n")
        f.close()
        print(name, " OK…")


