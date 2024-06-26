# data.py

import pandas as pd
# Base de conocimientos
# Datos de ejemplo: géneros de películas y títulos
data = {
    'Título': ['The Matrix', 'Inception', 'La La Land', 'Avengers', 'The Shawshank Redemption',
           'Pulp Fiction', 'Interstellar', 'Titanic', 'Joker', 'The Godfather'],
    'Acción': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    'Comedia': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'Drama': [1, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    'Ciencia Ficción': [0, 1, 0, 0, 1, 1, 0, 0, 1, 1]
}

# Convertir los datos a DataFrame
df = pd.DataFrame(data)
