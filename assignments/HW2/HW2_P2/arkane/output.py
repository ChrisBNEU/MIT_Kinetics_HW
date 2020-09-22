# Coordinates for r_no2 in Input Orientation (angstroms):
#   N   -0.0000   -0.3280    0.0000
#   O    1.1073    0.1435    0.0000
#   O   -1.1073    0.1437    0.0000
conformer(
    label = 'r_no2',
    E0 = (
        -302.775,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(45.9929, 'amu')),
        NonlinearRotor(
            inertia = ([41.3913, 39.2247, 2.16661], 'amu*angstrom^2'),
            symmetry = 2,
        ),
        HarmonicOscillator(frequencies=([719.751, 1348.86, 1653.01], 'cm^-1')),
    ],
    spin_multiplicity = 2,
    optical_isomers = 1,
)

# Coordinates for r_hydroxylamine in Input Orientation (angstroms):
#   N   -0.7301    0.0055    0.1038
#   O    0.7051   -0.0141   -0.0914
#   H    0.9812   -0.6885    0.5433
#   H   -0.9288    0.9893    0.3032
#   H   -1.0988   -0.1529   -0.8374
conformer(
    label = 'r_hydroxylamine',
    E0 = (
        -346.011,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(33.0215, 'amu')),
        NonlinearRotor(
            inertia = ([20.0185, 20.0086, 2.66503], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([384.847, 897.177, 1118.13, 1275.39, 1353.8, 1608.51, 3292.17, 3374.43, 3658.78], 'cm^-1'),
        ),
    ],
    spin_multiplicity = 1,
    optical_isomers = 1,
)

# Coordinates for p_hono in Input Orientation (angstroms):
#   N   -0.3379   -0.3950   -0.0002
#   O    1.0807   -0.2366   -0.0001
#   H    1.3928   -1.1576    0.0024
#   O   -0.8726    0.6553    0.0001
conformer(
    label = 'p_hono',
    E0 = (
        -397.438,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(47.0007, 'amu')),
        NonlinearRotor(
            inertia = ([45.7095, 40.2422, 5.46724], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([571.242, 605.967, 827.353, 1254.6, 1723.09, 3609.24], 'cm^-1'),
        ),
    ],
    spin_multiplicity = 1,
    optical_isomers = 1,
)

# Coordinates for p_nitric_oxide in Input Orientation (angstroms):
#   N    0.5718    0.0803    0.1969
#   O   -0.6205   -0.0992   -0.2403
#   H    0.9637    1.0237    0.1798
#   H    0.9392   -0.5650    0.8988
conformer(
    label = 'p_nitric_oxide',
    E0 = (
        -260.566,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(32.0136, 'amu')),
        NonlinearRotor(
            inertia = ([16.4348, 14.9691, 1.59961], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([449.081, 1228.57, 1333.3, 1609.65, 3259.02, 3383.42], 'cm^-1'),
        ),
    ],
    spin_multiplicity = 2,
    optical_isomers = 1,
)

# Coordinates for ts in Input Orientation (angstroms):
#   N   -0.7363   -1.2880   -1.1839
#   H   -1.7187   -1.5108   -1.3485
#   H   -0.4624   -1.2111   -0.1815
#   O   -0.4233   -0.1570   -1.8604
#   H    0.1711    0.3839   -1.2042
#   O    0.6403    0.9896    0.0965
#   N    0.1991    0.1597    0.9522
#   O    0.3799    0.3025    2.1389
conformer(
    label = 'ts',
    E0 = (
        -626.174,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(79.0144, 'amu')),
        NonlinearRotor(
            inertia = ([231.623, 193.649, 39.6665], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([109.665, 174.647, 199.284, 287.308, 395.863, 643.294, 776.873, 960.068, 1049.67, 1190.56, 1289.31, 1515.21, 1562.71, 1606.82, 2264.94, 2957.18, 3373.12], 'cm^-1'),
        ),
    ],
    spin_multiplicity = 2,
    optical_isomers = 1,
    frequency = (
        -417.985,
        'cm^-1',
    ),
)

