# Coordinates for CH3 in Input Orientation (angstroms):
#   C    0.0000    0.0000   -0.0000
#   H    0.0000   -0.0015   -1.0821
#   H    0.0000    0.9379    0.5424
#   H    0.0000   -0.9363    0.5397
conformer(
    label = 'CH3',
    E0 = (129.723, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(15.0235, 'amu')),
        NonlinearRotor(
            inertia = ([3.54019, 1.77507, 1.76512], 'amu*angstrom^2'),
            symmetry = 6,
        ),
        HarmonicOscillator(
            frequencies = ([445.514, 1365.37, 1365.43, 3008.15, 3182.8, 3182.83], 'cm^-1'),
        ),
    ],
    spin_multiplicity = 2,
    optical_isomers = 1,
)

# Coordinates for C2H4 in Input Orientation (angstroms):
#   C    0.6651   -0.0000    0.0003
#   C   -0.6651    0.0000   -0.0004
#   H   -1.2380   -0.9233   -0.0004
#   H   -1.2380    0.9233   -0.0004
#   H    1.2380    0.9252    0.0008
#   H    1.2380   -0.9252    0.0008
conformer(
    label = 'C2H4',
    E0 = (54.1827, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(28.0313, 'amu')),
        NonlinearRotor(
            inertia = ([20.2388, 16.7949, 3.44386], 'amu*angstrom^2'),
            symmetry = 4,
        ),
        HarmonicOscillator(
            frequencies = ([798.875, 923.675, 938.689, 1027.59, 1192.91, 1334.23, 1425.22, 1648.24, 3022.2, 3037.34, 3094.97, 3119.88], 'cm^-1'),
        ),
    ],
    spin_multiplicity = 1,
    optical_isomers = 1,
)

# Coordinates for C3H7 in Input Orientation (angstroms):
#   C   -0.4329   -0.0188    0.3501
#   C    0.7754    0.9262    0.4058
#   H    0.6881    1.6354    1.2350
#   H    1.7067    0.3656    0.5353
#   H    0.8623    1.5047   -0.5207
#   C   -0.3857   -0.9842   -0.7855
#   H    0.1053   -0.7190   -1.7171
#   H   -0.9716   -1.8973   -0.7686
#   H   -1.3530    0.5896    0.2897
#   H   -0.5239   -0.5644    1.2982
conformer(
    label = 'C3H7',
    E0 = (85.0019, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(43.0548, 'amu')),
        NonlinearRotor(
            inertia = ([65.2606, 56.6603, 15.3783], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([115.01, 241.643, 354.299, 450.108, 727.531, 851.536, 889.873, 1013.89, 1046.35, 1133.29, 1224.61, 1314.95, 1367.7, 1420.78, 1424.4, 1453.19, 1460.79, 2822.11, 2911.68, 2923.48, 2989.61, 2996.47, 3029.41, 3128.26], 'cm^-1'),
        ),
    ],
    spin_multiplicity = 2,
    optical_isomers = 2,
)

# Coordinates for TS in Input Orientation (angstroms):
#   C    0.3448    1.6937   -0.0000
#   H    0.9089    1.6395    0.9235
#   H   -0.5483    2.3099   -0.0000
#   H    0.9089    1.6395   -0.9235
#   C   -0.6647   -0.4378   -0.0000
#   H   -1.1637   -0.1497    0.9198
#   H   -1.1637   -0.1497   -0.9198
#   C    0.2890   -1.4008   -0.0003
#   H    0.7142   -1.7826    0.9255
#   H    0.7128   -1.7814   -0.9226
conformer(
    label = 'TS',
    E0 = (211.003, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(43.0548, 'amu')),
        NonlinearRotor(
            inertia = ([90.9664, 83.0695, 18.1879], 'amu*angstrom^2'),
            symmetry = 2,
        ),
        HarmonicOscillator(
            frequencies = ([87.3757, 209.424, 334.875, 462.021, 479.784, 754.667, 791.058, 835.554, 906.688, 983.949, 1193.03, 1267.76, 1378.09, 1383.52, 1420.73, 1545.05, 2992.01, 3028.73, 3038.24, 3102.91, 3127.46, 3146.61, 3157.14], 'cm^-1'),
        ),
    ],
    spin_multiplicity = 2,
    optical_isomers = 1,
    frequency = (
        -364.022,
        'cm^-1',
    ),
)

