import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from physics import calculate_transition


st.set_page_config(
    page_title="Quantum Dot Size vs. Emission",
    page_icon="⚛️",
    layout="wide"
)


# Visual helper


def wavelength_to_color(wavelength):
   
    # Rough mapping from visible wavelength to RGB color.
   

    if wavelength < 380:
        return "rgb(120,120,120)"

    if wavelength < 440:
        red = -(wavelength - 440) / 60
        green = 0
        blue = 1

    elif wavelength < 490:
        red = 0
        green = (wavelength - 440) / 50
        blue = 1

    elif wavelength < 510:
        red = 0
        green = 1
        blue = -(wavelength - 510) / 20

    elif wavelength < 580:
        red = (wavelength - 510) / 70
        green = 1
        blue = 0

    elif wavelength < 645:
        red = 1
        green = -(wavelength - 645) / 65
        blue = 0

    elif wavelength <= 750:
        red = 1
        green = 0
        blue = 0

    else:
        return "rgb(120,120,120)"

    red = int(max(0, min(1, red)) * 255)
    green = int(max(0, min(1, green)) * 255)
    blue = int(max(0, min(1, blue)) * 255)

    return f"rgb({red},{green},{blue})"



# Header

st.title("Quantum Dot Size vs. Optical Transition")

st.write(
    """An interactive simulation of how quantum confinement
    changes the optical transition of CdSe quantum dots.
    """
)


# Diameter control


diameter = st.slider(
    "Quantum dot diameter",
    min_value=3.0,
    max_value=8.0,
    value=5.0,
    step=0.1,
    format="%.1f nm"
)


energy, wavelength = calculate_transition(diameter)

color = wavelength_to_color(wavelength)


# Metrics


col1, col2, col3 = st.columns(3)

col1.metric(
    "Diameter",
    f"{diameter:.1f} nm"
)

col2.metric(
    "Transition energy",
    f"{energy:.2f} eV"
)

col3.metric(
    "Wavelength",
    f"{wavelength:.0f} nm"
)


# Quantum dot visualization


st.subheader("Quantum Dot")

dot_size = int(
    110
    + ((diameter - 3) / 5) * 100
)

st.markdown(
    f"""
    <div style="
        height:260px;
        display:flex;
        align-items:center;
        justify-content:center;
    ">
        <div style="
            width:{dot_size}px;
            height:{dot_size}px;
            border-radius:50%;
            background:{color};
            box-shadow:
                0 0 25px {color},
                0 0 55px {color};
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:20px;
            font-weight:600;
            color:white;
        ">
            {diameter:.1f} nm
        </div>
    </div>
    """,
    unsafe_allow_html=True
)



# Size vs wavelength curve


diameters = np.linspace(3, 8, 200)

wavelengths = []

for d in diameters:
    _, wl = calculate_transition(d)
    wavelengths.append(wl)


fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=diameters,
        y=wavelengths,
        mode="lines",
        name="Brus model"
    )
)

fig.add_trace(
    go.Scatter(
        x=[diameter],
        y=[wavelength],
        mode="markers",
        marker=dict(
            size=16,
            color=color,
            line=dict(
                width=2,
                color="white"
            )
        ),
        name="Selected quantum dot"
    )
)

fig.update_layout(
    title="Quantum Dot Diameter vs. Predicted Wavelength",
    xaxis_title="Diameter (nm)",
    yaxis_title="Wavelength (nm)",
    template="plotly_dark",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)



# Explanation


st.subheader("What is happening?")

st.markdown(
    """
    **Smaller quantum dot**

    ↓

    Stronger quantum confinement

    ↓

    Larger transition energy

    ↓

    Shorter wavelength
    """
)


st.latex(
    r"""
    E(R)=
    E_{g,\mathrm{bulk}}
    +
    \frac{\pi^2\hbar^2}{2R^2}
    \left(
    \frac{1}{m_e^*}
    +
    \frac{1}{m_h^*}
    \right)
    -
    \frac{1.8e^2}
    {4\pi\epsilon_0\epsilon_rR}
    """
)



# Experiment measurements


st.subheader("Experiment Data")

if "measurements" not in st.session_state:
    st.session_state.measurements = []


if st.button("Save current measurement"):

    st.session_state.measurements.append(
        {
            "Diameter (nm)": round(diameter, 2),
            "Energy (eV)": round(energy, 3),
            "Wavelength (nm)": round(wavelength, 1)
        }
    )


if st.session_state.measurements:

    dataframe = pd.DataFrame(
        st.session_state.measurements
    )

    st.dataframe(
        dataframe,
        use_container_width=True
    )

    csv = dataframe.to_csv(
        index=False
    )

    st.download_button(
        "Download measurements as CSV",
        csv,
        file_name="quantum_dot_measurements.csv",
        mime="text/csv"
    )

    if st.button("Clear measurements"):
        st.session_state.measurements = []
        st.rerun()


# Limitation

st.subheader("Model limitations")

st.write(
    """
    This simulation uses a simplified effective-mass model.
    Real quantum dots can differ because of surface states,
    ligands, defects, crystal structure, size distributions,
    and other effects.
    """
)