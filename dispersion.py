import matplotlib.pyplot as plt
import pandas as pd

# Leer archivo
df = pd.read_csv("indian_food.csv", sep=",")

# Normalizar nombres de columnas
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Mostrar columnas disponibles
print("Columnas disponibles:", df.columns)

# Gráfico de dispersión: prep_time vs cook_time
if "prep_time" in df.columns and "cook_time" in df.columns:
    plt.figure(figsize=(10, 6))
    plt.scatter(df["prep_time"], df["cook_time"], color="purple", alpha=0.6, edgecolors="black")
    
    plt.xlabel("Tiempo de preparación (minutos)")
    plt.ylabel("Tiempo de cocción (minutos)")
    plt.title("Relación entre tiempo de preparación y cocción")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()
else:
    print("⚠️ No se encontraron las columnas 'prep_time' y/o 'cook_time'.")
