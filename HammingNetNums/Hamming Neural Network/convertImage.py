from PIL import Image, ImageDraw  # Conectemos las bibliotecas necesarias.
import random

def convertImageToBinary(path):
    image = Image.open(path)  #Abrimos la imagen.
    draw = ImageDraw.Draw(image)  #Crear una herramienta de dibujo.
    width = image.size[0]  #Determina el ancho.
    height = image.size[1]  #Determinamos la altura.
    pix = image.load()  #Cargando valores de píxeles.
    factor = 100
    t = []
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if int(S > (((255 + factor) // 2) * 3)):
                a, b, c = 255, 255, 255
                t.append(-1)
            else:
                a, b, c = 0, 0, 0
                t.append(1)
            draw.point((i, j), (a, b, c))
    del draw
    return t

#Función para ruido de imagen
def getNoisyBinaryImage(path):
    image = Image.open(path)  #Abrimos la imagen.
    draw = ImageDraw.Draw(image)  #Crear una herramienta de dibujo.
    width = image.size[0]  #Determina el ancho.
    height = image.size[1]  #Determinamos la altura.
    pix = image.load()  #Cargando valores de píxeles.
    factor = 350
    t = []
    for i in range(width):
        for j in range(height):
            rand = random.randint(-factor, factor)
            a = pix[i, j][0] + rand
            b = pix[i, j][1] + rand
            c = pix[i, j][2] + rand
            if (a < 0):
                a = 0
            if (b < 0):
                b = 0
            if (c < 0):
                c = 0
            if (a > 255):
                a = 255
            if (b > 255):
                b = 255
            if (c > 255):
                c = 255
            draw.point((i, j), (a, b, c))
    image.save("examples of numbers/noisy5.jpg", "JPEG")
    del draw
    return t