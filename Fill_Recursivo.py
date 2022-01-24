import matplotlib.pyplot as plt

plt.title("Bresenham")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")


def LerPixel(ponto_X,ponto_Y,Pintados,result):
    branco = '-w'
    edgecolor = '-r'
    color ='-b'

    if (ponto_X,ponto_Y) in (result):
        return edgecolor
    if (ponto_X,ponto_Y) in (Pintados):
        return color
    else:
        print("Chamou")
        return branco 

def FloodFill(ponto_X,ponto_Y,edgecolor,color,Pintados,result):
    tupla = ()
    
    current = LerPixel(ponto_X,ponto_Y,Pintados,result)
    print(current)
    if current != edgecolor and current != color:
        tupla = (ponto_X,ponto_Y)
        Pintados.append(tupla)
        
        FloodFill(ponto_X+1,ponto_Y,edgecolor,color,Pintados,result)
        tupla = (ponto_X,ponto_Y)
        Pintados.append(tupla)
        
        FloodFill(ponto_X,ponto_Y+1,edgecolor,color,Pintados,result)
        tupla = (ponto_X,ponto_Y)
        Pintados.append(tupla)
        
        FloodFill(ponto_X-1,ponto_Y,edgecolor,color,Pintados,result)
        tupla = (ponto_X,ponto_Y)
        Pintados.append(tupla)
        
        FloodFill(ponto_X,ponto_Y-1,edgecolor,color,Pintados,result)
        tupla = (ponto_X,ponto_Y)
        Pintados.append(tupla)

    
            
    

def main():
    X_Vet = [-3,-1,6,3,-4,-3] #TESTE 1
    Y_Vet = [-2,4,1,10,9,-2]
    n = 6
    result = []
    edgecolor = '-r'
    color ='-b'
    Pintados = []
    Y_pintados = []


    for i in range (n-1):
        x1 = X_Vet[i]
        x2 = X_Vet[i+1]
        y1 = Y_Vet[i]
        y2 = Y_Vet[i+1]
        result.extend(reflexao(x1, y1, x2, y2))
        print("Reultado X:" ,result)
    x,y = zip(*result)
    print("Reultado X:" ,x,"Reultado Y:",y)
    plt.plot('-bo')
    plt.fill('-ro')
    plt.show()
        
    FloodFill(0,6,edgecolor,color,Pintados,result)
    w,z = zip(*Pintados)
    plt.plot('-ro',w,z,'-bo')
    print("X = ",w, "Y = " ,z)
    plt.show()

if __name__ == "__main__":
    main()
