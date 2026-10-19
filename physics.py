import numpy as np


# Physical constants
HBAR = 1.054571817e-34
H = 6.62607015e-34
C = 299792458

E_CHARGE = 1.602176634e-19
EPSILON_0 = 8.8541878128e-12
M_0 = 9.1093837139e-31


# Approximate CdSe parameters
E_G_BULK = 1.74
M_E = 0.13 * M_0
M_H = 0.45 * M_0
EPSILON_R = 10.6


def calculate_transition(diameter_nm):
    
    #Calculate the size-dependent transition energy
    #and wavelength of a CdSe quantum dot
    

    if diameter_nm <= 0:
        raise ValueError("Diameter must be positive.")

    radius = (diameter_nm / 2) * 1e-9

    confinement = (np.pi**2 * HBAR**2
        / (2 * radius**2)
        * (1 / M_E + 1 / M_H))

    coulomb = (
        1.8 * E_CHARGE**2
        / (4 * np.pi * EPSILON_0 * EPSILON_R * radius)
    )

    energy_eV = (
        E_G_BULK
        + (confinement - coulomb) / E_CHARGE
    )

    wavelength_nm = (
        H * C
        / (energy_eV * E_CHARGE)
    ) * 1e9

    return energy_eV, wavelength_nm