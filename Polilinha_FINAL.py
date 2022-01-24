import matplotlib.pyplot as plt

plt.title("Bresenham")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")


def reflexao(x1, y1, x2, y2):
    result_x = []
    x, y = x1, y1
    delta_x = abs(x2 - x1)
    delta_y = abs(y2 - y1)
    if delta_x>0:
        ponto_medio = delta_y/float(delta_x)
    else:
        ponto_medio = delta_y
    
    
    if ponto_medio > 1 or ponto_medio < -1:
        delta_x, delta_y = delta_y, delta_x
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        trocaxy = True
        Trocax = False
        Trocay = False
        print ("Trocou x por y")
        result_x.extend(Linha_Bres(x1, y1, x2, y2,Trocax,Trocay,trocaxy))

        print ("Chamou Linha_Bres")
        return result_x
        
    else:
        Trocax = False
        Trocay = False
        trocaxy = False
        print ("Entrou no else")
        result_x.extend(Linha_Bres(x1, y1, x2, y2,Trocax,Trocay,trocaxy))
        return result_x
        

def Linha_Bres(x1, y1, x2, y2,Trocax,Trocay,trocaxy):
    x, y = x1, y1
    delta_x = abs(x2 - x1)
    delta_y = abs(y2 - y1)
    if delta_x>0:
        ponto_medio = delta_y/float(delta_x)
    else:
        ponto_medio = delta_y
    delta = ponto_medio - float(1/2)


    valores_x = [x]
    valores_y = [y]
    
    while x < x2 and y1 < y2:
        print("Entrou no CASO 1!!!")
        if delta >= 0:
            y = y + 1
            delta = delta - 1
        x = x + 1
        delta  = delta + ponto_medio
        
        if Trocax == True:
            print("TRue1")
            valores_x.append(-x)
        if Trocay == True:
            print("Trueee2")
            valores_x.append(+x)
            valores_y.append(+y)
        else:
            print("true3")
            valores_x.append(x)
            valores_y.append(y)
        print('x = %s, y = %s' % (x, y))


    while x < x2 and y1 >= y2:
        print("Entrou no CASO 2!!!")
        print(delta)
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
        print('x = %s, y = %s' % (x, y))    
    
    
    while x > x2 and y1 > y2:
        print("Entrou no CASO 3!!!")
        if delta >= 0:
            y = y - 1
            delta = delta - 1
        x = x - 1
        delta  = delta + ponto_medio
        
        if Trocax == True:
            print("TRue1")
            valores_x.append(-x)
        if Trocay == True:
            print("Trueee2")
            valores_x.append(+x)
            valores_y.append(+y)
        else:
            print("true3")
            valores_x.append(x)
            valores_y.append(y)
        print('x = %s, y = %s' % (x, y))


    while x > x2 and y <= y2:
        print("Entrou no CASO 4!!!")
        if delta >= 0:
            y = y + 1
            delta = delta - 1
        x = x - 1
        delta  = delta + ponto_medio
        
        if Trocax == True:
            print("TRue1")
            valores_x.append(-x)
        if Trocay == True:
            print("Trueee2")
            valores_x.append(+x)
            valores_y.append(+y)
        else:
            print("true3")
            valores_x.append(x)
            valores_y.append(y)
        print('x = %s, y = %s' % (x, y))
    
    if trocaxy == True:
            valores_x , valores_y = valores_y , valores_x
            print('x = %s, y = %s' % (valores_x , valores_y))
            trocaxy = False    

   
    print("X = ",valores_x,"Y = ",valores_y)    
    
    n = len(valores_x)

    result = []
    tupla = ()
    for i in range(n):
        tupla = (valores_x[i],valores_y[i])
        result.append(tupla)
    return result

    
    


