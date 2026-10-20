# Quantum-Dot-Size-Emission
An interactive Python simulation exploring how the diameter of a CdSe quantum dot affects its predicted optical transition energy and wavelength.

## What this project does

The simulation allows the user to change the diameter of a CdSe quantum dot between 3 and 8 nm.

It then calculates:

- the transition energy,
- the corresponding wavelength,
- and the position of the quantum dot on the complete size–wavelength relationship.

The project uses the Brus equation and the effective-mass approximation.

## Why size matters

When semiconductor particles become only a few nanometers wide, electrons and holes become spatially confined.

As the quantum dot becomes smaller, quantum confinement becomes stronger.

This leads to:

**smaller quantum dot → larger transition energy → shorter wavelength**

## Tech stack

- Python
- Streamlit
- NumPy
- Plotly
- Pandas

## Project structure

```text
quantum-dot-size-emission/
├── physics.py
├── streamlit_app.py
├── requirements.txt
├── README.md
└── article.md
```

## Run the project

Install the dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
streamlit run streamlit_app.py
```

## Limitations

This is a simplified effective-mass model rather than a complete simulation of real CdSe quantum dots.

Real experimental results can also depend on surface states, ligands, defects, crystal structure, particle-size distributions, and other effects.

## Why I built this

This project is part of my exploration of AI-driven inverse design of quantum dots.

The current project solves a simplified forward problem:

**quantum-dot size → optical property**

My broader goal is to explore the inverse problem:

**desired optical property → possible quantum-dot design**
