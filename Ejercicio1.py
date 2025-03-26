import numpy as np  
from sklearn.neighbors import KNeighborsClassifier 

# Datos de entrenamiento del Modelo
MatrizX = np.array([[2, 0],[4, 4],[1, 1],[2, 4],[2, 2],[2, 3],[3, 4],[3, 3]])
Clases = np.array([0, 1, 0, 1, 0, 1, 0, 1]) 

# Configurar el clasificador K-NN con k=1
KNN = KNeighborsClassifier(n_neighbors=1, metric='manhattan')
KNN.fit(MatrizX, Clases)

# Clasificar el nuevo caso (2.5, 2.5)
Casos = np.array([[2.5, 2.5]])
C_preajustada_1 = KNN.predict(Casos)
print(f"Clase preajustada para los valores (2.5, 2.5): {C_preajustada_1[0]}")