# Simulating Quantum Confinement: How Quantum Dot Size Changes Light

*Reproducing the size-dependent optical properties of CdSe quantum dots using Python and the Brus equation.*

## 1. Introduction & Motivation

Quantum dots are semiconducting nanocrystals with remarkable optical properties, including the ability to act as single-photon emitters under suitable conditions. Their nanoscale dimensions allow their electronic and optical properties to be influenced by changes in size.

In solar cells, quantum dots could help broaden the range of wavelengths that can be absorbed, potentially improving energy conversion efficiency. In bioengineering, they can also be used as fluorescent markers to detect malignant cancer cells, although their biocompatibility depends on the materials used.

In this project, I aim to explore the theoretical framework underlying the size-dependent optical properties of quantum dots and visualize its predictions through an interactive simulation.

As a first step toward my broader goal of developing an AI system capable of inverse-designing quantum dots, I want to understand the physical principles that such a model would build upon and investigate how accurately simplified theoretical models describe their behavior.

## 2. The Physics Behind Quantum Dots

To understand how quantum dots change their optical properties, we first need to understand a phenomenon called **quantum confinement**.

In a bulk semiconductor, electrons can occupy energy states within the valence and conduction bands. The energy difference between these bands is called the band gap.

However, when the material becomes only a few nanometers in size, the situation changes. Electrons and holes become confined to a much smaller space, which changes their allowed energy levels.

A useful comparison is the quantum-mechanical particle in a box. When the box becomes smaller, the energy levels become more widely separated. Something similar happens in quantum dots.

This means that smaller quantum dots generally have a higher optical transition energy, while larger ones have a lower transition energy.

Since photon energy and wavelength are inversely related, this also changes the wavelength of light associated with the transition.

To describe this relationship mathematically, I used the **Brus equation**:


$$
E(R) = E_{\mathrm{bulk}} + \frac{\pi^2 \hbar^2}{2R^2} \left(\frac{1}{m_e^*} + \frac{1}{m_h^*}\right) - \frac{1.8e^2}{4\pi\varepsilon_0\varepsilon_r R}}
$$

The equation consists of three main parts.

The first term represents the band gap of the bulk semiconductor. For CdSe, I used approximately 1.74 eV.

The second term describes quantum confinement. It depends on the inverse square of the radius, meaning that it increases strongly when the quantum dot becomes smaller.

The third term accounts for the Coulomb attraction between the electron and the hole, which reduces the transition energy.

By combining these three terms, we can calculate an approximate optical transition energy for a quantum dot of a given size.

Finally, the wavelength can be calculated using:

$$
\lambda=\frac{hc}{E}
$$

This gives us the theoretical foundation for the simulation.

## 3. Implementing the Model in Python

After understanding the physical model, I wanted to turn it into an actual simulation.

I decided to use Python because it allows me to implement the equations directly and later connect them to more advanced computational models.

The main calculations are located in `physics.py`.

First, I defined the physical constants, including Planck's constant, the elementary charge and the electron rest mass. I also included approximate material-specific values for CdSe, such as its bulk band gap, effective electron and hole masses, and relative dielectric constant.

The simulation takes one main input: **the diameter of the quantum dot in nanometers**.

Since the Brus equation uses the radius, I first convert the diameter into a radius in meters.

```python
radius = (diameter_nm / 2) * 1e-9
```

The program then calculates the confinement energy and the Coulomb contribution separately.

The confinement term is calculated using:

```python
confinement = (
    np.pi**2 * HBAR**2
    / (2 * radius**2)
    * (1 / M_E + 1 / M_H)
)
```

The Coulomb contribution is calculated using:

```python
coulomb = (
    1.8 * E_CHARGE**2
    / (4 * np.pi * EPSILON_0 * EPSILON_R * radius)
)
```

Both terms are combined with the bulk band gap to determine the transition energy.

One important detail is that the physical constants are expressed in SI units, while the bulk band gap is given in electron volts. Therefore, the energy contributions must be converted into the same units before they can be added.

After calculating the transition energy, I use the photon energy equation to convert it into a wavelength.

```python
wavelength_nm = (
    H * C
    / (energy_eV * E_CHARGE)
) * 1e9
```

The resulting function returns two values: the transition energy in eV and the wavelength in nm.

This gives a simple forward model:

**Quantum dot diameter → transition energy → wavelength**

The model does not involve AI yet. Its purpose is to reproduce a known physical relationship before moving to more complicated approaches.

## 4. Building the Interactive Simulation

Having the calculation alone was not enough for me. I wanted to visualize the results and make it possible to experiment with different quantum-dot sizes.

For this, I built an interactive web application using **Streamlit**.

The application allows the user to change the diameter of a CdSe quantum dot between 3 and 8 nm using a slider.

