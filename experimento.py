# Este código ilustra el enfriamiento adiabático del universo utilizando un modelo simplificado.
# Las simplificaciones incluyen ignorar la energía oscura y la radiación.

import numpy as np
import matplotlib.pyplot as plt

# Constante de Hubble (H0) en unidades de (m/s)/Mpc, convertido a (m/s)/m.
# Este valor es una estimación según los datos del Planck 2018.
H0 = 67.66e3 / 3.086e22

# Temperatura actual del Fondo Cósmico de Microondas (CMB) en Kelvin.
# Este es un valor experimental bien medido.
T0_CMB = 2.7255

# Constante gravitacional en unidades de m^3/(kg s^2).
G = 6.67430e-11

# Densidad actual de la materia (rho_m0) en unidades de kg/m^3.
# Se calcula utilizando la constante de Hubble y la densidad de materia del universo (Omega_m = 0.315).
rho_m0 = 2.775e11 * H0**2 * 0.315

# Creamos un array de tiempo desde el Big Bang hasta la edad actual del universo en segundos.
# Usamos np.linspace para crear un array de 1000 puntos entre 1 segundo y 13.8 mil millones de años convertido a segundos.
t = np.linspace(1, 13.8e9 * 3.154e7, 1000)

# Calculamos el factor de escala (a_t) usando una forma simplificada de la ecuación de Friedmann.
# Esta forma solo es válida para un universo dominado por materia.
a_t = (8 * np.pi * G * rho_m0 / 3)**(1/3) * t**(2/3)

# Calculamos la temperatura (T_t) en función del tiempo usando la ley de enfriamiento adiabático.
# T(t) = T0 / a(t), donde T0 es la temperatura actual del CMB.
T_t = T0_CMB / a_t

# Graficamos la temperatura en función del tiempo.
plt.figure(figsize=(10, 6))
# Convertimos el tiempo a años para el eje x.
plt.plot(t / 3.154e7, T_t, label='Temperatura (K)')
plt.yscale('log')  # Usamos escala logarítmica para el eje y.
plt.xlabel('Tiempo desde el Big Bang (años)')
plt.ylabel('Temperatura (K)')
plt.title('Enfriamiento Adiabático del Universo')
plt.legend()
plt.grid(True)
plt.show()
