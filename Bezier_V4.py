import matplotlib.pyplot as plt

plt.title("Bresenham")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")


def Bezierpoit(n,ctrl_pts_x,ctrl_pts_y,meio):
    pts_x = []
    pts_y = []
    result_x = []

    for i in range (n+1):
        #pts_x = ctrl_pts_x
        pts_x.append(ctrl_pts_x[i])
        pts_y.append(ctrl_pts_y[i])
    r=1
    for r in range (r,n):
        for i in range (n):
            pts_x[i] = ((1-meio) * pts_x[i] + meio * pts_x[i+1])
            pts_y[i] = ((1-meio) * pts_y[i] + meio * pts_y[i+1])
    print("Pontos: ",ctrl_pts_x,ctrl_pts_y)
    print("Controle: ",pts_x,pts_y)
    result_x.extend(reflexao(ctrl_pts_x,ctrl_pts_y,pts_x,pts_y,n))
    return result_x
                  

def reflexao(X_Vet, Y_Vet, pts_x, pts_y, n):
    x = [n]
    y = [n]
    #x[0], y[0] = X_Vet[0], Y_Vet[0]
    delta_x = []
    delta_y = []
    delta = []
    ponto_medio = []
    print("XXXVET",X_Vet)
    print("YYYVET",Y_Vet)
    result_x = []

    for i in range(n-(n-1)):
        delta_x.append(X_Vet[i+1] - X_Vet[i])
        delta_y.append(Y_Vet[i+1] - Y_Vet[i])
    
        ponto_medio.append(delta_y[i]/float(delta_x[i]))
        print ("Delta: ",delta_y,delta_x)
        print ("POnto Medio: ",ponto_medio)
        delta.append(ponto_medio[i] - float(1/2))

    for i in range(n-(n-1)):    
        if ponto_medio[i] >= 1 or ponto_medio[i] <= -1:
            delta_x, delta_y = delta_y, delta_x
            X_Vet, Y_Vet = Y_Vet,X_Vet
            #x[i], y[i] = y[i], x[i]
            #x[i+1], y[i+1] = y[i+1], x[i+1]
            trocaxy = True
            Trocax = False
            Trocay = False
            print ("Trocou x por y")
            if X_Vet[i] > X_Vet[i+1]:
                X_Vet[i], X_Vet[i+1] = -Y_Vet[i], -Y_Vet[i+1]
                Trocax = True
                print ("Negativou x")
            if Y_Vet[i] > Y_Vet[i+1]:
                Y_Vet[i], Y_Vet[i+1] = -Y_Vet[i], -Y_Vet[i+1]
                Trocay = True
                print ("Negativou y")
            print ("Chamou Linha_Bres")
            result_x.extend(Linha_Bres(X_Vet, Y_Vet,pts_x, pts_y, n,Trocax,Trocay,trocaxy))
            return result_x
        else:
            Trocax = False
            Trocay = False
            trocaxy = False
            print ("Entrou no else AQUI")
            result_x.extend(Linha_Bres(X_Vet, Y_Vet,pts_x, pts_y, n,Trocax,Trocay,trocaxy))
            return result_x

def Linha_Bres(X_Vet, Y_Vet,pts_x, pts_y, n,Trocax,Trocay,trocaxy):
    print(X_Vet)
    x = [n]
    y = [n]
    delta_x = []
    delta_y =[]
    #x[0], y[0] = X_Vet[0], Y_Vet[0]
    valores_x = [X_Vet[0]]
    valores_y = [Y_Vet[0]]
    delta = []
    ponto_medio = []
    
    for i in range(n):
        delta_x.append(X_Vet[i+1] - X_Vet[i])
        delta_y.append(Y_Vet[i+1] - Y_Vet[i])
        print(delta_x)
        print(delta_y)
        ponto_medio.append(delta_y [i]/(delta_x[i]))
        print ("Delta: ",delta_y,delta_x)
        print ("POnto Medio: ",ponto_medio)

        delta.append(ponto_medio[i] - float(1/2))
        
        print(X_Vet)
        print(Y_Vet)
    for i in range(n):
        while X_Vet[i] < X_Vet[i+1]:
            print("entrou aqui 2")
            if delta[i] >= 0:
                print("entrou aqui 3")
                Y_Vet[i]+=1
                delta[i]-=1
            X_Vet[i]=(X_Vet[i]+1)
            print('Delta Antes: ',delta)
            delta[i]+= ponto_medio[i]
            print('Delta Depois: ',delta)
                    
            if Trocax == True:
                valores_x.append(-X_Vet[i])
            if Trocay == True:
                valores_y.append(-Y_Vet[i])
            else:
                print("PEGOU",X_Vet[i])
                valores_x.append(X_Vet[i])
                valores_y.append(Y_Vet[i])
                #print('x = %s, y = %s' % (x_Vet[i], Y_Vet[i]))      
    if trocaxy == True:
            valores_x , valores_y = valores_y , valores_x
            print('x = %s, y = %s' % (valores_x , valores_y))
            trocaxy = False

    q = len(valores_x)

    result = []
    tupla = ()
    for i in range(q):
        tupla = (valores_x[i],valores_y[i])
        result.append(tupla)
    return result                     