# Thermodynamics for r_no2:
#   Enthalpy of formation (298 K)   =   -69.923 kcal/mol
#   Entropy of formation (298 K)    =    57.421 cal/(mol*K)
#    =========== =========== =========== =========== ===========
#    Temperature Heat cap.   Enthalpy    Entropy     Free energy
#    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
#    =========== =========== =========== =========== ===========
#            300       8.931     -69.905      57.480     -87.149
#            400       9.669     -68.975      60.150     -93.035
#            500      10.388     -67.972      62.386     -99.165
#            600      11.014     -66.901      64.337    -105.503
#            800      11.907     -64.602      67.638    -118.712
#           1000      12.493     -62.158      70.362    -132.520
#           1500      13.224     -55.696      75.593    -169.085
#           2000      13.482     -49.010      79.438    -207.886
#           2400      13.615     -43.590      81.908    -240.169
#    =========== =========== =========== =========== ===========
thermo(
    label = 'r_no2',
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.03074, -0.00206322, 1.80931e-05, -2.30185e-08, 9.32025e-12, -36414.8, 5.92785],
                Tmin = (10, 'K'),
                Tmax = (783.479, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.07784, 0.00613146, -3.97077e-06, 1.18018e-09, -1.32167e-13, -36367.6, 9.64032],
                Tmin = (783.479, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (
            -302.763,
            'kJ/mol',
        ),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (58.2013, 'J/(mol*K)'),
    ),
)

# Thermodynamics for r_hydroxylamine:
#   Enthalpy of formation (298 K)   =   -80.062 kcal/mol
#   Entropy of formation (298 K)    =    56.214 cal/(mol*K)
#    =========== =========== =========== =========== ===========
#    Temperature Heat cap.   Enthalpy    Entropy     Free energy
#    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
#    =========== =========== =========== =========== ===========
#            300      10.656     -80.041      56.285     -96.927
#            400      12.169     -78.900      59.559    -102.723
#            500      13.579     -77.611      62.429    -108.825
#            600      14.839     -76.189      65.018    -115.200
#            800      16.947     -73.002      69.588    -128.672
#           1000      18.597     -69.441      73.554    -142.995
#           1500      21.301     -59.397      81.662    -181.890
#           2000      22.818     -48.335      88.016    -224.367
#           2400      23.620     -39.039      92.251    -260.441
#    =========== =========== =========== =========== ===========
thermo(
    label = 'r_hydroxylamine',
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.02604, -0.00215997, 3.61452e-05, -5.56852e-08, 2.89876e-11, -41615.5, 4.8241],
                Tmin = (10, 'K'),
                Tmax = (491.087, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.33056, 0.0116502, -6.03761e-06, 1.57987e-09, -1.64824e-13, -41449, 11.7981],
                Tmin = (491.087, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (
            -346.01,
            'kJ/mol',
        ),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (108.088, 'J/(mol*K)'),
    ),
)

# Thermodynamics for p_hono:
#   Enthalpy of formation (298 K)   =   -92.358 kcal/mol
#   Entropy of formation (298 K)    =    59.381 cal/(mol*K)
#    =========== =========== =========== =========== ===========
#    Temperature Heat cap.   Enthalpy    Entropy     Free energy
#    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
#    =========== =========== =========== =========== ===========
#            300      10.881     -92.337      59.454    -110.173
#            400      12.344     -91.173      62.793    -116.290
#            500      13.439     -89.880      65.671    -122.716
#            600      14.289     -88.493      68.199    -129.412
#            800      15.617     -85.495      72.502    -143.497
#           1000      16.556     -82.272      76.094    -158.366
#           1500      17.853     -73.624      83.090    -198.258
#           2000      18.513     -64.521      88.322    -241.166
#           2400      18.928     -57.031      91.735    -277.196
#    =========== =========== =========== =========== ===========
thermo(
    label = 'p_hono',
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.05583, -0.00550874, 6.37335e-05, -1.20972e-07, 7.43935e-11, -47799.2, 6.50747],
                Tmin = (10, 'K'),
                Tmax = (527.102, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.33377, 0.00953017, -6.26718e-06, 1.96987e-09, -2.35522e-13, -47855.9, 8.26892],
                Tmin = (527.102, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (
            -397.431,
            'kJ/mol',
        ),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (83.1447, 'J/(mol*K)'),
    ),
)

