import matplotlib.pyplot as plt
import pandas as pd

# Leer el archivo con separador coma
df = pd.read_csv("indian_food.csv", sep=",")

# Normalizar nombres de columnas
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Mostrar columnas disponibles
print("Columnas disponibles:", df.columns)

# Gráfica lineal de cook_time
if "cook_time" in df.columns:
    plt.figure(figsize=(14, 6))
    plt.plot(df.index, df["cook_time"], marker="o", linestyle="-", color="blue", alpha=0.7)
    plt.xlabel("Índice del platillo")
    plt.ylabel("Tiempo de cocción (minutos)")
    plt.title("Gráfica lineal del tiempo de cocción en los platillos")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()
else:
    print("⚠️ No se encontró la columna 'cook_time'.")
