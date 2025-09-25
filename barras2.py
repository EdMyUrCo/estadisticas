import matplotlib.pyplot as plt
import pandas as pd

# Cargar datos con el separador correcto
df = pd.read_csv("hotel_bookings.csv", sep=',')

# Mostrar primeras filas y columnas para confirmar
print("\nPrimeras filas del DataFrame:")
print(df.head())
print("\nColumnas disponibles:")
print(df.columns)

# Histograma del plazo de entrega (lead_time)
plt.figure(figsize=(10, 6))
plt.hist(df['lead_time'], bins=50, color='skyblue', edgecolor='black')
plt.xlabel("Plazo de entrega (días)")
plt.ylabel("Cantidad de reservas")
plt.title("Histograma de Plazo de entrega (lead_time)")
plt.show()
