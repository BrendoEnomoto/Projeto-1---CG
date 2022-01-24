import matplotlib.pyplot as plt

plt.title("Bresenham")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")


def reflexao(x1, y1, x2, y2):
    x, y = x1, y1
    delta_x = abs(x2 - x1)
    delta_y = abs(y2 - y1)
    ponto_medio = delta_y/float(delta_x)
    Result_X = []
    #delta = ponto_medio - float(1/2)

    if ponto_medio > 1 or ponto_medio < -1:
        delta_x, delta_y = delta_y, delta_x
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        trocaxy = True
        Trocax = False
        Trocay = False
        Result_X.extend(Linha_Bres(x1, y1, x2, y2,Trocax,Trocay,trocaxy))
        return Result_X
    else:
        Trocax = False
        Trocay = False
        trocaxy = False
        Result_X.extend(Linha_Bres(x1, y1, x2, y2,Trocax,Trocay,trocaxy))
        return Result_X
        

def Linha_Bres(x1, y1, x2, y2,Trocax,Trocay,trocaxy):
    x, y = x1, y1
    delta_x = abs(x2 - x1)
    delta_y = abs(y2 - y1)
    ponto_medio = delta_y/float(delta_x)

    delta = ponto_medio - float(1/2)


    valores_x = [x]
    valores_y = [y]
    
    while x < x2 and y1 < y2:
        if delta >= 0:
            y = y + 1
            delta = delta - 1
        x = x + 1
        delta  = delta + ponto_medio
        
        if Trocax == True:
            valores_x.append(-x)
        if Trocay == True:
            valores_x.append(+x)
            valores_y.append(+y)
        else:
            valores_x.append(x)
            valores_y.append(y)


    while x < x2 and y1 > y2:
        if delta >= 0:
            y = y - 1
            delta = delta - 1
        x = x + 1
        delta  = delta + ponto_medio
        
        if Trocax == True:
           valores_x.append(-x)
        if Trocay == True:
            valores_y.append(-y)
        else:
            valores_x.append(x)
            valores_y.append(y)    
    
    
    while x > x2 and y1 > y2:
        if delta >= 0:
            y = y - 1
            delta = delta - 1
        x = x - 1
        delta  = delta + ponto_medio
        
        if Trocax == True:
            valores_x.append(-x)
        if Trocay == True:
            valores_x.append(+x)
            valores_y.append(+y)
        else:
            valores_x.append(x)
            valores_y.append(y)


    while x > x2 and y <= y2:
        
        if delta >= 0:
            y = y + 1
            delta = delta - 1
        x = x - 1
        delta  = delta + ponto_medio
        
        if Trocax == True:
            valores_x.append(-x)
        if Trocay == True:
            valores_x.append(+x)
            valores_y.append(+y)
        else:
            valores_x.append(x)
            valores_y.append(y)
        
    
    if trocaxy == True:
            valores_x , valores_y = valores_y , valores_x
            #print('x = %s, y = %s' % (valores_x , valores_y))
            trocaxy = False    
        
      
    #plt.plot(valores_x, valores_y,"-bo")
    #plt.show()

    n = len(valores_x)

    result = []
    tupla = ()
    for i in range(n):
        tupla = (valores_x[i],valores_y[i])
        result.append(tupla)
    
    return result



