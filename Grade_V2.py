from tkinter import *
from tkinter.ttk import *
from turtle import distance, left, right
from typing import final
from Polilinha import plot
import numpy as np
import Polilinha_FINAL
import Breserhan_V5
import Fill_Recursivo
import Circulo_v4
import Bezier_V4
import Elipse_v1
import Recorte_Polígono
import Transformations_2d
import Orto_Projections
import Perspective
import Transformations_3d
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
  edgecolor = '-r'
  color ='-b'
  Pintados = []

  if selecionado == "1 - Linha":
    x1 = int((e.get()))
    y1 = int((f.get()))
    x2 = int((g.get()))
    y2 = int((h.get()))
    

    result_x.extend(Breserhan_V5.reflexao(x1, y1, x2, y2))
    x,y = zip(*result_x)
    
    DesenharPixel(x,y, '#808080')

  if selecionado == "2 - Círculo":
    x_centro = int((e.get())) #usar 6
    y_centro = int((f.get())) #Usar 3
    raio = int((g.get())) #Usar 5

    x = 0
    y = raio
    erro_círculo = -raio
    result_x.extend(Circulo_v4.Circulo_Bres(x, y, x_centro, y_centro))

    while x <= y:
        erro_círculo += 2 * x + 1
        x += 1
        if erro_círculo >= 0:
            erro_círculo += 2 - 2*y
            y -= 1
            #break #EU odeio o argumento break
        result_x.extend(Circulo_v4.Circulo_Bres(x, y, x_centro, y_centro))
    #print("Print 2: ",result_x)
    Conjunto_X,Conjunto_Y = zip(*result_x)
    
    DesenharPixel(Conjunto_X,Conjunto_Y, '#808080')

  if selecionado == "3 - Elipse":
    x_centro = int((e.get())) #usar 0
    y_centro = int((f.get())) #usar 10
    raio_A = int((g.get())) #usar 5
    raio_B = int((h.get())) # Usar 10
    

    result_x.extend(Elipse_v1.Eplipse_Bres(raio_A, raio_B, x_centro, y_centro))
    x,y = zip(*result_x)
    
    DesenharPixel(x,y, '#808080')

  if selecionado == "4 - Curva":
    stringX = (e.get()) #usar[0,1,2,3]
    stringY = (f.get()) #Usar[0,5,2,15]
    meio = float((g.get())) #Usar 1.5

    ctrl_pts_x = stringX.split(',')
    ctrl_pts_y = stringY.split(',')

    ctrl_pts_x = list(map(int,ctrl_pts_x))
    ctrl_pts_y = list(map(int,ctrl_pts_y))

    n = len(ctrl_pts_x)-1
    result_x.extend(Bezier_V4.Bezierpoit(n,ctrl_pts_x,ctrl_pts_y,meio))
    Curva_X,Curva_Y = zip(*result_x)
    print("Reultado X:" ,Curva_X,"Reultado Y:",Curva_Y)
    DesenharPixel(Curva_X,Curva_Y, '#808080')


  if selecionado == "5 - Polilinha":
    stringX=(e.get()) #[-3,-1,6,3,-4] #TESTE 1 # [-5,4,8,5,0,-6]
    
    stringY=(f.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]

    X_Vet=stringX.split(',')
    Y_Vet=stringY.split(',')
    n = len(X_Vet)
    
    X_Vet = list(map(float,X_Vet))
    Y_Vet = list(map(float,Y_Vet))
    print(X_Vet)
    print(Y_Vet)
    
    for i in range (n):
      x1 = X_Vet[i]
      x2 = X_Vet[(i+1)%n]
      y1 = Y_Vet[i]
      y2 = Y_Vet[(i+1)%n]
      result_x.extend(Polilinha_FINAL.reflexao(x1, y1, x2, y2))
          
    x,y = zip(*result_x)
      
    DesenharPixel(x,y, '#808080')  

  if selecionado == "6 - Preenchimento Recursivo":
    stringX=(e.get())
    
    stringY=(f.get())
    X_Pintar = int((g.get())) #usar 0
    Y_Pintar = int((h.get())) #Usar 6

    X_Vet=stringX.split(',')
    Y_Vet=stringY.split(',')
    n = len(X_Vet)
    
    X_Vet = list(map(int,X_Vet))
    Y_Vet = list(map(int,Y_Vet))
    print(X_Vet)
    print(Y_Vet)
    
    for i in range (n):
      x1 = X_Vet[i]
      x2 = X_Vet[(i+1)%n]
      y1 = Y_Vet[i]
      y2 = Y_Vet[(i+1)%n]
      result_x.extend(Polilinha_FINAL.reflexao(x1, y1, x2, y2))
          
    x,y = zip(*result_x)
      
    DesenharPixel(x,y, '#808080')  

    Fill_Recursivo.FloodFill(X_Pintar,Y_Pintar,edgecolor,color,Pintados,result_x)
    w,z = zip(*Pintados)
    DesenharPixel(w,z, '#f00')

  
  if selecionado == "7 - Recorte Polígono":
    stringX=(e.get()) #[-3,-1,6,3,-4] #TESTE 1 # [-5,4,8,5,0,-6] # -3,12,12,7,12,12
    
    stringY=(f.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2] #  4,13,6,4,2,-4

    left=(float(g.get())) # -2 #TESTE 1 # 0
    
    right=(float(h.get())) # 5 #TESTE 1 # 10

    top=(float(j.get())) # 8 #TESTE 1 # 10
    
    bottom=(float(k.get())) # 0 #TESTE 1 # 0

    X_Vet=stringX.split(',')
    Y_Vet=stringY.split(',')
    n = len(X_Vet)
    
    X_Vet = list(map(float,X_Vet))
    Y_Vet = list(map(float,Y_Vet))
    result = []
    result_corte = []

    result.extend(Recorte_Polígono.recorta_poligono(left,top,right,bottom,X_Vet,Y_Vet))
    x,y = zip(*result)

    m = len(x)
    for i in range (m):
        x1 = x[i]
        x2 = x[(i+1)%m]
        y1 = y[i]
        y2 = y[(i+1)%m]
        result_corte.extend(Polilinha_FINAL.reflexao(x1, y1, x2, y2))
    
    w,z = zip(*result_corte)
      
    DesenharPixel(w,z, '#808080')  
  

  if selecionado == "8 - Rotacionar Polígono 2d":
    stringX=(e.get()) #[-3,-1,6,3,-4] #TESTE 1 # [-5,4,8,5,0,-6]
    
    stringY=(f.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]

    Angle = (int(g.get()))
    Rotation_Point = (int(h.get()))
    Rotation_Point = Rotation_Point - 1
    
    X_Vet=stringX.split(',')
    Y_Vet=stringY.split(',')
    
    X_Vet = list(map(float,X_Vet))
    Y_Vet = list(map(float,Y_Vet))

 
    Polygon = np.array([X_Vet,Y_Vet])

    Polygon = np.append(Polygon,[np.ones(len(Polygon[0]))],axis=0)


    Final_Result = Transformations_2d.rotation(Polygon, Angle, Rotation_Point)
    Final_Result = np.delete(Final_Result,(2), axis=0)
    
    print(Final_Result)
    

    
    Final = plot(Final_Result)
    print("FInal",Final)
    
    

    DesenharPixel(Final[0],Final[1], '#f00')
    

  if selecionado == "9 - Transladar Polígono 2d":
    stringX=(e.get()) #[-3,-1,6,3,-4] #TESTE 1 # [-5,4,8,5,0,-6]
    
    stringY=(f.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]

    stringTranslationCoordinates=(g.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]

    X_Vet=stringX.split(',')
    Y_Vet=stringY.split(',')
    Translation_Coordinates = stringTranslationCoordinates.split(',')
    
      
    X_Vet = list(map(float,X_Vet))
    Y_Vet = list(map(float,Y_Vet))
    Translation_Coordinates = list(map(int,Translation_Coordinates))

    Polygon = np.array([X_Vet,Y_Vet])

    Polygon = np.append(Polygon,[np.ones(len(Polygon[0]))],axis=0)


    Final_Result = Transformations_2d.translation(Polygon,Translation_Coordinates)
    Final_Result = np.delete(Final_Result,(2), axis=0)
    
    print(Final_Result)
    

    
    Final = plot(Final_Result)
    print("FInal",Final)
    
    

    DesenharPixel(Final[0],Final[1], '#f00')

  if selecionado == "10 - Escalar Polígono 2d":
    stringX=(e.get()) #[-3,-1,6,3,-4] #TESTE 1 # [-5,4,8,5,0,-6]
    
    stringY=(f.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]

    stringScalingFactors=(g.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]
    
    Fixed_Point = (int(h.get()))
    
    Fixed_Point = Fixed_Point - 1

    X_Vet=stringX.split(',')
    Y_Vet=stringY.split(',')
    Scaling_Factors = stringScalingFactors.split(',')
    
    
    X_Vet = list(map(float,X_Vet))
    Y_Vet = list(map(float,Y_Vet))
    Scaling_Factors = list(map(int,Scaling_Factors))

    Polygon = np.array([X_Vet,Y_Vet])

    Polygon = np.append(Polygon,[np.ones(len(Polygon[0]))],axis=0)


    Final_Result = Transformations_2d.scaling(Polygon,Scaling_Factors,Fixed_Point)
    Final_Result = np.delete(Final_Result,(2), axis=0)
    
    print(Final_Result)
    

    
    Final = plot(Final_Result)
    print("FInal",Final)
    
    

    DesenharPixel(Final[0],Final[1], '#f00')

  if selecionado == "11 - Projeção Ortogonal - Frontal":
    stringX=(e.get()) #[-3,-1,6,3,-4] #TESTE 1 # [-5,4,8,5,0,-6]
    
    stringY=(f.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]

    stringZ=(g.get()) 

    X_Vet=stringX.split(',')
    Y_Vet=stringY.split(',')
    Z_Vet=stringY.split(',')
    
    
    X_Vet = list(map(float,X_Vet))
    Y_Vet = list(map(float,Y_Vet))
    Z_Vet = list(map(float,Z_Vet))

    Polygon = np.array([X_Vet,Y_Vet,Z_Vet])

    Polygon = np.append(Polygon,[np.ones(len(Polygon[0]))],axis=0)


    Final_Result = Orto_Projections.orto_front(Polygon)
    
    print(Final_Result)
    

    
    Final = plot(Final_Result)
    print("FInal",Final)
    
    

    DesenharPixel(Final[0],Final[1], '#f00')

  if selecionado == "12 - Projeção Ortogonal - Lateral":
    stringX=(e.get()) #[-3,-1,6,3,-4] #TESTE 1 # [-5,4,8,5,0,-6]
    
    stringY=(f.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]

    stringZ=(g.get()) 

    X_Vet=stringX.split(',')
    Y_Vet=stringY.split(',')
    Z_Vet=stringZ.split(',')
    
    n = len(X_Vet)
    
    X_Vet = list(map(float,X_Vet))
    Y_Vet = list(map(float,Y_Vet))
    Z_Vet = list(map(float,Z_Vet))

    Polygon = np.array([X_Vet,Y_Vet,Z_Vet])
    
    Polygon = np.append(Polygon,[np.ones(len(Polygon[0]))],axis=0)


    Final_Result = Orto_Projections.orto_side(Polygon)
    
    print(Final_Result)
    

    Final = plot(Final_Result)
    print("FInal",Final)
    
    

    DesenharPixel(Final[0],Final[1], '#f00')

  if selecionado == "13 - Projeção Ortogonal - Superior":
    stringX=(e.get()) #[-3,-1,6,3,-4] #TESTE 1 # [-5,4,8,5,0,-6]
    
    stringY=(f.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]

    stringZ=(g.get())

    X_Vet=stringX.split(',')
    Y_Vet=stringY.split(',')
    Z_Vet=stringZ.split(',')
    
    
    X_Vet = list(map(float,X_Vet))
    Y_Vet = list(map(float,Y_Vet))
    Z_Vet = list(map(float,Z_Vet))

    Polygon = np.array([X_Vet,Y_Vet,Z_Vet])

    Polygon = np.append(Polygon,[np.ones(len(Polygon[0]))],axis=0)


    Final_Result = Orto_Projections.orto_top(Polygon)
    
    print(Final_Result)
    

    
    Final = plot(Final_Result)
    print("FInal",Final)
    
    

    DesenharPixel(Final[0],Final[1], '#f00')

  if selecionado == "14 - Perspectiva - 1 ponto":
    stringX=(e.get()) #[-3,-1,6,3,-4] #TESTE 1 # [-5,4,8,5,0,-6]
    
    stringY=(f.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]

    stringZ=(g.get())
    
    Distance = (int(h.get()))
    
    Focal_Point = (int(j.get()))
    
    Focal_Point = Focal_Point - 1

    X_Vet=stringX.split(',')
    Y_Vet=stringY.split(',')
    Z_Vet=stringZ.split(',')
    
    
    X_Vet = list(map(float,X_Vet))
    Y_Vet = list(map(float,Y_Vet))
    Z_Vet = list(map(float,Z_Vet))

    Polygon = np.array([X_Vet,Y_Vet,Z_Vet])

    Polygon = np.append(Polygon,[np.ones(len(Polygon[0]))],axis=0)


    Final_Result = Perspective.one_point_perspective(Polygon,Distance,Focal_Point)
    
    print(Final_Result)
    

    
    Final = plot(Final_Result)
    print("FInal",Final)
    
    

    DesenharPixel(Final[0],Final[1], '#f00')

  if selecionado == "15 - Perspectiva - 2 pontos":
    stringX=(e.get()) #[-3,-1,6,3,-4] #TESTE 1 # [-5,4,8,5,0,-6]
    
    stringY=(f.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]

    stringZ=(g.get())
    
    Distance = (int(h.get()))
    
    Focal_Point = (int(j.get()))
    
    Focal_Point = Focal_Point - 1

    X_Vet=stringX.split(',')
    Y_Vet=stringY.split(',')
    Z_Vet=stringZ.split(',')
    
    
    X_Vet = list(map(float,X_Vet))
    Y_Vet = list(map(float,Y_Vet))
    Z_Vet = list(map(float,Z_Vet))

    Polygon = np.array([X_Vet,Y_Vet,Z_Vet])

    Polygon = np.append(Polygon,[np.ones(len(Polygon[0]))],axis=0)


    Final_Result = Perspective.two_point_perspective(Polygon,Distance,Focal_Point)
    
    print(Final_Result)
    

    
    Final = plot(Final_Result)
    print("FInal",Final)
    
    DesenharPixel(Final[0],Final[1], '#f00')

  if selecionado == "16 - Perspectiva - 3 pontos":
    stringX=(e.get()) #[-3,-1,6,3,-4] #TESTE 1 # [-5,4,8,5,0,-6]
    
    stringY=(f.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]

    stringZ=(g.get())
    
    Distance = (int(h.get()))
    
    Focal_Point = (int(j.get()))
    
    Focal_Point = Focal_Point - 1

    X_Vet=stringX.split(',')
    Y_Vet=stringY.split(',')
    Z_Vet=stringZ.split(',')
    
    
    X_Vet = list(map(float,X_Vet))
    Y_Vet = list(map(float,Y_Vet))
    Z_Vet = list(map(float,Z_Vet))

    Polygon = np.array([X_Vet,Y_Vet,Z_Vet])

    Polygon = np.append(Polygon,[np.ones(len(Polygon[0]))],axis=0)


    Final_Result = Perspective.three_point_perspective(Polygon,Distance,Focal_Point)
    
    print(Final_Result)
    

    
    Final = plot(Final_Result)
    print("FInal",Final)
    

    DesenharPixel(Final[0],Final[1], '#f00')

  if selecionado == "17 - Transladar Polígono 3d":
    stringX=(e.get()) #[-3,-1,6,3,-4] #TESTE 1 # [-5,4,8,5,0,-6]
    
    stringY=(f.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]
    
    stringZ=(g.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]

    stringTranslationCoordinates=(h.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]
    
    X_Vet=stringX.split(',')
    Y_Vet=stringY.split(',')
    Z_Vet=stringZ.split(',')
    Translation_Coordinates = stringTranslationCoordinates.split(',')
    

    
    X_Vet = list(map(float,X_Vet))
    Y_Vet = list(map(float,Y_Vet))
    Z_Vet = list(map(float,Z_Vet))
    Translation_Coordinates = list(map(int,Translation_Coordinates))

    Polygon = np.array([X_Vet,Y_Vet,Z_Vet])

    Polygon = np.append(Polygon,[np.ones(len(Polygon[0]))],axis=0)


    Final_Result = Transformations_3d.translation(Polygon,Translation_Coordinates)
    Final_Result = np.delete(Final_Result,(3), axis=0)
    
    print(Final_Result)
    

    
    Final = plot(Final_Result)
    print("FInal",Final)
    
    

    DesenharPixel(Final[0],Final[1], '#f00')

  if selecionado == "18 - Escalar Polígono 3d":
    stringX=(e.get()) #[-3,-1,6,3,-4] #TESTE 1 # [-5,4,8,5,0,-6]
    
    stringY=(f.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]
    
    stringZ=(f.get())

    stringScalingFactors=(h.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]
    
    Fixed_Point = (int(j.get()))
    
    Fixed_Point = Fixed_Point - 1

    X_Vet=stringX.split(',')
    Y_Vet=stringY.split(',')
    Z_Vet=stringY.split(',')
    Scaling_Factors = stringScalingFactors.split(',')
    
    
    X_Vet = list(map(float,X_Vet))
    Y_Vet = list(map(float,Y_Vet))
    Z_Vet = list(map(float,Z_Vet))
    Scaling_Factors = list(map(int,Scaling_Factors))

    Polygon = np.array([X_Vet,Y_Vet,Z_Vet])

    Polygon = np.append(Polygon,[np.ones(len(Polygon[0]))],axis=0)


    Final_Result = Transformations_3d.scaling(Polygon,Scaling_Factors,Fixed_Point)
    Final_Result = np.delete(Final_Result,(3), axis=0)
    
    print(Final_Result)
    

    
    Final = plot(Final_Result)
    print("FInal",Final)
    
    

    DesenharPixel(Final[0],Final[1], '#f00')

  if selecionado == "19 - Rotacionar Polígono 3d":
    stringX=(e.get()) #[-3,-1,6,3,-4] #TESTE 1 # [-5,4,8,5,0,-6]
    
    stringY=(f.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]

    Angle = (int(g.get()))
    Rotation_Point = (int(h.get()))
    Rotation_Point = Rotation_Point - 1
    
    X_Vet=stringX.split(',')
    Y_Vet=stringY.split(',')
    
    X_Vet = list(map(float,X_Vet))
    Y_Vet = list(map(float,Y_Vet))

 
    Polygon = np.array([X_Vet,Y_Vet])

    Polygon = np.append(Polygon,[np.ones(len(Polygon[0]))],axis=0)


    Final_Result = Transformations_2d.rotation(Polygon, Angle, Rotation_Point)
    Final_Result = np.delete(Final_Result,(2), axis=0)
    
    print(Final_Result)
    

    
    Final = plot(Final_Result)
    print("FInal",Final)
    
    

    DesenharPixel(Final[0],Final[1], '#f00')

  if selecionado == "19 - Rotacionar X Polígono 3d":
    stringX=(e.get()) #[-3,-1,6,3,-4] #TESTE 1 # [-5,4,8,5,0,-6]
    
    stringY=(f.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]
    
    stringZ=(g.get())

    Angle = (int(h.get()))
    Rotation_Point = (int(j.get()))
    Rotation_Point = Rotation_Point - 1
    
    X_Vet=stringX.split(',')
    Y_Vet=stringY.split(',')
    Z_Vet=stringZ.split(',')
    
    X_Vet = list(map(float,X_Vet))
    Y_Vet = list(map(float,Y_Vet))
    Z_Vet = list(map(float,Z_Vet))

 
    Polygon = np.array([X_Vet,Y_Vet,Z_Vet])

    Polygon = np.append(Polygon,[np.ones(len(Polygon[0]))],axis=0)


    Final_Result = Transformations_3d.rotation_x(Polygon, Angle, Rotation_Point)
    Final_Result = np.delete(Final_Result,(3), axis=0)
    
    print(Final_Result)
    

    
    Final = plot(Final_Result)
    print("FInal",Final)
    
    

    DesenharPixel(Final[0],Final[1], '#f00')

  if selecionado == "20 - Rotacionar Y Polígono 3d":
    stringX=(e.get()) #[-3,-1,6,3,-4] #TESTE 1 # [-5,4,8,5,0,-6]
    
    stringY=(f.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]
    
    stringZ=(g.get())

    Angle = (int(h.get()))
    Rotation_Point = (int(j.get()))
    Rotation_Point = Rotation_Point - 1
    
    X_Vet=stringX.split(',')
    Y_Vet=stringY.split(',')
    Z_Vet=stringZ.split(',')
    
    X_Vet = list(map(float,X_Vet))
    Y_Vet = list(map(float,Y_Vet))
    Z_Vet = list(map(float,Z_Vet))

 
    Polygon = np.array([X_Vet,Y_Vet,Z_Vet])

    Polygon = np.append(Polygon,[np.ones(len(Polygon[0]))],axis=0)


    Final_Result = Transformations_3d.rotation_y(Polygon, Angle, Rotation_Point)
    Final_Result = np.delete(Final_Result,(3), axis=0)
    
    print(Final_Result)
    

    
    Final = plot(Final_Result)
    print("FInal",Final)
    
    

    DesenharPixel(Final[0],Final[1], '#f00')

  if selecionado == "21 - Rotacionar Z Polígono 3d":
    stringX=(e.get()) #[-3,-1,6,3,-4] #TESTE 1 # [-5,4,8,5,0,-6]
    
    stringY=(f.get()) #[-2,4,1,10,9] #TESTE 1 # [-7,-5,0,5,8,2]
    
    stringZ=(g.get())

    Angle = (int(h.get()))
    Rotation_Point = (int(j.get()))
    Rotation_Point = Rotation_Point - 1
    
    X_Vet=stringX.split(',')
    Y_Vet=stringY.split(',')
    Z_Vet=stringZ.split(',')
    
    X_Vet = list(map(float,X_Vet))
    Y_Vet = list(map(float,Y_Vet))
    Z_Vet = list(map(float,Z_Vet))

 
    Polygon = np.array([X_Vet,Y_Vet,Z_Vet])

    Polygon = np.append(Polygon,[np.ones(len(Polygon[0]))],axis=0)


    Final_Result = Transformations_3d.rotation_z(Polygon, Angle, Rotation_Point)
    Final_Result = np.delete(Final_Result,(3), axis=0)
    
    print(Final_Result)
    

    
    Final = plot(Final_Result)
    print("FInal",Final)
    
    

    DesenharPixel(Final[0],Final[1], '#f00')
    
