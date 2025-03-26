import numpy as np  
from sklearn.neighbors import KNeighborsClassifier 

# Datos de entrenamiento del Modelo
MatrizX = np.array([[2, 12],[4, 9],[10, 1],[9, 4],[2, 6],[2, 18],[3, 4],[3, 3]])
Clases = np.array([0, 1, 0, 1, 0, 1, 0, 1]) 

# Configurar el clasificador K-NN con k=1
KNN = KNeighborsClassifier(n_neighbors=1, metric='manhattan')
KNN.fit(MatrizX, Clases)

# Clasificar el nuevo caso (2.5, 2.5)
Casos = np.array([[5, 5]])
C_preajustada_1 = KNN.predict(Casos)
print(f"Clase preajustada para los valores (5, 5): {C_preajustada_1[0]}")
