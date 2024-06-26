# recommendation.py

import pandas as pd

from model import model  # Importar el modelo entrenado desde model.py
from data import df  # Importar el DataFrame creado en data.py
# MOTOR DE INFERENCIA
# Definir una función para el Sistema Experto de Recomendación
def sistema_experto_recomendacion(accion, comedia, drama, ciencia_ficcion):
    # Convertir las preferencias a un DataFrame
    preferencias = {'Acción': accion, 'Comedia': comedia, 'Drama': drama, 'Ciencia Ficción': ciencia_ficcion}
    preferencias_df = pd.DataFrame([preferencias])
    
    # Hacer la predicción de probabilidades
    probabilidades = model.predict_proba(preferencias_df)[0]
    
    # Obtener el índice de la película con la mayor probabilidad
    indice_recomendado = max(range(len(probabilidades)), key=lambda i: probabilidades[i])
    
    # Obtener el título de la película recomendada
    pelicula_recomendada = df.loc[indice_recomendado, 'Título']
    
    # Explicación básica del razonamiento
    explicacion = "Basado en sus preferencias de géneros de películas, se recomienda ver: "
    
    return explicacion + pelicula_recomendada