# Thermodynamics for p_nitric_oxide:
#   Enthalpy of formation (298 K)   =   -59.725 kcal/mol
#   Entropy of formation (298 K)    =    56.096 cal/(mol*K)
#    =========== =========== =========== =========== ===========
#    Temperature Heat cap.   Enthalpy    Entropy     Free energy
#    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
#    =========== =========== =========== =========== ===========
#            300       9.693     -59.706      56.161     -76.554
#            400      10.630     -58.690      59.077     -82.320
#            500      11.548     -57.580      61.548     -88.354
#            600      12.395     -56.382      63.730     -94.620
#            800      13.831     -53.754      67.500    -107.755
#           1000      14.971     -50.870      70.714    -121.584
#           1500      16.867     -42.863      77.181    -158.635
#           2000      17.909     -34.144      82.190    -198.525
#           2400      18.427     -26.871      85.504    -232.081
#    =========== =========== =========== =========== ===========
thermo(
    label = 'p_nitric_oxide',
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.00045, -0.000131602, 1.55202e-05, -2.04262e-08, 8.80025e-12, -31341.8, 4.95051],
                Tmin = (10, 'K'),
                Tmax = (599.177, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.85564, 0.0075109, -3.61216e-06, 8.60912e-10, -8.15093e-14, -31204.6, 9.88721],
                Tmin = (599.177, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (
            -260.592,
            'kJ/mol',
        ),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (83.1447, 'J/(mol*K)'),
    ),
)

#   ======= =========== =========== =========== ===============
#   Temp.   k (TST)     Tunneling   k (TST+T)   Units
#   ======= =========== =========== =========== ===============
#     400 K   1.104e+07     1.11121   1.226e+07 cm^3/(mol*s)
#     500 K   5.584e+07     1.07161   5.983e+07 cm^3/(mol*s)
#     700 K   4.456e+08     1.03782   4.624e+08 cm^3/(mol*s)
#     900 K   1.715e+09     1.02388   1.756e+09 cm^3/(mol*s)
#    1100 K   4.606e+09      1.0167   4.683e+09 cm^3/(mol*s)
#    1200 K   6.936e+09     1.01434   7.036e+09 cm^3/(mol*s)
#   ======= =========== =========== =========== ===============


#   ======= ============ =========== ============ ============= =========
#   Temp.    Kc (eq)        Units     k_rev (TST) k_rev (TST+T)   Units
#   ======= ============ =========== ============ ============= =========
#     400 K   3.613e+01              3.055e+05     3.395e+05      cm^3/(mol*s)
#     500 K   2.220e+01              2.515e+06     2.695e+06      cm^3/(mol*s)
#     700 K   1.324e+01              3.366e+07     3.493e+07      cm^3/(mol*s)
#     900 K   1.017e+01              1.686e+08     1.726e+08      cm^3/(mol*s)
#    1100 K   8.689e+00              5.301e+08     5.390e+08      cm^3/(mol*s)
#    1200 K   8.210e+00              8.448e+08     8.569e+08      cm^3/(mol*s)
#   ======= ============ =========== ============ ============= =========


# k_rev (TST) = Arrhenius(A=(68.8741,'cm^3/(mol*s)'), n=2.65367, Ea=(24.9311,'kJ/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1200,'K'), comment="""Fitted to 6 data points; dA = *|/ 1.69184, dn = +|- 0.069448, dEa = +|- 0.382994 kJ/mol""") 
# k_rev (TST+T) = Arrhenius(A=(39.4275,'cm^3/(mol*s)'), n=2.72276, Ea=(24.1041,'kJ/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1200,'K'), comment="""Fitted to 6 data points; dA = *|/ 1.5945, dn = +|- 0.0616218, dEa = +|- 0.339834 kJ/mol""") 

# kinetics fitted using the modified three-parameter Arrhenius equation k = A * (T/T0)^n * exp(-Ea/RT) 
kinetics(
    label = 'r_no2 + r_hydroxylamine <=> p_hono + p_nitric_oxide',
    kinetics = Arrhenius(
        A = (10.0495, 'cm^3/(mol*s)'),
        n = 3.08086,
        Ea = (14.7702, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (400, 'K'),
        Tmax = (1200, 'K'),
        comment = 'Fitted to 6 data points; dA = *|/ 1.33796, dn = +|- 0.0384536, dEa = +|- 0.212065 kJ/mol',
    ),
)

