import pandas as pd
from imblearn.over_sampling import SMOTE

# Leer el archivo de Excel
df = pd.read_excel('CustomerChurn0.xlsx')

# Especificar la columna objetivo
target_column = 'Complains'

# Separar características y etiquetas
X = df.drop(columns=[target_column])
y = df[target_column]

# Aplicar SMOTE solo a la clase minoritaria (1)
smote = SMOTE(sampling_strategy=0.6)  # Generar un 50% de datos sintéticos
X_resampled, y_resampled = smote.fit_resample(X, y)

# Unir características y etiquetas sintéticas en un nuevo DataFrame
synthetic_data = pd.DataFrame(X_resampled, columns=X.columns)
synthetic_data[target_column] = y_resampled

# Guardar los nuevos datos en un archivo Excel
synthetic_data.to_excel('CustomerChurn3.xlsx', index=False)

# Imprimir la cantidad de muestras por clase en los nuevos datos
print(synthetic_data[target_column].value_counts())

#################################################################################3
# import pandas as pd
# from imblearn.over_sampling import SMOTE
# from sklearn.model_selection import train_test_split

# # Leer los datos desde el archivo Excel
# df = pd.read_excel('CustomerChurn0.xlsx')

# # Especificar la columna que contiene las características y la columna objetivo
# X = df.drop(columns=['Complains'])  # Features
# y = df['Complains']  # Target variable

# # Dividir los datos en conjuntos de entrenamiento y prueba
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Aplicar SMOTE al conjunto de entrenamiento
# sm = SMOTE(sampling_strategy=0.5, random_state=42)
# X_train_res, y_train_res = sm.fit_resample(X_train, y_train)

# # Convertir los datos sintéticos en un DataFrame
# synthetic_data = pd.DataFrame(X_train_res, columns=X.columns)
# synthetic_data['Complains'] = y_train_res

# # Escribir los nuevos datos en un archivo Excel
# synthetic_data.to_excel('nuevos_datos.xlsx', index=False)

# # Verificar el balance de clases en los nuevos datos
# print("Clases en los nuevos datos:")
# print(synthetic_data['Complains'].value_counts())
########################################################
