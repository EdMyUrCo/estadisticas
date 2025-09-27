import matplotlib.pyplot as plt
import pandas as pd

# Leer archivo
df = pd.read_csv("indian_food.csv", sep=",")

# Normalizar nombres de columnas
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Mostrar columnas
print("Columnas disponibles:", df.columns)

# Gráfica lineal comparando prep_time y cook_time
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
else:
    print("⚠️ No se encontraron las columnas 'prep_time' y/o 'cook_time'.")
