import pandas as pd

def dividir_archivo_excel(archivo_entrada, porcentaje_primero):
    # Leer el archivo Excel
    df = pd.read_excel(archivo_entrada)
    
    # Obtener el número total de filas
    total_filas = len(df)
    
    # Calcular el número de filas para el primer archivo
    filas_primero = int(total_filas * porcentaje_primero / 100)
    
    # Ajustar la división si el número total de filas es impar
    if total_filas % 2 != 0:
        filas_primero += 1
    
    # Dividir el DataFrame en dos partes
    primera_parte = df.iloc[:filas_primero]
    segunda_parte = df.iloc[filas_primero:]
    
    # Guardar las partes en archivos Excel separados
    primera_parte.to_excel('primeras_filas.xlsx', index=False)
    segunda_parte.to_excel('ultimas_filas.xlsx', index=False)

# Nombre del archivo original
archivo_entrada = 'CustomerChurn2.xlsx'

# Pedir al usuario el porcentaje de filas para el primer archivo
porcentaje_primero = float(input("Porcentaje de filas para el primer archivo (entre 0 y 100): "))

# Llamar a la función para dividir el archivo
dividir_archivo_excel(archivo_entrada, porcentaje_primero)