def InsereValor(event):
 
  selecionado = combo.get()

  if selecionado == "1 - Linha":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)  
    h.grid(column = 15, row = 4)

    Mesagem_Inicial_x1= Label(master, text= "Qual o valor inicial de x? ")
    Mesagem_Inicial_x1.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_y1= Label(master, text= "Qual o valor inicial de y? ")
    Mesagem_Inicial_y1.grid(column = 10, row= 2, pady= 10)  
    Mesagem_Inicial_x2= Label(master, text= "Qual o valor final de x? ")
    Mesagem_Inicial_x2.grid(column = 10, row= 3, pady= 10)  
    Mesagem_Inicial_y2= Label(master, text= "Qual o valor final de y?")
    Mesagem_Inicial_y2.grid(column = 10, row= 4, pady= 10)  
    botao = Button(master,text="Desenhar Linha",command=funcao_selecionada)        
    botao.grid(column = 15, row = 5, pady= 10) 

  if selecionado == "2 - Círculo":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3) 

    Mesagem_Inicial_x1= Label(master, text= "Qual o valor do ponto X ao centro? ")
    Mesagem_Inicial_x1.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_y1= Label(master, text= "Qual o valor do ponto Y ao centro? ")
    Mesagem_Inicial_y1.grid(column = 10, row= 2, pady= 10)  
    Mesagem_Inicial_x2= Label(master, text= "Qual o valor do raio? ")
    Mesagem_Inicial_x2.grid(column = 10, row= 3, pady= 10)
    botao = Button(master,text="Desenhar Círculo",command=funcao_selecionada)        
    botao.grid(column = 15, row = 4, pady= 10) 

  if selecionado == "3 - Elipse":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)  
    h.grid(column = 15, row = 4)

    Mesagem_Inicial_x1= Label(master, text= "Qual o valor do ponto X ao centro? ")
    Mesagem_Inicial_x1.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_y1= Label(master, text= "Qual o valor do ponto Y ao centro? ")
    Mesagem_Inicial_y1.grid(column = 10, row= 2, pady= 10)  
    Mesagem_Inicial_x2= Label(master, text= "Qual o valor do raio A? ")
    Mesagem_Inicial_x2.grid(column = 10, row= 3, pady= 10)  
    Mesagem_Inicial_y2= Label(master, text= "Qual o valor do raio B? ")
    Mesagem_Inicial_y2.grid(column = 10, row= 4, pady= 10)  
    botao = Button(master,text="Desenhar Elipse",command=funcao_selecionada)        
    botao.grid(column = 15, row = 5, pady= 10) 

  if selecionado == "4 - Curva":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3) 

    Mesagem_Inicial_x1= Label(master, text= "Insira as coordenadas X dos pontos de controle, separado-as com vírgula: ")
    Mesagem_Inicial_x1.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_y1= Label(master, text= "Insira as coordenadas Y dos pontos de controle, separado-as com vírgula: ")
    Mesagem_Inicial_y1.grid(column = 10, row= 2, pady= 10)  
    Mesagem_Inicial_x2= Label(master, text= "Insrira o valor do meio: ")
    Mesagem_Inicial_x2.grid(column = 10, row= 3, pady= 10)
    botao = Button(master,text="Desenhar Curva",command=funcao_selecionada)        
    botao.grid(column = 15, row = 4, pady= 10) 
  
  if selecionado == "5 - Polilinha":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)

    Mesagem_Inicial_X= Label(master, text= "Insira os pontos do conjunto X que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_X.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Y que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 2, pady= 10)  
    botao = Button(master,text="Desenhar Polígono",command=funcao_selecionada)        
    botao.grid(column = 15, row = 3, pady= 10)

  if selecionado == "6 - Preenchimento Recursivo":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)
    h.grid(column = 15, row = 4)

    Mesagem_Inicial_X= Label(master, text= "Insira os pontos do conjunto X que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_X.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Y que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 2, pady= 10)
    Mesagem_Inicial_PontoX= Label(master, text= "Insira a coordenada X de um ponto dentro do polígono: ")
    Mesagem_Inicial_PontoX.grid(column = 10, row= 3, pady= 10) 
    Mesagem_Inicial_PontoY= Label(master, text= "Insira a coordenada Y de um ponto dentro do polígono: ")
    Mesagem_Inicial_PontoY.grid(column = 10, row= 4, pady= 10)   
    botao = Button(master,text="Desenhar e Preencher Polígono",command=funcao_selecionada)        
    botao.grid(column = 15, row = 5, pady= 10)  


  if selecionado == "7 - Recorte Polígono":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)
    h.grid(column = 15, row = 4)
    j.grid(column = 15, row = 5)
    k.grid(column = 15, row = 6)

    Mesagem_Inicial_X= Label(master, text= "Insira os pontos do conjunto X que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_X.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Y que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 2, pady= 10)
    Mesagem_Inicial_PontoX= Label(master, text= "Insira a coordenada X (Left) da área de recorte: ")
    Mesagem_Inicial_PontoX.grid(column = 10, row= 3, pady= 10) 
    Mesagem_Inicial_PontoY= Label(master, text= "Insira a coordenada X (Right) da área de recorte: ")
    Mesagem_Inicial_PontoY.grid(column = 10, row= 4, pady= 10)   
    Mesagem_Inicial_PontoY= Label(master, text= "Insira a coordenada Y (Top) da área de recorte: ")
    Mesagem_Inicial_PontoY.grid(column = 10, row= 5, pady= 10)
    Mesagem_Inicial_PontoY= Label(master, text= "Insira a coordenada Y (Bottom) da área de recorte: ")
    Mesagem_Inicial_PontoY.grid(column = 10, row= 6, pady= 10)      
    botao = Button(master,text="Recortar Polígono",command=funcao_selecionada)        
    botao.grid(column = 15, row = 7, pady= 10)

  if selecionado == "8 - Rotacionar Polígono 2d":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)
    h.grid(column = 15, row = 4)

    Mesagem_Inicial_X= Label(master, text= "Insira os pontos do conjunto X que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_X.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Y que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 2, pady= 10)
    Mesagem_Inicial_PontoX= Label(master, text= "Informe o ângulo de rotação do polígono: ")
    Mesagem_Inicial_PontoX.grid(column = 10, row= 3, pady= 10) 
    Mesagem_Inicial_PontoY= Label(master, text= "Informe o ponto de rotação do polígono: ")
    Mesagem_Inicial_PontoY.grid(column = 10, row= 4, pady= 10)   
    botao = Button(master,text="Rotacionar Poligono",command=funcao_selecionada)        
    botao.grid(column = 15, row = 5, pady= 10)    

  if selecionado == "9 - Transladar Polígono 2d":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)   

    Mesagem_Inicial_X= Label(master, text= "Insira os pontos do conjunto X que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_X.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Y que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 2, pady= 10)
    Mesagem_Inicial_PontoX= Label(master, text= "Informe as coordenadas de translação: ")
    Mesagem_Inicial_PontoX.grid(column = 10, row= 3, pady= 10)  
    botao = Button(master,text="Transladar Polígono 2d",command=funcao_selecionada)        
    botao.grid(column = 15, row = 4, pady= 10)
    
  if selecionado == "10 - Escalar Polígono 2d":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)   
    h.grid(column = 15, row = 4)

    Mesagem_Inicial_X= Label(master, text= "Insira os pontos do conjunto X que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_X.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Y que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 2, pady= 10)
    Mesagem_Inicial_PontoX= Label(master, text= "Informe os fatores de escalada: ")
    Mesagem_Inicial_PontoX.grid(column = 10, row= 3, pady= 10) 
    Mesagem_Inicial_PontoX= Label(master, text= "Informe o ponto de fixação: ")
    Mesagem_Inicial_PontoX.grid(column = 10, row= 4, pady= 10)  
    botao = Button(master,text="Escalar Polígono 2d",command=funcao_selecionada)        
    botao.grid(column = 15, row = 5, pady= 10)
    
  if selecionado == "11 - Projeção Ortogonal - Frontal":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)   

    Mesagem_Inicial_X= Label(master, text= "Insira os pontos do conjunto X que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_X.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Y que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 2, pady= 10)
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Z que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 3, pady= 10)  
    botao = Button(master,text="Projeção Ortogonal - Frontal",command=funcao_selecionada)        
    botao.grid(column = 15, row = 4, pady= 10)

  if selecionado == "11 - Projeção Ortogonal - Frontal":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)

    Mesagem_Inicial_X= Label(master, text= "Insira os pontos do conjunto X que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_X.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Y que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 2, pady= 10)
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Z que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 3, pady= 10)  
    botao = Button(master,text="Projeção Ortogonal - Frontal",command=funcao_selecionada)        
    botao.grid(column = 15, row = 4, pady= 10)

  if selecionado == "12 - Projeção Ortogonal - Lateral":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)

    Mesagem_Inicial_X= Label(master, text= "Insira os pontos do conjunto X que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_X.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Y que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 2, pady= 10)
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Z que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 3, pady= 10)  
    botao = Button(master,text="Projeção Ortogonal - Lateral",command=funcao_selecionada)        
    botao.grid(column = 15, row = 4, pady= 10)

  if selecionado == "13 - Projeção Ortogonal - Superior":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)

    Mesagem_Inicial_X= Label(master, text= "Insira os pontos do conjunto X que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_X.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Y que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 2, pady= 10)
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Z que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 3, pady= 10)  
    botao = Button(master,text="Projeção Ortogonal - Superior",command=funcao_selecionada)        
    botao.grid(column = 15, row = 4, pady= 10)
    
  if selecionado == "14 - Perspectiva - 1 ponto":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)
    h.grid(column = 15, row = 4)
    j.grid(column = 15, row = 5)

    Mesagem_Inicial_X= Label(master, text= "Insira os pontos do conjunto X que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_X.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Y que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 2, pady= 10)
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Z que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 3, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira o ponto d: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 4, pady= 10)
    Mesagem_Inicial_Y= Label(master, text= "Insira o ponto de foco: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 5, pady= 10)
    botao = Button(master,text="Perspectiva - 1 ponto",command=funcao_selecionada)        
    botao.grid(column = 15, row = 6, pady= 10)

  if selecionado == "15 - Perspectiva - 2 pontos":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)
    h.grid(column = 15, row = 4)
    j.grid(column = 15, row = 5)

    Mesagem_Inicial_X= Label(master, text= "Insira os pontos do conjunto X que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_X.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Y que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 2, pady= 10)
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Z que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 3, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira o ponto d: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 4, pady= 10)
    Mesagem_Inicial_Y= Label(master, text= "Insira o ponto de foco: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 5, pady= 10)
    botao = Button(master,text="Perspectiva - 2 pontos",command=funcao_selecionada)        
    botao.grid(column = 15, row = 6, pady= 10)

  if selecionado == "16 - Perspectiva - 3 pontos":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)
    h.grid(column = 15, row = 4)
    j.grid(column = 15, row = 5)

    Mesagem_Inicial_X= Label(master, text= "Insira os pontos do conjunto X que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_X.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Y que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 2, pady= 10)
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Z que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 3, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira o ponto d: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 4, pady= 10)
    Mesagem_Inicial_Y= Label(master, text= "Insira o ponto de foco: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 5, pady= 10)
    botao = Button(master,text="Perspectiva - 3 pontos",command=funcao_selecionada)        
    botao.grid(column = 15, row = 6, pady= 10)

  if selecionado == "17 - Transladar Polígono 3d":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)
    h.grid(column = 15, row = 4)

    Mesagem_Inicial_X= Label(master, text= "Insira os pontos do conjunto X que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_X.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Y que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 2, pady= 10)
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Z que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 3, pady= 10)  
    Mesagem_Inicial_PontoX= Label(master, text= "Informe as coordenadas de translação: ")
    Mesagem_Inicial_PontoX.grid(column = 10, row= 4, pady= 10)  
    botao = Button(master,text="Transladar Polígono 3d",command=funcao_selecionada)        
    botao.grid(column = 15, row = 6, pady= 10)

  if selecionado == "18 - Escalar Polígono 3d":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)   
    h.grid(column = 15, row = 4)
    j.grid(column = 15, row = 5)

    Mesagem_Inicial_X= Label(master, text= "Insira os pontos do conjunto X que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_X.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Y que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 2, pady= 10)
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Z que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 3, pady= 10)
    Mesagem_Inicial_PontoX= Label(master, text= "Informe os fatores de escalada: ")
    Mesagem_Inicial_PontoX.grid(column = 10, row= 4, pady= 10) 
    Mesagem_Inicial_PontoX= Label(master, text= "Informe o ponto de fixação: ")
    Mesagem_Inicial_PontoX.grid(column = 10, row= 5, pady= 10)  
    botao = Button(master,text="Escalar Polígono 3d",command=funcao_selecionada)        
    botao.grid(column = 15, row = 6, pady= 10)
    
  if selecionado == "19 - Rotacionar X Polígono 3d":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)
    h.grid(column = 15, row = 4)
    j.grid(column = 15, row = 5)

    Mesagem_Inicial_X= Label(master, text= "Insira os pontos do conjunto X que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_X.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Y que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 2, pady= 10)
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Z que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 3, pady= 10)
    Mesagem_Inicial_PontoX= Label(master, text= "Informe o ângulo de rotação do polígono: ")
    Mesagem_Inicial_PontoX.grid(column = 10, row= 4, pady= 10) 
    Mesagem_Inicial_PontoY= Label(master, text= "Informe o ponto de rotação do polígono: ")
    Mesagem_Inicial_PontoY.grid(column = 10, row= 5, pady= 10)   
    botao = Button(master,text="Rotacionar X Polígono 3d",command=funcao_selecionada)        
    botao.grid(column = 15, row = 6, pady= 10) 
  
  if selecionado == "20 - Rotacionar Y Polígono 3d":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)
    h.grid(column = 15, row = 4)
    j.grid(column = 15, row = 5)

    Mesagem_Inicial_X= Label(master, text= "Insira os pontos do conjunto X que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_X.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Y que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 2, pady= 10)
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Z que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 3, pady= 10)
    Mesagem_Inicial_PontoX= Label(master, text= "Informe o ângulo de rotação do polígono: ")
    Mesagem_Inicial_PontoX.grid(column = 10, row= 4, pady= 10) 
    Mesagem_Inicial_PontoY= Label(master, text= "Informe o ponto de rotação do polígono: ")
    Mesagem_Inicial_PontoY.grid(column = 10, row= 5, pady= 10)   
    botao = Button(master,text="Rotacionar Y Polígono 3d",command=funcao_selecionada)        
    botao.grid(column = 15, row = 6, pady= 10)

  if selecionado == "21 - Rotacionar Z Polígono 3d":
    e.grid(column = 15, row = 1)  
    f.grid(column = 15, row = 2)
    g.grid(column = 15, row = 3)
    h.grid(column = 15, row = 4)
    j.grid(column = 15, row = 5)

    Mesagem_Inicial_X= Label(master, text= "Insira os pontos do conjunto X que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_X.grid(column = 10, row= 1, pady= 10)  
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Y que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 2, pady= 10)
    Mesagem_Inicial_Y= Label(master, text= "Insira os pontos do conjunto Z que formam o polígono separado-os com vírgula: ")
    Mesagem_Inicial_Y.grid(column = 10, row= 3, pady= 10)
    Mesagem_Inicial_PontoX= Label(master, text= "Informe o ângulo de rotação do polígono: ")
    Mesagem_Inicial_PontoX.grid(column = 10, row= 4, pady= 10) 
    Mesagem_Inicial_PontoY= Label(master, text= "Informe o ponto de rotação do polígono: ")
    Mesagem_Inicial_PontoY.grid(column = 10, row= 5, pady= 10)   
    botao = Button(master,text="Rotacionar Z Polígono 3d",command=funcao_selecionada)        
    botao.grid(column = 15, row = 6, pady= 10)



    
