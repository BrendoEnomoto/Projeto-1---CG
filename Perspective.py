from Orto_Projections import orto_front
import numpy as np
from Polilinha import plot

def translation(Polygon, Translation_Coordinates):
    polygon = Polygon
    translation_coordinates = Translation_Coordinates
    translation_matrix = np.array([[1,0,0,translation_coordinates[0]],
                                   [0,1,0,translation_coordinates[1]],
                                   [0,0,1,0],
                                   [0,0,0,1]])
    result = np.dot(translation_matrix, polygon)
    return result

def one_point_perspective(Polygon, Distance, Focal_Point):
    polygon = Polygon
    distance = Distance
    
    translation_coordinates = [polygon[0][Focal_Point]*-1,
                               polygon[1][Focal_Point]*-1]
    
    
    polygon = translation(polygon, translation_coordinates)
    
    perspective_matrix = np.array([[distance,0,0,0],
                                   [0,distance,0,0],
                                   [0,0,distance,0],
                                   [0,0,1,0]])
       
    result = np.dot(perspective_matrix, polygon)
    
    
    
    result = result / result[3]
    
    result =  orto_front(result)
    
    return result

def two_point_perspective(Polygon, Distance, Focal_Point):
    polygon = Polygon
    distance = Distance
    
    translation_coordinates = [polygon[0][Focal_Point]*-1,
                               polygon[1][Focal_Point]*-1]
    
    
    polygon = translation(polygon, translation_coordinates)
    
    perspective_matrix = np.array([[1,0,0,0],
                                   [0,1,0,0],
                                   [0,0,1,0],
                                   [1/distance,0,1/distance,0]])
    result = np.dot(perspective_matrix, polygon)
    
    result = result / result[3]
    
    result =  orto_front(result)
    
    return result

def three_point_perspective(Polygon, Distance, Focal_Point):
    polygon = Polygon
    distance = Distance
    
    translation_coordinates = [polygon[0][Focal_Point]*-1,
                               polygon[1][Focal_Point]*-1]
    
    
    polygon = translation(polygon, translation_coordinates)
    
    perspective_matrix = np.array([[1,0,0,0],
                                   [0,1,0,0],
                                   [0,0,1,0],
                                   [1/Distance,1/distance,1/distance,0]])
    result = np.dot(perspective_matrix, polygon)
    
    result = result / result[3]
    
    result =  orto_front(result)
    
    return result

def main():
    
    Polygon = np.array([[0,10,10,0,0,10,10,0], 
                        [0,0,10,10,0,0,10,10],
                        [-100,-100,-100,-100,-110,-110,-110,-110]])
       
    Polygon = np.append(Polygon,[np.ones(len(Polygon[0]))],axis=0)
    
    Distance = -100
    
    Focal_Point = 0
    
    Final_Result = one_point_perspective(Polygon, Distance, Focal_Point)
    
        
    print(Final_Result)
    plot(Final_Result)

if __name__ == "__main__":
    main()
