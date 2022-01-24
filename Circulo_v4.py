import matplotlib.pyplot as plt

plt.title("Bresenham")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")


def Circulo_Bres(x, y, x_centro, y_centro): #remover o "e" pois pode dar errado!
    valores_x = []
    valores_y = []
    result = []
    tupla = ()
    
    valores_x.append(x + x_centro), valores_y.append(y + y_centro)
    valores_x.append(y + x_centro), valores_y.append(x + y_centro)
    valores_x.append(y + x_centro), valores_y.append(-x + y_centro)
    valores_x.append(x + x_centro), valores_y.append(-y + y_centro)
    valores_x.append(-x + x_centro), valores_y.append(-y + y_centro)
    valores_x.append(-y + x_centro), valores_y.append(-x + y_centro)
    valores_x.append(-y + x_centro), valores_y.append(x + y_centro)
    valores_x.append(-x + x_centro), valores_y.append(y + y_centro)

    n = len(valores_x)
    for i in range(n):
        tupla = (valores_x[i],valores_y[i])
        result.append(tupla)
    return result