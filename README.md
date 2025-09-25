# 📊 Análisis de Datos con Python, Pandas y Matplotlib

Este repositorio contiene diferentes scripts de análisis de datos realizados en **Python** utilizando las librerías **Pandas** y **Matplotlib**.  
Cada análisis se centra en un conjunto de datos distinto y presenta resultados mediante gráficos e interpretaciones descriptivas.

---

## 🛒 1. Informe de Ventas por Producto (Webstore)

### Descripción
Este análisis muestra las **ventas totales por servicio/producto** registradas en una tienda web.  
Se utilizó un dataset en formato CSV con separador `;`.

### Script
```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("services_data_webstore_semicolon.csv", sep=';')

plt.figure(figsize=(10, 6))
categoria_ventas = df.groupby('Service')['Total Price'].sum()
categoria_ventas.plot(kind='bar')
plt.xlabel('servicios')
plt.ylabel('ventas')
plt.title('Total ventas por Producto')
plt.show()

Resultados

Se obtiene un gráfico de barras con las ventas totales por servicio.

Se observa que algunos servicios generan más ingresos que otros.

El servicio con mayores ventas se identifica como el principal generador de ingresos.

🏨 2. Informe sobre Plazo de Entrega en Reservas Hoteleras
Descripción

Este análisis estudia el plazo de entrega (lead_time) en un dataset de reservas hoteleras.
El plazo de entrega corresponde al número de días entre la fecha de reserva y la llegada al hotel.

Script

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("hotel_bookings.csv", sep=',')

plt.figure(figsize=(10, 6))
plt.hist(df['lead_time'], bins=50, color='skyblue', edgecolor='black')
plt.xlabel("Plazo de entrega (días)")
plt.ylabel("Cantidad de reservas")
plt.title("Histograma de Plazo de entrega (lead_time)")
plt.show()

Resultados

El dataset contiene 119,390 reservas.

Promedio de lead_time: 104 días

Mínimo: 0 días | Máximo: 737 días

La mayoría de reservas se realizan con poca anticipación, aunque existe un grupo significativo que reserva con meses de antelación.

🌍 3. Informe de Histogramas de Latitud y Longitud (Global Education)
Descripción

Este análisis examina la distribución geográfica de los datos en el conjunto Global Education mediante histogramas de latitud y longitud.

Script

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Global_Education.csv", sep=',', encoding='latin-1')
df.columns = df.columns.str.strip()

# Histograma de Latitud
plt.figure(figsize=(10, 5))
plt.hist(df['Latitude'], bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Latitud')
plt.ylabel('Frecuencia')
plt.title('Histograma de Latitud')
plt.show()

# Histograma de Longitud
plt.figure(figsize=(10, 5))
plt.hist(df['Longitude'], bins=30, color='salmon', edgecolor='black')
plt.xlabel('Longitud')
plt.ylabel('Frecuencia')
plt.title('Histograma de Longitud')
plt.show()

Resultados

Latitud: valores entre 0.0235 y 64.9630 (promedio: 25.08).

Longitud: valores entre 0.8247 y 178.0650 (promedio: 55.17).

Los histogramas muestran una concentración de registros en determinadas regiones, reflejando las áreas geográficas con más datos educativos.

⚙️ Requisitos

Para ejecutar los scripts necesitas:

Python 3.x

Librerías:

pip install pandas matplotlib

📌 Conclusión General

Estos tres análisis demuestran cómo Python puede ser utilizado para procesar, visualizar y extraer conclusiones a partir de distintos conjuntos de datos.
Las técnicas empleadas permiten entender mejor los patrones en ventas, reservas hoteleras y datos geográficos educativos, lo que puede orientar estrategias de negocio, planificación y estudios académicos.

github:

https://github.com/EdMyUrCo/estadisticas.git