# Thermodynamics for CH3:
#   Enthalpy of formation (298 K)   =    33.552 kcal/mol
#   Entropy of formation (298 K)    =    46.719 cal/(mol*K)
#    =========== =========== =========== =========== ===========
#    Temperature Heat cap.   Enthalpy    Entropy     Free energy
#    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
#    =========== =========== =========== =========== ===========
#            300       9.524      33.571      46.782      19.536
#            400      10.270      34.560      49.624      14.711
#            500      11.009      35.625      51.996       9.627
#            600      11.715      36.761      54.066       4.322
#            800      13.011      39.236      57.617      -6.857
#           1000      14.147      41.955      60.646     -18.691
#           1500      16.305      49.608      66.822     -50.625
#           2000      17.594      58.114      71.707     -85.300
#           2400      18.170      65.277      74.971    -114.652
#    =========== =========== =========== =========== ===========
thermo(
    label = 'CH3',
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.98357, 0.000912259, 9.10026e-06, -1.21426e-08, 5.48822e-12, 15597.4, 0.235334],
                Tmin = (10, 'K'),
                Tmax = (550.254, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.48507, 0.00453619, -7.79077e-07, -1.72631e-10, 4.96015e-14, 15652.3, 2.34249],
                Tmin = (550.254, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (129.677, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (83.1447, 'J/(mol*K)'),
    ),
)

