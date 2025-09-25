import matplotlib.pyplot as plt
import pandas as pd

# Cargar los datos con el separador correcto
df = pd.read_csv("Global_Education.csv", sep=',', encoding='latin-1')

# Limpiar espacios en los nombres de columnas
df.columns = df.columns.str.strip()

print("Columnas disponibles:", df.columns)

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
