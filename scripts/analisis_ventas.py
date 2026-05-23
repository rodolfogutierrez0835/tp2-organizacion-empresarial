import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo de ventas
df = pd.read_csv("../datos/ventas.csv")

# Calcular el total por venta
df["total"] = df["cantidad"] * df["precio"]

# Ventas totales
ventas_totales = df["total"].sum()

# Producto más vendido
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()

# Ventas por mes
df["fecha"] = pd.to_datetime(df["fecha"])
df["mes"] = df["fecha"].dt.to_period("M")
ventas_por_mes = df.groupby("mes")["total"].sum()

# Mostrar resultados
print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)
print("Ventas por mes:")
print(ventas_por_mes)

# Crear gráfico
ventas_por_mes.plot(kind="bar", title="Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.tight_layout()
plt.savefig("../resultados/grafico_ventas.png")
