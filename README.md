# Enfriamiento Adiabático del Universo

Este código ilustra cómo la temperatura del universo podría haber disminuido desde el Big Bang hasta la actualidad, utilizando un modelo simplificado que considera un universo dominado solo por materia.

## Constantes Utilizadas

1. **Constante de Hubble (H0)**: Representa la tasa de expansión del universo. El valor utilizado es 67.66 km/s/Mpc, que es una estimación según los datos del Planck 2018. Se convierte a unidades de (m/s)/m para el cálculo.

2. **Temperatura actual del Fondo Cósmico de Microondas (T0_CMB)**: Es la temperatura actual del universo, medida a 2.7255 K. Este valor es bien conocido y medido experimentalmente.

3. **Constante Gravitacional (G)**: Usada para calcular el factor de escala del universo en el modelo de Friedmann. El valor es 6.67430 x 10^-11 m^3/kg s^2.

4. **Densidad actual de la materia (rho_m0)**: Calculada utilizando la constante de Hubble y la densidad de materia del universo (Omega_m = 0.315). Se usa para el cálculo del factor de escala en la ecuación de Friedmann.

## Detalles del Cálculo

1. **Tiempo (t)**: Se considera un rango de tiempo desde 1 segundo después del Big Bang hasta la edad actual del universo (13.8 mil millones de años), convertido a segundos.

2. **Factor de Escala (a_t)**: Se calcula utilizando una versión simplificada de la ecuación de Friedmann, que es válida para un universo dominado por materia. La fórmula es:

    a(t) = (8 *pi* G *rho_m0 / 3)^(1/3)* t^(2/3)

3. **Temperatura (T_t)**: La temperatura en función del tiempo se calcula usando la ley de enfriamiento adiabático:

    T(t) = T0 / a(t)

## Ejecución

El código genera un gráfico que muestra cómo la temperatura del universo disminuye con el tiempo en este modelo simplificado.

## Notas

Este modelo es una simplificación y no considera efectos como la energía oscura o la radiación. Se utiliza para fines ilustrativos.
