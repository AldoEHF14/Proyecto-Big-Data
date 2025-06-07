import pandas as pd

# Cargar el archivo Excel
archivo_excel = "CustomerChurn2.xlsx"  # Reemplaza con el nombre de tu archivo
columna_etiquetas = "Complains"  # Reemplaza con el nombre de la columna de etiquetas

df = pd.read_excel(archivo_excel)

# Contar la frecuencia de cada clase en la columna de etiquetas
balanceo = df[columna_etiquetas].value_counts()

# Mostrar el balanceo
print("Balanceo de clases:")
print(balanceo)

# Graficar el balanceo (opcional)
import matplotlib.pyplot as plt

plt.bar(balanceo.index, balanceo.values, color=['blue', 'orange'])
plt.xlabel("Clases")
plt.ylabel("Frecuencia")
plt.title("Balanceo de Clases")
plt.show()
