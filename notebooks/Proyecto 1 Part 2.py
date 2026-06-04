import pandas as pd
df = pd.read_csv("/Users/carlis/retail-sales-analysis/data/retail_sales_dataset.csv")

# Ver las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(df.head(10))

#Exploracion inicial de datos
print("Ultimas filas del DataFrame:")
print(df.tail(5))

print("Informacion del DataFrame:")
print(df.info())

print("Estadisticas descriptivas del DataFrame:")
print(df.describe())

#Inspeccion de los datos
print("Tipos de datos de las Columnas")
print(df.dtypes)

print("Conteo de valores unicos en la columna 'Product Category':")
print(df['Product Category'].value_counts())

print("Valores unicos en la columna 'Gender':")
print(df['Gender'].unique())

#Filtrado de datos
filtro_ventas = df[df['Total Amount'] > 500]
print(filtro_ventas)

filtro_precio = df[df['Price per Unit'] < 50]
print(filtro_precio)

filtro_query = df.query("`Product Category` == 'Clothing' and `Total Amount` > 30")
print(filtro_query)

#Slicing de datos
df_columnas = df[["Product Category", "Total Amount"]]
print(df_columnas)

df_loc = df.loc[5:10, ["Product Category", "Customer ID"]]
print(df_loc)

df_iloc = df.iloc[0:5, 0:3]
print(df_iloc)