combo = Combobox(master)
combo ['values'] = ("Selecionar" , "1 - Linha" , "2 - Círculo", "3 - Elipse","4 - Curva" , "5 - Polilinha" , "6 - Preenchimento Recursivo","7 - Recorte Polígono", "8 - Rotacionar Polígono 2d" , "9 - Transladar Polígono 2d", '10 - Escalar Polígono 2d',
                    '11 - Projeção Ortogonal - Frontal', "12 - Projeção Ortogonal - Lateral", '13 - Projeção Ortogonal - Superior',"14 - Perspectiva - 1 ponto", '15 - Perspectiva - 2 pontos', '16 - Perspectiva - 3 pontos', '17 - Transladar Polígono 3d',
                    '18 - Escalar Polígono 3d', '19 - Rotacionar X Polígono 3d', "20 - Rotacionar Y Polígono 3d", "21 - Rotacionar Z Polígono 3d")
combo.current(0)
combo.grid(column = 15, row = 0)
combo.bind("<<ComboboxSelected>>", InsereValor)
e = Entry(master)
f = Entry(master)
g = Entry(master)
h = Entry(master)
j = Entry(master)
k = Entry(master)

def main():
    
    Mesagem_Inicial= Label(master, text= "Qual algoritmo deseja executar?")
    Mesagem_Inicial.grid(column = 10, row= 0) 

      
if __name__ == "__main__":
    main()

CriarTemplate()


mainloop()
