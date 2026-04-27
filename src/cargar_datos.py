import numpy as np
import os

def cargar_datos(ruta_archivo):
    # Carga los datos del archivo CSV utilizando NumPy
    datos = np.genfromtxt(ruta_archivo, delimiter=',', skip_header=1)
    return datos

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    ruta_archivo = os.path.join(base_dir, '..', 'data', 'retail_sales_dataset.csv')
    
    datos = cargar_datos(ruta_archivo)
    print(datos)