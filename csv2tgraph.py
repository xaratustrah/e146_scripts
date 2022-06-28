#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Convert CSV to TGraph for fitting

2022 Xaratustrah
'''

from ROOT import TGraph, TCanvas, TFile
import numpy as np
import sys


def process(filename):
    gas = np.genfromtxt(filename, delimiter='|')
    x, y = gas[:,0], gas[:,1]
    # TGraph needs python array not numpy ndarray. so we have to "ravel"
    tg = TGraph(len(x), x.ravel(), y.ravel())
    ff = TFile( filename + '.root', 'RECREATE' )
    tg.Write()
    ff.Close()



def main():

    process(sys.argv[1])


# ------------------------
if __name__ == '__main__':
    main()

