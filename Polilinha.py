from unittest import removeResult
import matplotlib.pyplot as plt
import numpy as np
plt.title("Bresenham")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")


def reflexao(x1, y1, x2, y2):
    x, y = float(x1), float(y1)
    delta_x = float(abs(x2 - x1))
    delta_y = float(abs(y2 - y1))
    result_x = []
    if float(delta_x) >0:
        ponto_medio = float(delta_y)/float(delta_x)
    else:
        ponto_medio = float(delta_y)

    

    if ponto_medio > 1 or ponto_medio < -1:
        delta_x, delta_y = float(delta_y), float(delta_x)
        x, y = float(y), float(x)
        x1, y1 = float(y1), float(x1)
        x2, y2 = y2, x2
        trocaxy = True
        Trocax = False
        Trocay = False
        result_x.extend(Linha_Bres(x1, y1, x2, y2,Trocax,Trocay,trocaxy))

        return result_x
        
    else:
        Trocax = False
        Trocay = False
        trocaxy = False
        result_x.extend(Linha_Bres(x1, y1, x2, y2,Trocax,Trocay,trocaxy))
        return result_x
        

def Linha_Bres(x1, y1, x2, y2,Trocax,Trocay,trocaxy):
    x, y = x1, y1
    delta_x = float(abs(x2 - x1))
    delta_y = float(abs(y2 - y1))
    if float(delta_x) >0:
        ponto_medio = float(delta_y)/float(delta_x)
    else:
        ponto_medio = float(delta_y)
    delta = float(ponto_medio) - float(1/2)
   

    valores_x = [x]
    valores_y = [y]
    
    while x < x2 and y1 < y2:
        if delta >= 0:
            y = float(y + 1)
            delta = delta - 1
        x = float(x + 1)
        delta  = float(delta + ponto_medio)
        
        if Trocax == True:
            valores_x.append(-x)
        if Trocay == True:
            valores_x.append(+x)
            valores_y.append(+y)
        else:
            valores_x.append(x)
            valores_y.append(y)


    while x < x2 and y1 >= y2:
        if delta >= 0:
            y = float(y - 1)
            delta = delta - 1
        x = float(x + 1)
        delta  = float(delta + ponto_medio)
        
        if Trocax == True:
           valores_x.append(-x)
        if Trocay == True:
            valores_y.append(-y)
        else:
            valores_x.append(x)
            valores_y.append(y) 
    
    
    while x > x2 and y1 > y2:
        if delta >= 0:
            y = float(y - 1)
            delta = float(delta - 1)
        x = float(x - 1)
        delta  = float(delta + ponto_medio)
        
        if Trocax == True:
            valores_x.append(-x)
        if Trocay == True:
            valores_x.append(+x)
            valores_y.append(+y)
        else:
            valores_x.append(float(x))
            valores_y.append(float(y))


    while x > x2 and y <= y2:
        if delta >= 0:
            y = float(y + 1)
            delta = float(delta - 1)
        x = float(x - 1)
        delta  = float(delta + ponto_medio)
        
        if Trocax == True:
            valores_x.append(-x)
        if Trocay == True:
            valores_x.append(+x)
            valores_y.append(+y)
        else:
            valores_x.append(float(x))
            valores_y.append(float(y))
    
    if trocaxy == True:
            valores_x , valores_y = valores_y , valores_x
            trocaxy = False    
   
    #return valores_x + valores_y
    #return valores_x,valores_y
    n = len(valores_x)

    result = []
    tupla = ()
    for i in range(n):
        tupla = (valores_x[i],valores_y[i])
        result.append(tupla)
    return result

    
def plot(Coordinates):
    
    coordinates = np.around(Coordinates)
    
    X_Vet = coordinates[0]
    Y_Vet = coordinates[1]
    
    n = len(X_Vet)
    
    result_x = []
       
    for i in range (n):
        x1 = X_Vet[i]
        x2 = X_Vet[(i+1)%n]
        y1 = Y_Vet[i]
        y2 = Y_Vet[(i+1)%n]
        result_x.extend(reflexao(x1, y1, x2, y2))
        x,y = zip(*result_x)
    result = np.array([x,y])
    
    return result
    #plt.plot(x,y,'-bo')
    #plt.show()    

def main():
    if __name__ == "__main__":
        main()
