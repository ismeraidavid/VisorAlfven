import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# Constantes. El usuario puede elegir el valor que quiera mediante el slider
V = st.sidebar.slider('V', min_value=0.0, max_value=10.0, value=1.0, step=0.1)
omega_d = st.sidebar.slider('omega_d', min_value=0.0, max_value=100.0, value=1.0, step=0.1)
P = st.sidebar.slider('P', min_value=0.0, max_value=10.0, value=1.0, step=0.1)
Q = st.sidebar.slider('Q', min_value=0.0, max_value=10.0, value=0.1, step=0.01)
x0 = st.sidebar.slider('x0', min_value=-5.0, max_value=5.0, value=0.0, step=0.1)
t = st.sidebar.slider('t', min_value=0.0, max_value=10.0, value=1.0, step=1.0)

# Creación del espacio (x,z)
x_rango = np.linspace(-10, 10, 400)
z_rango = np.linspace(0, 10, 200)
x, z = np.meshgrid(x_rango, z_rango)

# Velocidad de Alfvén
v_A = P + Q * (x - x0)**2

# Número de onda
k_z = omega_d / v_A

# Onda
v1 = V * np.cos(k_z * z - omega_d * t)

##############################
#                            #
#        WEB APP             #
#                            #
#                            #
##############################

st.title('4.3: Phase-mixing theory of Alfven wave propagation')

# Enunciado del ejercicio
st.markdown(
    """
    The phase-mixing theory of Alfven wave propagation is not difficult to grasp. Yet, an illustration using a computer program can help a lot in understanding the situation. Consider, therefore, a wave pattern given by the real part of the expression:

    $$\\vec{v_1} = v_1 \\cdot \\vec{e_y}$$ with $$v_1 = V \\cdot \\cos[k_z(x) \\cdot z - \\omega_d \\cdot t]$$

    V and $$\\omega_d$$ are two constants, and $$k_z(x) = \\frac{\\omega_d}{v_A(x)}$$. As already known, the Alfven speed in a plasma is given by $$v_A =\\frac{B}{(\\mu_0 \\cdot \\rho)^{1/2}}$$

    Set V = 1, $$\\omega_d = 1$$, $$v_A(x) = P + Q(x-x_0)^{2}$$ and draw an (x, z) map of $$v_1$$ (e.g., with Python’s contourf or pcolormesh). For the constants P and Q, choose values that let you understand the major ideas behind the phase-mixing theory, and, in particular, the concept of effective wavenumber along x presented in the course.
    """
)

st.title('Visor de patrones de onda Alfvén')

# Plot v_A(x)
fig_vA, ax_vA = plt.subplots(figsize=(10, 3))
ax_vA.plot(x_rango, v_A[0, :], label='$v_A(x)$')
ax_vA.set_title('Distribution of $v_A(x)$')
ax_vA.set_xlabel('x')
ax_vA.set_ylabel('$v_A$')
ax_vA.legend()

# Plot principal
fig, ax = plt.subplots(figsize=(10, 6))
contour = ax.contourf(x, z, v1, cmap='viridis', levels=100)
plt.colorbar(contour, ax=ax, label='$v_1$')
ax.set_title('$v_1 = V \cdot \cos[k_z(x) \cdot z - \omega_d \cdot t]$')
ax.set_xlabel('x')
ax.set_ylabel('z')
ax.set_aspect('equal')  # Ejes proporcionales

st.pyplot(fig_vA)
st.pyplot(fig)

