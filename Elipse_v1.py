import matplotlib.pyplot as plt

plt.title("Bresenham")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")


def Eplipse_Bres(raio_A: float, raio_B:float, x_centro:float, y_centro:float):
    valores_x = []
    valores_y = []


    A_Quad = raio_A * raio_A
    B_Quad = raio_B * raio_B

    x = 0
    y = raio_B

    dx = 2 * B_Quad * x
    dy = 2 * A_Quad * y


    #Calculos para a primeira região do primeiro quadrante
    e = -raio_B * A_Quad + A_Quad * 0.25
    
    
    
    while dx < dy:
        valores_x.append(x + x_centro), valores_y.append(y + y_centro)
        valores_x.append(-x + x_centro), valores_y.append(y + y_centro)
        valores_x.append(x + x_centro), valores_y.append(-y + y_centro)
        valores_x.append(-x + x_centro), valores_y.append(-y + y_centro)
        x = x + 1
        e = e + dx + B_Quad
        print(" E 1: ",e)
        dx = dx + 2 * B_Quad
        if e > 0:
            y = y -1
            e = e + A_Quad - dy
            dy = dy - 2 * A_Quad
        

    #Calculos para a segunda região do primeiro quadrante
    e = B_Quad*((x+0.5)*(x+0.5)) + A_Quad * y *y - A_Quad * B_Quad
    

    while y>=0:
        valores_x.append(x + x_centro), valores_y.append(y + y_centro)
        valores_x.append(-x + x_centro), valores_y.append(y + y_centro)
        valores_x.append(x + x_centro), valores_y.append(-y + y_centro)
        valores_x.append(-x + x_centro), valores_y.append(-y + y_centro)
        
        #print(x,y,x_centro,y_centro) 
        y = y - 1
        e = e + A_Quad - dy
        print(" E 2: ",e)
        dy = dy - 2 * A_Quad
        if e<0:
            x = x +1
            e = e + dx + B_Quad
            dx = dx + 2 * B_Quad
    
    print('x = %s, y = %s' % (valores_x , valores_y))
    

    n = len(valores_x)

    result = []
    tupla = ()
    for i in range(n):
        tupla = (valores_x[i],valores_y[i])
        result.append(tupla)
    return result


def main():
    x_centro: float
    y_centro: float
    raio_A: float
    raio_B: float

    result_x = []


    x_centro = int(input("Qual o valor inicial do x inicial? "))
    y_centro = int(input("Qual o valor inicial do y inicial? "))
    raio_A = int(input("Qual o valor do raio A? "))
    raio_B = int(input("Qual o valor do raio B? "))
    
    
    result_x.extend(Eplipse_Bres(raio_A, raio_B, x_centro, y_centro))
    x,y = zip(*result_x)

    plt.plot(x,y,'-bo')
    plt.show()


if __name__ == "__main__":
    main()