Whenever the diameter changes, the program automatically recalculates the transition energy and wavelength.

I also used Plotly to create a graph that shows the relationship between quantum-dot diameter and predicted wavelength.

Instead of displaying only one result, the graph shows the full relationship across the selected size range. A marker indicates the currently selected quantum dot.

Another feature is the visual representation of the quantum dot itself. Its displayed size changes with the selected diameter, while its color is approximated from the calculated wavelength.

Of course, this is only a simplified visualization. The displayed colors should not be treated as an exact representation of what a real quantum dot would look like.

Finally, I added the possibility of saving different simulation results in a table and exporting them as a CSV file.

This allows users to compare different sizes and analyze the calculated values outside the application. These saved values are theoretical predictions rather than experimental measurements.

The application was built using Python, Streamlit, NumPy, Plotly and Pandas.

You can find the implementation in my [GitHub repository](https://github.com/klahlou2008/Quantum-Dot-Size-Emission).

## 5. Results and Limitations

After implementing the model, I calculated the optical transition energies and wavelengths for different CdSe quantum-dot diameters.

The results show a clear relationship between size and optical properties.

| Diameter (nm) | Transition Energy (eV) | Wavelength (nm) |
|---|---|---|
| 3 | 3.234 | 383.4 |
| 4 | 2.550 | 486.3 |
| 5 | 2.239 | 553.8 |
| 6 | 2.073 | 598.2 |
| 8 | 1.912 | 648.5 |

As the diameter increases from 3 to 8 nm, the predicted transition energy decreases, while the wavelength increases.

This means that smaller quantum dots correspond to shorter wavelengths, while larger ones correspond to longer wavelengths.

Another interesting aspect is that the relationship is nonlinear. Changing the diameter by 1 nm has a stronger effect at smaller sizes than at larger ones.

This is mainly due to the confinement term in the Brus equation, which depends on the inverse square of the radius.

However, there are important limitations.

First, the Brus equation is based on a simplified effective-mass model. It does not describe every physical process occurring inside a real quantum dot.

Factors such as surface states, defects, ligands, crystal structure and the surrounding environment can influence the optical properties.

Furthermore, the model predicts an approximate transition energy rather than the complete emission spectrum. In real quantum dots, the photoluminescence peak may differ from the transition energy calculated by the model.

Another limitation is that reproducing the mathematical predictions does not automatically mean that the simulation accurately describes experimental results.

For that, the calculated values would have to be compared with measurements from real CdSe quantum dots of known sizes.

Therefore, the simulation demonstrates the theoretical relationship between size and optical transitions, but it is not yet a validated predictor of experimental emission wavelengths.

## 6. Connecting the Project to Inverse Materials Design

My long-term goal at TKS is to build an AI system that can inverse-design quantum dots.

Instead of manually choosing material properties and calculating what the resulting quantum dot would do, I want to explore whether researchers could specify their desired optical properties and receive possible material structures in return.

This project is a first step toward that goal.

The current simulation solves what is called a **forward problem**.

We provide a quantum-dot diameter, and the model predicts the corresponding optical transition.

In inverse design, we want to reverse that process.

For example, a researcher could specify a desired wavelength, and the system would attempt to find a quantum-dot design capable of producing it.

However, real inverse design is more complicated than simply rearranging the Brus equation.

The optical properties of quantum dots depend on much more than their diameter. Their material composition, shape, surface chemistry and internal structure can all play a role.

This also creates a problem called **non-uniqueness**: multiple different structures may produce similar optical properties.

An AI-based inverse-design system would therefore need to identify possible structures and evaluate how well they match the desired properties.

One approach would be to use a forward model to predict the optical properties of candidate structures, while an inverse model proposes possible designs.

Before exploring such systems, I wanted to understand how a simpler forward model works.

By implementing the Brus equation and visualizing its predictions, I could examine the relationship between a structural property and an optical property.

The next step would be to move beyond this one-variable model and explore machine-learning approaches that can work with more complex quantum-dot structures and optical spectra.

Ultimately, I want to investigate how these approaches could make the design of new materials faster and more accessible.

## References

1. Brus, L. E. (1984). *Electron–Electron and Electron–Hole Interactions in Small Semiconductor Crystallites: The Size Dependence of the Lowest Excited Electronic State.* Journal of Chemical Physics, 80, 4403–4409. https://doi.org/10.1063/1.447218

2. Brus, L. E. (1986). *Electronic Wave Functions in Semiconductor Clusters: Experiment and Theory.* Journal of Physical Chemistry, 90, 2555–2560. https://doi.org/10.1021/j100403a003

3. [Quantum Dot Size vs. Emission — GitHub Repository](https://github.com/klahlou2008/Quantum-Dot-Size-Emission)
