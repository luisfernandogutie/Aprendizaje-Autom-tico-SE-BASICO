# Sistema Experto de Recomendación de Películas

Este proyecto implementa un sistema experto de recomendación de películas utilizando técnicas de aprendizaje automático. El sistema se basa en un modelo de árbol de decisión para predecir y recomendar películas según las preferencias de género del usuario.

## Librerías Utilizadas

- `pandas`: Para la manipulación y análisis de datos.
- `scikit-learn`: Para la implementación del modelo de aprendizaje automático (árbol de decisión).

## Arquitectura del Sistema

El sistema está compuesto por los siguientes componentes:

1. **Datos de Entrada (Interfaz de Usuario):**
   - El usuario proporciona sus preferencias de género de películas (por ejemplo, acción, comedia, drama, ciencia ficción).

2. **Base de Conocimiento:**
   - Un DataFrame que contiene información sobre películas y sus géneros.

3. **Motor de Inferencia:**
   - Un modelo de árbol de decisión entrenado con datos históricos de películas para predecir la recomendación basada en las preferencias del usuario.

4. **Datos de Salida (Respuesta del Sistema):**
   - Una recomendación específica de una película basada en las preferencias del usuario.

## Concepto de Uso

El sistema aprende automáticamente a partir de datos históricos para hacer predicciones futuras. El modelo de árbol de decisión se entrena con datos de películas y sus géneros, y luego se utiliza para hacer recomendaciones basadas en las preferencias ingresadas por el usuario.

## Ejemplo Básico

### Datos de Ejemplo

```python
data = {
    'Título': ['The Matrix', 'Inception', 'La La Land', 'Avengers', 'The Shawshank Redemption', 
               'Pulp Fiction', 'Interstellar', 'Titanic', 'Joker', 'The Godfather'],
    'Acción': [1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    'Comedia': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    'Drama': [1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    'Ciencia Ficción': [1, 1, 0, 0, 0, 0, 1, 0, 0, 0]
}
