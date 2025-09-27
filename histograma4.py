import matplotlib.pyplot as plt
import pandas as pd

# Leer CSV con separador correcto (coma)
df = pd.read_csv("fashion_products.csv", sep=',')

# Revisar columnas
print(df.columns)

# Histograma de precios
plt.hist(df['Price'], bins=10, edgecolor='black')
plt.xlabel("Precio")
plt.ylabel("Frecuencia")
plt.title("Distribución de precios")
plt.show()