# Thermodynamics for C2H4:
#   Enthalpy of formation (298 K)   =    15.472 kcal/mol
#   Entropy of formation (298 K)    =    52.411 cal/(mol*K)
#    =========== =========== =========== =========== ===========
#    Temperature Heat cap.   Enthalpy    Entropy     Free energy
#    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
#    =========== =========== =========== =========== ===========
#            300      10.518      15.493      52.482      -0.252
#            400      12.706      16.652      55.803      -5.669
#            500      14.908      18.034      58.877     -11.404
#            600      16.910      19.627      61.776     -17.438
#            800      20.106      23.345      67.102     -30.336
#           1000      22.521      27.619      71.860     -44.241
#           1500      26.291      39.931      81.792     -82.758
#           2000      28.236      53.610      89.650    -125.690
#           2400      29.220      65.112      94.890    -162.623
#    =========== =========== =========== =========== ===========
thermo(
    label = 'C2H4',
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.10239, -0.00710856, 5.47104e-05, -6.75635e-08, 2.75482e-11, 6516.35, 3.23344],
                Tmin = (10, 'K'),
                Tmax = (733.684, 'K'),
            ),
            NASAPolynomial(
                coeffs = [0.557358, 0.0183765, -9.98252e-06, 2.65955e-09, -2.77995e-13, 6870.81, 18.1089],
                Tmin = (733.684, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (54.1998, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (133.032, 'J/(mol*K)'),
    ),
)

# Thermodynamics for C3H7:
#   Enthalpy of formation (298 K)   =    24.060 kcal/mol
#   Entropy of formation (298 K)    =    70.298 cal/(mol*K)
#    =========== =========== =========== =========== ===========
#    Temperature Heat cap.   Enthalpy    Entropy     Free energy
#    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
#    =========== =========== =========== =========== ===========
#            300      18.437      24.097      70.421       2.971
#            400      22.546      26.147      76.290      -4.369
#            500      26.437      28.599      81.745     -12.273
#            600      29.949      31.422      86.882     -20.707
#            800      35.609      38.008      96.316     -39.045
#           1000      39.808      45.568     104.734     -59.166
#           1500      46.360      67.301     122.268    -116.101
#           2000      49.703      91.401     136.112    -180.822
#           2400      51.359     111.633     145.329    -237.156
#    =========== =========== =========== =========== ===========
thermo(
    label = 'C3H7',
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.8784, 0.0119939, 3.21407e-05, -4.57876e-08, 1.78678e-11, 10217.7, 8.64694],
                Tmin = (10, 'K'),
                Tmax = (836.769, 'K'),
            ),
            NASAPolynomial(
                coeffs = [1.38176, 0.0316855, -1.70638e-05, 4.49285e-09, -4.64283e-13, 10364, 18.6242],
                Tmin = (836.769, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (84.9552, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (232.805, 'J/(mol*K)'),
    ),
)

#   ======= =========== =========== =========== ===============
#   Temp.   k (TST)     Tunneling   k (TST+T)   Units
#   ======= =========== =========== =========== ===============
#     300 K   8.055e+06     1.14119   9.192e+06 cm^3/(mol*s)
#     400 K   1.372e+08     1.07729   1.478e+08 cm^3/(mol*s)
#     500 K   8.445e+08     1.04913   8.860e+08 cm^3/(mol*s)
#     600 K   3.093e+09     1.03414   3.199e+09 cm^3/(mol*s)
#     700 K   8.346e+09     1.02519   8.556e+09 cm^3/(mol*s)
#     800 K   1.848e+10      1.0194   1.884e+10 cm^3/(mol*s)
#     900 K   3.571e+10     1.01544   3.626e+10 cm^3/(mol*s)
#    1000 K   6.247e+10      1.0126   6.326e+10 cm^3/(mol*s)
#   ======= =========== =========== =========== ===============


#   ======= ============ =========== ============ ============= =========
#   Temp.    Kc (eq)        Units     k_rev (TST) k_rev (TST+T)   Units
#   ======= ============ =========== ============ ============= =========
#     300 K   1.909e+16   cm^3/mol    4.219e-10     4.814e-10      s^-1
#     400 K   7.063e+11   cm^3/mol    1.942e-04     2.092e-04      s^-1
#     500 K   1.608e+09   cm^3/mol    5.251e-01     5.509e-01      s^-1
#     600 K   2.902e+07   cm^3/mol    1.066e+02     1.102e+02      s^-1
#     700 K   1.716e+06   cm^3/mol    4.865e+03     4.988e+03      s^-1
#     800 K   2.131e+05   cm^3/mol    8.673e+04     8.842e+04      s^-1
#     900 K   4.342e+04   cm^3/mol    8.224e+05     8.351e+05      s^-1
#    1000 K   1.249e+04   cm^3/mol    5.000e+06     5.063e+06      s^-1
#   ======= ============ =========== ============ ============= =========


# k_rev (TST) = Arrhenius(A=(7.41045e+09,'s^-1'), n=1.15603, Ea=(126.996,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1000,'K'), comment="""Fitted to 8 data points; dA = *|/ 1.5631, dn = +|- 0.0609742, dEa = +|- 0.264202 kJ/mol""") 
# k_rev (TST+T) = Arrhenius(A=(3.7165e+09,'s^-1'), n=1.24412, Ea=(126.201,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1000,'K'), comment="""Fitted to 8 data points; dA = *|/ 1.65799, dn = +|- 0.0690195, dEa = +|- 0.299063 kJ/mol""") 

# kinetics fitted using the modified three-parameter Arrhenius equation k = A * (T/T0)^n * exp(-Ea/RT) 
kinetics(
    label = 'CH3 + C2H4 <=> C3H7',
    kinetics = Arrhenius(
        A = (4682.64, 'cm^3/(mol*s)'),
        n = 2.72052,
        Ea = (19.7827, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1000, 'K'),
        comment = 'Fitted to 8 data points; dA = *|/ 1.24741, dn = +|- 0.0301781, dEa = +|- 0.130762 kJ/mol',
    ),
)

