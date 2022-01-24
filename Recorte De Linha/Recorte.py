from tkinter import *
from tkinter.ttk import *


## parametros iniciais
tamanhoTela = 600 
tamanhoPixel = int(tamanhoTela / 50)

## criar o canvas utilizando o tkinter
master = Tk()
tela = Canvas(master, width=tamanhoTela, height=tamanhoTela)
tela.grid()


## função que cria a grade
def CriarTemplate():
  aux = int(tamanhoTela / 2) + (tamanhoPixel / 2)

  for x in range(0, tamanhoTela, tamanhoPixel): # linhas horizontais
    tela.create_line(x, 0, x, tamanhoTela, fill='#808080')

  for y in range(0, tamanhoTela, tamanhoPixel): # linhas horizontais
    tela.create_line(0, y, tamanhoTela, y, fill='#808080')

  tela.create_line(0, aux - tamanhoPixel, tamanhoTela, aux - tamanhoPixel, fill="#f00") # linha central - horizontal
  tela.create_line(aux, 0, aux, tamanhoTela, fill="#f00") # linha central - vertical


def ConverterCoordenadas(x, y): # converter coordenadas para o sistema de grade
  real_x = int((tamanhoPixel * x) + (tamanhoTela / 2))
  real_y = int((tamanhoTela / 2) - (tamanhoPixel * y))

  return real_x, real_y


def DesenharPixel(x, y, cor): # desenha um pixel na grade
  n = len(x)

  for i in range(n):
    x1, y1 = ConverterCoordenadas(x[i], y[i])
    tela.create_rectangle(x1, y1, x1 + tamanhoPixel, y1 - tamanhoPixel, fill=cor)


def funcao_selecionada():
  selecionado = combo.get()
  X_Vet = [] #[-3,-1,6,3,-4,-3] #TESTE 1
  Y_Vet = [] #[-2,4,1,10,9,-2]
  stringX = []
  stringY = []
  result_x = []

  if selecionado == "1 - Recortar Linha":
    x1 = int((e.get())) # 10   # teste 2  # -1
    y1 = int((f.get())) # -5   # teste 2  # 5
    x2 = int((g.get())) # 30   # teste 2  # 3
    y2 = int((h.get())) # 10   # teste 2  # 8
    xmin = int((i.get())) # 0  # teste 2  # -3
    ymin = int((j.get())) # 0  # teste 2  # 1
    xmax = int((k.get())) # 25 # teste 2  # 2
    ymax = int((l.get())) # 25 # teste 2  # 6


    recorta_linha(x1, y1, x2, y2, xmin, xmax, ymin, ymax)
    #DesenharPixel(x,y, '#808080')  

def InsereValor(event):
 

  selecionado = combo.get()

  if selecionado == "1 - Recortar Linha":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)  
    h.grid(column = 15, row = 4)
    i.grid(column = 15, row = 5)
    j.grid(column = 15, row = 6)
    k.grid(column = 15, row = 7)
    l.grid(column = 15, row = 8)


    Mesagem_Inicial_x1= Label(master, text= "Qual o valor inicial de x? ")
    Mesagem_Inicial_x1.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_y1= Label(master, text= "Qual o valor inicial de y? ")
    Mesagem_Inicial_y1.grid(column = 10, row= 2, pady= 10)  
    Mesagem_Inicial_x2= Label(master, text= "Qual o valor final de x? ")
    Mesagem_Inicial_x2.grid(column = 10, row= 3, pady= 10)  
    Mesagem_Inicial_y2= Label(master, text= "Qual o valor final de y?")
    Mesagem_Inicial_y2.grid(column = 10, row= 4, pady= 10)  
    
    Mesagem_Inicial_xmin= Label(master, text= "Qual o valor do x mínimo? ")
    Mesagem_Inicial_xmin.grid(column = 10, row= 5, pady= 10) 
    Mesagem_Inicial_ymin= Label(master, text= "Qual o valor do y mínimo? ")
    Mesagem_Inicial_ymin.grid(column = 10, row= 6, pady= 10)  
    Mesagem_Inicial_xmax= Label(master, text= "Qual o valor do x máximo? ")
    Mesagem_Inicial_xmax.grid(column = 10, row= 7, pady= 10)
    Mesagem_Inicial_ymax= Label(master, text= "Qual o valor do y máximo? ")
    Mesagem_Inicial_ymax.grid(column = 10, row= 8, pady= 10)  

    botao = Button(master,text="Desenhar Linha Clipada",command=funcao_selecionada)        
    botao.grid(column = 15, row = 9, pady= 10) 
  

combo = Combobox(master)
combo ['values'] = ("Selecionar","1 - Recortar Linha")
combo.current(0)
combo.grid(column = 15, row = 0)
combo.bind("<<ComboboxSelected>>", InsereValor)
e = Entry(master)
f = Entry(master)
g = Entry(master)
h = Entry(master)
i = Entry(master)
j = Entry(master)
k = Entry(master)
l = Entry(master)

