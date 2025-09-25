import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv("services_data_webstore_semicolon.csv",sep=';')

plt.figure(figsize=(10, 6))
categoria_ventas = df.groupby('Service')['Total Price'].sum()
categoria_ventas.plot(kind='bar')
plt.xlabel('servicios')
plt.ylabel('iventas')
plt.title('Total ventas por Producto')
plt.show()