# 📊 Análisis de Datos con Python, Pandas y Matplotlib

Este repositorio contiene diferentes scripts de análisis de datos realizados en **Python** utilizando las librerías **Pandas** y **Matplotlib**.  
Cada análisis se centra en un conjunto de datos distinto y presenta resultados mediante gráficos e interpretaciones descriptivas.

---

## 🛒 1. Informe de Ventas por Producto (Webstore)

### 📌 Descripción
Este análisis muestra las **ventas totales por servicio/producto** registradas en una tienda web.  
Se utilizó un dataset en formato CSV con separador `;`.

### 💻 Script
```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("services_data_webstore_semicolon.csv", sep=';')

plt.figure(figsize=(10, 6))
categoria_ventas = df.groupby('Service')['Total Price'].sum()
categoria_ventas.plot(kind='bar')
plt.xlabel('Servicios')
plt.ylabel('Ventas')
plt.title('Total ventas por Producto')
plt.show()

📊 Resultados

Se obtiene un gráfico de barras con las ventas totales por servicio.

Algunos servicios generan más ingresos que otros.

El servicio con mayores ventas se identifica como el principal generador de ingresos.

🏨 2. Informe sobre Plazo de Entrega en Reservas Hoteleras
📌 Descripción

Este análisis estudia el plazo de entrega (lead_time) en un dataset de reservas hoteleras.
El plazo de entrega corresponde al número de días entre la fecha de reserva y la llegada al hotel.

💻 Script
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("hotel_bookings.csv", sep=',')

plt.figure(figsize=(10, 6))
plt.hist(df['lead_time'], bins=50, color='skyblue', edgecolor='black')
plt.xlabel("Plazo de entrega (días)")
plt.ylabel("Cantidad de reservas")
plt.title("Histograma de Plazo de entrega (lead_time)")
plt.show()

📊 Resultados

Dataset con 119,390 reservas.

Promedio de lead_time: 104 días.

Valores extremos: mínimo 0 días | máximo 737 días.

La mayoría de reservas se realizan con poca anticipación, aunque existe un grupo que reserva con meses de antelación.

🌍 3. Informe de Histogramas de Latitud y Longitud (Global Education)
📌 Descripción

Este análisis examina la distribución geográfica de los datos en el conjunto Global Education mediante histogramas de latitud y longitud.

💻 Script
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

📊 Resultados

Latitud: valores entre 0.0235 y 64.9630 (promedio: 25.08).

Longitud: valores entre 0.8247 y 178.0650 (promedio: 55.17).

Los histogramas muestran concentración de registros en ciertas regiones, reflejando áreas con más datos educativos.

🍲 4. Análisis de Platillos de Comida India
📌 Scripts
🔹 Relación entre tiempo de preparación y cocción

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("indian_food.csv", sep=",")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

if "prep_time" in df.columns and "cook_time" in df.columns:
    plt.figure(figsize=(10, 6))
    plt.scatter(df["prep_time"], df["cook_time"], color="purple", alpha=0.6, edgecolors="black")
    plt.xlabel("Tiempo de preparación (minutos)")
    plt.ylabel("Tiempo de cocción (minutos)")
    plt.title("Relación entre tiempo de preparación y cocción")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()

🔹 Gráfica lineal de tiempos de cocción
if "cook_time" in df.columns:
    plt.figure(figsize=(14, 6))
    plt.plot(df.index, df["cook_time"], marker="o", linestyle="-", color="blue", alpha=0.7)
    plt.xlabel("Índice del platillo")
    plt.ylabel("Tiempo de cocción (minutos)")
    plt.title("Gráfica lineal del tiempo de cocción en los platillos")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()

🔹 Comparación de tiempos de preparación y cocción
if "prep_time" in df.columns and "cook_time" in df.columns:
    plt.figure(figsize=(14, 6))
    plt.plot(df.index, df["prep_time"], marker="o", linestyle="-", color="green", alpha=0.7, label="Tiempo de preparación")
    plt.plot(df.index, df["cook_time"], marker="s", linestyle="-", color="blue", alpha=0.7, label="Tiempo de cocción")
    plt.xlabel("Índice del platillo")
    plt.ylabel("Tiempo (minutos)")
    plt.title("Comparación lineal de tiempos de preparación y cocción")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()

🔹 Platillos por estado
if "name" in df.columns and "state" in df.columns:
    platos_por_estado = df.groupby("state")["name"].count().sort_values(ascending=False)

    plt.figure(figsize=(14, 7))
    platos_por_estado.plot(kind="bar", color="green", alpha=0.7)
    plt.xlabel("Estado")
    plt.ylabel("Número de platillos")
    plt.title("Cantidad de platillos por estado en India")
    plt.xticks(rotation=75)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.show()

👗 5. Análisis de Productos de Moda (Fashion Products)
📌 Histogramas
🔹 Distribución de Precios
df = pd.read_csv("fashion_products.csv", sep=',')
plt.hist(df['Price'], bins=10, edgecolor='black')
plt.xlabel("Precio")
plt.ylabel("Frecuencia")
plt.title("Distribución de precios")
plt.show()

🔹 Distribución de Tallas
plt.hist(df['Size'], bins=10, edgecolor='black')
plt.xlabel("Tallas")
plt.ylabel("Frecuencia")
plt.title("Distribución de tallas")
plt.show()

⚙️ Requisitos

Para ejecutar los scripts necesitas:

Python 3.x

Librerías instaladas:
pip install pandas matplotlib

📌 Conclusión General

Estos análisis demuestran cómo Python puede ser utilizado para procesar, visualizar y extraer conclusiones a partir de distintos conjuntos de datos.
Las técnicas empleadas permiten entender mejor los patrones en ventas, reservas hoteleras, gastronomía y moda, lo que puede orientar estrategias de negocio, planificación y estudios académicos.

🔗 GitHub

Repositorio completo: estadísticas
github: https://github.com/EdMyUrCo/estadisticas.git