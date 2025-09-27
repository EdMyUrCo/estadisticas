import matplotlib.pyplot as plt
import pandas as pd

# Leer el archivo con separador coma
df = pd.read_csv("indian_food.csv", sep=",")

# Normalizar nombres de columnas
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Mostrar columnas disponibles
print("Columnas disponibles:", df.columns)

# Verificar si existen las columnas necesarias
if "name" in df.columns and "state" in df.columns:
    # Contar cantidad de platillos por estado
    platos_por_estado = df.groupby("state")["name"].count().sort_values(ascending=False)

    # Gráfica de barras
    plt.figure(figsize=(14, 7))
    platos_por_estado.plot(kind="bar", color="green", alpha=0.7)
    plt.xlabel("Estado")
    plt.ylabel("Número de platillos")
    plt.title("Cantidad de platillos por estado en India")
    plt.xticks(rotation=75)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.show()
else:
    print("⚠️ No se encontraron las columnas 'name' y 'state'.")
