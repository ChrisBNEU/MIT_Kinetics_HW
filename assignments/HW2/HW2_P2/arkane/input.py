#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This example also generates YAML files for all species and TS
# A YAML file is generated for species if they're structure is defined and Thermo() is called,
# and for TS if all the respective reactant/s and product/s have structures

modelChemistry = "b3lyp/6-31g(d,p)"
useHinderedRotors = False
useBondCorrections = False

species('r_no2', 'r_no2.py',
       structure=SMILES('N(=O)[O]'))
species('r_hydroxylamine', 'r_hydroxylamine.py',
       structure=SMILES('NO'))
species('p_hono', 'p_hono.py',
       structure=SMILES('N(=O)O'))
species('p_nitric_oxide', 'p_nitric_oxide.py',
       structure=SMILES('N[O]'))
transitionState('ts', 'ts.py')

thermo('r_no2','NASA')
thermo('r_hydroxylamine','NASA')
thermo('p_hono','NASA')
thermo('p_nitric_oxide','NASA')

reaction(
    label = 'r_no2 + r_hydroxylamine <=> p_hono + p_nitric_oxide',
    reactants = ['r_no2', 'r_hydroxylamine'],
    products = ['p_hono', 'p_nitric_oxide'],
    transitionState = 'ts',
    tunneling='Eckart',
)

statmech('ts')
kinetics(
    label = 'r_no2 + r_hydroxylamine <=> p_hono + p_nitric_oxide',
    Tmin = (400,'K'), Tmax = (1200,'K'), Tcount = 6, # this can be changed to any desired temperature range with any number of temperatures
    Tlist = ([400,500,700,900,1100,1200],'K'),
    )
