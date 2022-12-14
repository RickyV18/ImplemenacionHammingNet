from pylab import *
from math import sqrt
import matplotlib.pyplot as plt
import convertImage as convertModule
import os

IMAGE_PATH = "Hamming Neural Network/test numbers/noisy4.jpg"

def show(s):  #función para la visualización de matrices
    for j in range(len(s)):
        for i in range(len(s[0])):
            print("{:3f}".format(s[j][i]), end=" ")
        print(sep="")


def change(v, a, b):  #función para transformar el vector v en una matriz de tamaños dados a y b
    t = [[0 for j in range(a)] for i in range(b)]
    k = 0
    j = 0
    while k < b:
        i = 0
        while i < a:
            t[k][i] = v[j]
            j += 1
            i += 1
        k += 1
    return t


def product(w, y, T):  #función de multiplicación matriz-vector
    z = []
    for i in range(len(w)):
        x = 0
        for j in range(len(y)):
            x = x + w[i][j] * y[j]
        z.append((x + T))
    return z


def action(s, T, Emax):  #función de activación
    t = []
    for i in s:
        if i <= 0:
            t.append(0)
        elif 0 < i <= T:
            t.append(Emax * i)
        elif i > T:
            t.append(T)
    return t


def mysum(y, j):  #función para calcular la suma de valores vectoriales para i != j
    p = 0
    sum = 0
    while p < len(y):
        if p != j:
            sum = sum + y[p]
        p += 1
    return sum


def norm(v, p):  #función que calcula la diferencia de dos vectores y calcula la norma del vector resultante
    t = []
    for i in range(len(v)):
        t.append(v[i] - p[i])
    sum = 0
    for i in t:
        sum += i * i
    return sqrt(sum)


path = ['Hamming Neural Network/examples of numbers/1.jpg',
        'Hamming Neural Network/examples of numbers/2.jpg',
        'Hamming Neural Network/examples of numbers/3.jpg',
        'Hamming Neural Network/examples of numbers/4.jpg',
        'Hamming Neural Network/examples of numbers/5.jpg',
        ]
x = []
print(os.path.basename(IMAGE_PATH))
for i in path:
    x.append(convertModule.convertImageToBinary(i))
y = convertModule.convertImageToBinary(IMAGE_PATH)
entr = y
k = len(x)
#Número de píxeles
a = 40
b = 40
entr = y
q = change(y, a, b)
plt.matshow(q)
plt.colorbar()

m = len(x[0])
w = [[(x[i][j]) / 2 for j in range(m)] for i in range(k)]  # Matriz de pesos
T = m / 2  # parámetro de la función de activación
e = round(1 / len(x), 1)
E = [[0 for j in range(k)] for i in range(k)]  # Los valores de las sinapsis de retroalimentación de las neuronas de la segunda 
                                                #capa se establecen en forma de elementos de una matriz cuadrada de tamaño K x K:

Emax = 0.000001  #el valor máximo permitido de la norma de la diferencia de vectores de salida en dos iteraciones sucesivas
U = 1 / Emax
for i in range(k):
    for j in range(k):
        if j == i:
            E[i][j] = 1.0
        else:
            E[i][j] = -e
s = [product(w, y, T)]
p = action(s[0], U, Emax)
y = [p]
i = 0
j = []
p = [0 for j in range(len(s[0]))]
while norm(y[i], p) >= Emax:
    s.append([0 for j in range(len(s[0]))])
    for j in range(len(s[0])):
        s[i + 1][j] = y[i][j] - e * mysum(y[i], j)
    y.append((action(s[i + 1], U, Emax)))
    i += 1
    p = y[i - 1]
print('Tabla de valores de salida:')
show(y)
print('Último valor de salida: ', *y[len(y) - 1])
j = []
i = 0
result_index = y[len(y) - 1].index(max(y[len(y) - 1])) + 1
if max(y[len(y) - 1]) == 0:
    print("La red Hamming no puede dar preferencia entre clases",
          "\nDada una pequeña cantidad de características de entrada, se debe concluir que la red no pudo clasificar la imagen en absoluto, en lugar de que la atribuyó igualmente a las clases anteriores.")
    plt.show()
    exit()
else:
    q = change(x[result_index - 1], a, b)
    print('Valor de salida positivo (mayor)', result_index,
          '\n - La neurona indica que la imagen de entrada ruidosa debe atribuirse a', result_index, '- mi clase')
    plt.matshow(q)
    plt.colorbar()
    plt.show()