def recorta_linha(x1, y1, x2, y2,xmin,xmax,ymin,ymax):
    c1 = sign(x1,y1,xmin,xmax,ymin,ymax)
    c2 = sign(x2,y2,xmin,xmax,ymin,ymax)
    cord_parcial = 0
    result_x = []
    zero = 0b0000
   
    if c1 | c2 == zero:
        result_x.extend(reflexao(x1, y1, x2, y2))
        x,y = zip(*result_x)
        print("FFFINAL",type(result_x[0]))
        print("FFFINAL",result_x)
        DesenharPixel(x,y, '#808080')
        
    elif c1 & c2 != zero:
        print("Totalmente Fora")
    else:
        #Encontra o valor do bit da diferença através da comparação dos códigos c1 e c2
        comp = c1 | c2
        if comp == 0b1000 or 0b1001 or 0b1010:
            difBit = 1
            
        if comp == 0b0100 or 0b0101 or 0b0110:
            difBit = 2
           
        if comp == 0b0010:
            difBit = 3
            
        if comp== 0b0001:
            difBit = 4

        #Determina o extremo que será usado para encontrar a interseção           
        if difBit==1:
            cord_parcial = xmin
        if difBit==2:
            cord_parcial = ymin
        if difBit==3:
            cord_parcial = xmax
        if difBit==4:
            cord_parcial = ymax
        ponto_I = intersecao(difBit,cord_parcial,xmin,xmax,ymin,ymax,x1, y1, x2, y2)

        #verifica se o código 1 é igual a 0
        if(GetBIT(c1,difBit)==0):
           recorta_linha(x1,y1,ponto_I[0],ponto_I[1],xmin,xmax,ymin,ymax)
        else:
            recorta_linha(ponto_I[0],ponto_I[1],x2,y2,xmin,xmax,ymin,ymax)

def sign(x,y,xmin,xmax,ymin,ymax):
    if (ymax - y)>=0:
        bit1 = str(0)
    else:
        bit1 = str(1)

    if (y - ymin) >=0:
        bit2 = bit1 + str(0)
    else:
        bit2 = bit1 + str(1)
    if (xmax - x)>=0:
        bit3 = bit2 + str(0)
    else:
        bit3 = bit2 + str(1)
    if (x- xmin)>=0:
        bit4 = bit3 + str(0)
    else:
        bit4 = bit3 + str(1)

    code = (bit4)

    if code == "1001":
        code = 0b1001 #9
    if code == "1000":
        code = 0b1000 # 8
    if code == "1010":
        code = 0b1010 # 10
    if code == "0001": 
        code = 0b0001 # 1
    if code =="0000":
        code = 0b0000 # 0
    if code == "0010":
        code = 0b0010 #2
    if code == "0101":
        code = 0b0101 # 5
    if code == "0100":
        code = 0b0100 # 4
    if code == "0110":
        code = 0b110 #6
    
    
    return (code)
   
        

def intersecao(difBit,cord_parcial,xmin,xmax,ymin,ymax,x1, y1, x2, y2):
    tupla = ()
    print(cord_parcial,xmin)
    if  difBit == 1:
        print("inserr 1")
        print(cord_parcial,xmin)
        yi = (((cord_parcial - x1) * (y2-y1) / (x2-x1)) + y1)
        tupla = (xmin,yi)
        return tupla
    if difBit == 3:
        print("inserr 2")
        yi = (((cord_parcial - x1) * (y2-y1) / (x2-x1)) + y1)
        tupla = (xmax,yi)
        return tupla
    if difBit == 2:
        print("inserr 3")
        xi = (((cord_parcial-y1) * (x2-x1) / (y2-y1)) + x1)
        tupla =(xi,ymin)
        return tupla
    if difBit == 4:
        print("inserr 4")
        xi = (((cord_parcial-y1) * (x2-x1) / (y2-y1)) + x1)
        tupla =(xi,ymax)
        return tupla

def GetBIT(c1,difBit):
    print("Código = ",c1,"BIT da diferença",difBit)

    #Se o código 1 for 0 para um determado bit de diferença, chama recorta_linha(x1,y1,ponto_I[0],ponto_I[1],xmin,xmax,ymin,ymax)
    # senão chama recorta_linha(ponto_I[0],ponto_I[1],x2,y2,xmin,xmax,ymin,ymax)
    # recorta_linha(ponto_I[0],ponto_I[1],x2,y2,xmin,xmax,ymin,ymax) é chamada primeiro
    # recorta_linha(x1,y1,ponto_I[0],ponto_I[1],xmin,xmax,ymin,ymax), é chamada por segundo e nesse momento nossa linha está toda dentro da aréa que será plotada
    if difBit==1 and c1 == 0b0000:
        print("OPOÇÃO 1")
        comp = 0
    elif difBit==2 and c1 == 0b0000:
        print("POÇÃO 3")
        comp = 0
    elif difBit==3 and c1 == 0b0000:
        print("POÇÃO 5")
        comp = 0
    elif difBit==4 and c1 == 0b0000:
        print("POÇÃO 7")
        comp = 0
    else:
        print("OPOÇÃO 8")
        comp = 1
    print("COMP = ",comp)
    return comp


def reflexao(x1, y1, x2, y2):
    x, y = x1, y1
    delta_x = abs(x2 - x1)
    delta_y = abs(y2 - y1)
    ponto_medio = delta_y/float(delta_x)
    result_x = []
    delta = ponto_medio - float(1/2)

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
    ponto_medio = delta_y/float(delta_x)

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


    while x < x2 and y1 > y2:
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
            #print('x = %s, y = %s' % (valores_x , valores_y))
            trocaxy = False    
        
    n = len(valores_x)

    result = []
    tupla = ()
    for i in range(n):
        tupla = (valores_x[i],valores_y[i])
        result.append(tupla)
    return result









def main():
    
    Mesagem_Inicial= Label(master, text= "Qual algoritmo deseja executar?")
    Mesagem_Inicial.grid(column = 10, row= 0)

      
if __name__ == "__main__":
    main()

CriarTemplate()


mainloop()
