import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Datos de ejemplo: géneros de películas y títulos
data = {
    'Título': ['Pelicula1', 'Pelicula2', 'Pelicula3', 'Pelicula4', 'Pelicula5', 
               'Pelicula6', 'Pelicula7', 'Pelicula8', 'Pelicula9', 'Pelicula10'],
    'Acción': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    'Comedia': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'Drama': [1, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    'Ciencia Ficción': [0, 1, 0, 0, 1, 1, 0, 0, 1, 1]
}

# Convertir a DataFrame
df = pd.DataFrame(data)

# Separar características (X) y etiquetas (y)
X = df[['Acción', 'Comedia', 'Drama', 'Ciencia Ficción']]
y = df['Título']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de árbol de decisión
model = DecisionTreeClassifier()

# Entrenar el modelo
model.fit(X_train, y_train)

# Hacer predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy * 100:.2f}%')

# Definir una función para el Sistema Experto de Recomendación
def sistema_experto_recomendacion():
    print("Por favor, ingrese sus preferencias de géneros de películas (1 para Sí, 0 para No):")
    accion = int(input("¿Le gusta la acción? (1/0): "))
    comedia = int(input("¿Le gusta la comedia? (1/0): "))
    drama = int(input("¿Le gusta el drama? (1/0): "))
    ciencia_ficcion = int(input("¿Le gusta la ciencia ficción? (1/0): "))
    
    # Convertir preferencias a DataFrame
    preferencias = {'Acción': accion, 'Comedia': comedia, 'Drama': drama, 'Ciencia Ficción': ciencia_ficcion}
    preferencias_df = pd.DataFrame([preferencias])
    
    # Hacer la predicción de probabilidades
    probabilidades = model.predict_proba(preferencias_df)[0]
    
    # Obtener el índice de la película con mayor probabilidad
    indice_recomendado = max(range(len(probabilidades)), key=lambda i: probabilidades[i])
    
    # Obtener el título de la película recomendada
    pelicula_recomendada = df.loc[indice_recomendado, 'Título']
    
    # Explicación básica del razonamiento
    explicacion = "Basado en sus preferencias de géneros de películas, se recomienda ver: "
    
    return explicacion + pelicula_recomendada

# Ejemplo de uso del Sistema Experto de Recomendación
recomendacion = sistema_experto_recomendacion()
print(recomendacion)
