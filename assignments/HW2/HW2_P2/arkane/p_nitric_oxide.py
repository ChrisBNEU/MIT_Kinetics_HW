#!/usr/bin/env python
# -*- coding: utf-8 -*-

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'b3lyp/6-31G(d,p)': Log('p_nitric_oxide.out'),
}

geometry = Log('p_nitric_oxide.out')

frequencies = Log('p_nitric_oxide.out')

"""pivot are the two atoms that are attached to the rotor
top contains the atoms that are being rotated including one of the atoms from pivots
symmetry is the symmetry number of the scan
fit is fit of the scan data. It defaults to 'best', but can also be assigned as 'cosine' or 'fourier'
Principally, the rotor symmetry can be automatically determined by Arkane, but could also be given by the user
(then the user's input overrides Arkane's determination):
rotors = [HinderedRotor(scanLog=Log('ethyl_scan_72.log'), pivots=[1,2], top=[1,3,4], symmetry=6, fit='best')]"""

