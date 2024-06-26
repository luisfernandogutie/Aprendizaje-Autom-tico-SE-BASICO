# model.py

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from data import df  # Importar el DataFrame creado en data.py

# Separar características (X) y etiquetas (y)
X = df[['Acción', 'Comedia', 'Drama', 'Ciencia Ficción']]
y = df['Título']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de árbol de decisión
model = DecisionTreeClassifier()

# Entrenar el modelo
model.fit(X_train, y_train)
