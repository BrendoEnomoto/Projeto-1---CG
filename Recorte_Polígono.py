from unittest import result
import matplotlib.pyplot as plt

plt.title("Bresenham")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

    
def recorta_poligono(left,top,right,bottom,X_Vet,Y_Vet):
    result_x_1 = []
    result_y_1 = []
    result_x_2 = []
    result_y_2 = []
    result_x_3 = []
    result_y_3 = []
    result_x_4 = []
    result_y_4 = []
    result = []
    tupla = ()
    tamanho_lista = len(X_Vet)
    
    for i in range(len(X_Vet)):
        print("Entrou no IF ",i)
        if X_Vet[i] >= left:
            if X_Vet[(i+1)%tamanho_lista] >=left:
                result_x_1.append(X_Vet[(i+1)%tamanho_lista]),result_y_1.append(Y_Vet[(i+1)%tamanho_lista])
            else:
                result_x_1.append(left),result_y_1.append(round(left - X_Vet[i]) * (Y_Vet[(i+1)%tamanho_lista] - Y_Vet[i] * 1) / (X_Vet[(i+1)%tamanho_lista]*1 - X_Vet[i])+ Y_Vet[i])
        else:
            if (X_Vet[(i+1)%tamanho_lista]>=left):
                result_x_1.append(left),result_y_1.append(round(left - X_Vet[i]) * (Y_Vet[(i+1)%tamanho_lista] - Y_Vet[i] * 1) / (X_Vet[(i+1)%tamanho_lista]*1 - X_Vet[i])+ Y_Vet[i])
                #result_x_1.append(left),result_y_1.append(round(left - X_Vet[i]) * (Y_Vet[i+1] - Y_Vet[i] * 1) / (X_Vet[i+1]*1 - X_Vet[i]) + Y_Vet[i])
                result_x_1.append(X_Vet[(i+1)%tamanho_lista]),result_y_1.append(Y_Vet[(i+1)%tamanho_lista])
            else:
                print("Não adiciona nada")

    #print("Result X FINAL=",result_x_1,"Resultado Y= ",result_y_1)

    for i in range(len(result_x_1)):
        if result_x_1[i] <= right:
            print("Result X FFF=",result_x_1,"Resultado Y= ",result_y_1)
            tamanho_lista = len(result_x_1)
            if result_x_1[(i+1)%tamanho_lista] <=right:
                result_x_2.append(result_x_1[(i+1)%tamanho_lista]),result_y_2.append(result_y_1[(i+1)%tamanho_lista])
            else:
                result_x_2.append(right),result_y_2.append(round(right - result_x_1[i]) * (result_y_1[(i+1)%tamanho_lista] - result_y_1[i] * 1) / (result_x_1[(i+1)%tamanho_lista]*1 - result_x_1[i])+ result_y_1[i])
        else:
            print("Result X FFF=",result_x_1,"Resultado Y= ",result_y_1)
            if result_x_1[(i+1)%tamanho_lista] <= right:
                result_x_2.append(right),result_y_2.append(round(right - result_x_1[i]) * (result_y_1[(i+1)%tamanho_lista] - result_y_1[i] * 1) / (result_x_1[(i+1)%tamanho_lista]*1 - result_x_1[i])+ result_y_1[i])
                result_x_2.append(result_x_1[(i+1)%tamanho_lista]),result_y_2.append(result_y_1[(i+1)%tamanho_lista])
            else:
                print("Não adiciona nada 2")
    print("Result X2 =",result_x_2,"Resultado Y2= ",result_y_2)


    for i in range(len(result_x_2)):
        if result_y_2[i] <= top:
            tamanho_lista = len(result_x_2)
            if result_y_2[(i+1)%tamanho_lista] <=top:
                print("Result X2 SSSS=",result_x_2,"Resultado Y2= ",result_y_2)
                result_x_3.append(result_x_2[(i+1)%tamanho_lista]),result_y_3.append(result_y_2[(i+1)%tamanho_lista])
            else:
                result_x_3.append(round(top - result_y_2[i]) * (result_x_2[(i+1)%tamanho_lista] - result_x_2[i]*1) /  (result_y_2[(i+1)%tamanho_lista] - result_y_2[i])  + result_x_2[i]), result_y_3.append(top)
        else:
            
            if result_y_2[(i+1)%tamanho_lista] <= top:
                result_x_3.append(round(top - result_y_2[i]) * (result_x_2[(i+1)%tamanho_lista] - result_x_2[i]*1) /  (result_y_2[(i+1)%tamanho_lista] - result_y_2[i])  + result_x_2[i]), result_y_3.append(top)
                result_x_3.append(result_x_2[(i+1)%tamanho_lista]),result_y_3.append(result_y_2[(i+1)%tamanho_lista])
            else:
                print("Não adiciona nada 2")
    print("Result X3 =",result_x_3,"Resultado Y3= ",result_y_3)


    for i in range(len(result_x_3)):
        if result_y_3[i] >= bottom:
            tamanho_lista = len(result_x_3)
            if result_y_3[(i+1)%tamanho_lista] >bottom:
                print("Result X2 SSSS=",result_x_2,"Resultado Y2= ",result_y_2)
                result_x_4.append(result_x_3[(i+1)%tamanho_lista]),result_y_4.append(result_y_3[(i+1)%tamanho_lista])
            else:
                result_x_4.append(round(bottom - result_y_3[i]) * (result_x_3[(i+1)%tamanho_lista] - result_x_3[i]*1) /  (result_y_3[(i+1)%tamanho_lista] - result_y_3[i])  + result_x_3[i]), result_y_4.append(bottom)
        else:
            
            if result_y_3[(i+1)%tamanho_lista] >= bottom:
                result_x_4.append(round(bottom - result_y_3[i]) * (result_x_3[(i+1)%tamanho_lista] - result_x_3[i]*1) /  (result_y_3[(i+1)%tamanho_lista] - result_y_3[i])  + result_x_3[i]), result_y_4.append(bottom)
                result_x_4.append(result_x_3[(i+1)%tamanho_lista]),result_y_4.append(result_y_3[(i+1)%tamanho_lista])
            else:
                print("Não adiciona nada 2")

    result_x_4.append(result_x_4[0]),result_y_4.append(result_y_4[0])
    print("X = ",result_x_4,"Y = ",result_y_4)
    
    n = len(result_x_4)
    for i in range(n):
        tupla = (result_x_4[i],result_y_4[i])
        result.append(tupla)
    return result

    
def main():
    result = []
    left = -0
    top = 10
    right = 10
    bottom = 0

    X_Vet = [-3,12,12,7,12,12] #TESTE 1
    Y_Vet = [4,13,6,4,2,-4]

    result.extend(recorta_poligono(left,top,right,bottom,X_Vet,Y_Vet))
    x,y = zip(*result)
    plt.plot(x,y,'-bo')
    plt.show()
    


if __name__ == "__main__":
    main()
