#!/usr/bin/env python

import glob
import shutil
import os


def list_extensions(rootdir):

    filelist = glob.glob(os.path.join(rootdir, '*.*'))
    extensions = [os.path.splitext(x)[-1] for x in filelist]

    return extensions

def sort_extensions(rootdir):

    all_extensions = list_extensions(rootdir)

    for ext in all_extensions:

        dirname = ext[1::]

        try:
            os.mkdir(os.path.join(rootdir, dirname))
        except:
            pass

        filelist = glob.glob(os.path.join(rootdir, '*'+ext))

        for p in filelist:
            if os.path.isdir(dirname):
                shutil.move(p, dirname)
            
    return True


        