#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-UM-11"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['QP183+05'] = [ 125277, 125279,  125281, 125287, 125289 ] 
on['PJ1138']   = [125586, 125588, 125590,125592, 125602, 125604, 125759, 125761]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['QP183+05']   = ""
pars1['PJ1138']     = ""

#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2['QP183+05']   = "srdp=1 admit=0"
pars2['PJ1138']     = ""

#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}
pars3['QP183+05']   = "srdp=1 admit=0"
pars3['PJ1138']     = ""

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
