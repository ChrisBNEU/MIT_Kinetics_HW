#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This example also generates YAML files for all species and TS
# A YAML file is generated for species if they're structure is defined and Thermo() is called,
# and for TS if all the respective reactant/s and product/s have structures

modelChemistry = "b3lyp/6-31g(d,p)"
useHinderedRotors = False
useBondCorrections = False

species('CH3', 'ch3.py',
       structure=SMILES('[CH3.]'))
species('C2H4', 'ethene.py',
       structure=SMILES('C=C'))
species('C3H7', 'propene.py',
       structure=SMILES('[CH2]CC'))
transitionState('TS', 'TS.py')

thermo('CH3','NASA')
thermo('C2H4','NASA')
thermo('C3H7','NASA')

reaction(
    label = 'CH3 + C2H4 <=> C3H7',
    reactants = ['CH3', 'C2H4'],
    products = ['C3H7'],
    transitionState = 'TS',
    tunneling='Eckart',
)

statmech('TS')
kinetics(
    label = 'CH3 + C2H4 <=> C3H7',
    Tmin = (300,'K'), Tmax = (1000,'K'), Tcount = 8, # this can be changed to any desired temperature range with any number of temperatures
    Tlist = ([300,400,500,600,700,800,900,1000],'K'),
    )
