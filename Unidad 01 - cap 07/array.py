import numpy as np

arreglo = np.array([2,4,6])
print("Tipo de dato de los elementos del arreglo...", arreglo.dtype)
print("Dimension del arreglo...", arreglo.ndim)
print("Dimension del arreglo, tupla que indica el tamano del arreglo en cada dimension...", arreglo.shape)
print('Numero total de elementos del arreglo...', arreglo.size)
print("El tamano en byte de cada elemento del arreglo...", arreglo.itemsize)

# Figura 6.2
b = np.array([[2,4,6],[1,3,5]])

c = np.array([[1,2],[4,5]], dtype=complex)
print(c)

# Figura 6.4
d = np.arange(1,10,2)
print('np.arange(1,10,2)...\n', d)

# Figura 6.5
d = np.arange(2, 6, 0.3).reshape(2,7)
print('np.arange(2, 6, 0.3).reshape(2,7)...\n',d)

# Fig 6.6
e = np.linspace(1, 10, 8)
print('np.linspace...\n', e)

# Fig 6.7
e = np.random.rand(10)
print('np.random.rand(10)...\n',e)

# Figura 6.8
e = np.random.rand(3,4)
print('np.random.rand(3,4)...\n',e)
