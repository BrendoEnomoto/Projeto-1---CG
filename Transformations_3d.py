import numpy as np
from Polilinha import plot

def translation(Polygon, Translation_Coordinates):
    polygon = Polygon
    translation_coordinates = Translation_Coordinates
    translation_matrix = np.array([[1,0,0,translation_coordinates[0]],
                                   [0,1,0,translation_coordinates[1]],
                                   [0,0,1,translation_coordinates[2]],
                                   [0,0,0,1]])
    result = np.dot(translation_matrix, polygon)
    
    return result

def scaling(Polygon, Scaling_Factors, Fixed_Point):
    polygon = Polygon
    scaling_factors = Scaling_Factors
    translation_coordinates = [polygon[0][Fixed_Point]*-1,
                               polygon[1][Fixed_Point]*-1,
                               polygon[2][Fixed_Point]*-1]
    
    inverted_translation_coordinates = [polygon[0][Fixed_Point],
                                    polygon[1][Fixed_Point],
                                    polygon[2][Fixed_Point]]
    
    polygon = translation(polygon, translation_coordinates)
    
  
    scaling_matrix = np.array([[scaling_factors[0],0,0,0],
                               [0,scaling_factors[1],0,0],
                               [0,0,scaling_factors[2],0],
                               [0,0,0,1]])
    parcial_result = np.dot(scaling_matrix, polygon)
    
    final_result = translation(parcial_result, inverted_translation_coordinates)
    
    return final_result

def rotation_x(Polygon, Angle, Rotation_Point):
    polygon = Polygon
    angle = Angle
    translation_coordinates = [polygon[0][Rotation_Point]*-1,
                               polygon[1][Rotation_Point]*-1,
                               polygon[2][Rotation_Point]*-1]
    
    inverted_translation_coordinates = [polygon[0][Rotation_Point],
                                        polygon[1][Rotation_Point],
                                        polygon[2][Rotation_Point]*-1]
    
    polygon = translation(polygon, translation_coordinates)  
        
    rotation_matrix = np.array([[1,0,0,0],
                                [0,np.cos(np.radians(angle)), np.sin(np.radians(angle))*-1,0],
                                [0,np.sin(np.radians(angle)), np.cos(np.radians(angle)),0], 
                                [0,0,0,1]]
                               )
    parcial_result = np.dot(rotation_matrix, polygon)  

    
    final_result = translation(parcial_result, inverted_translation_coordinates)
    
    return final_result

def rotation_y(Polygon, Angle, Rotation_Point):
    polygon = Polygon
    angle = Angle
    translation_coordinates = [polygon[0][Rotation_Point]*-1,
                               polygon[1][Rotation_Point]*-1,
                               polygon[2][Rotation_Point]*-1]
    
    inverted_translation_coordinates = [polygon[0][Rotation_Point],
                                        polygon[1][Rotation_Point],
                                        polygon[2][Rotation_Point]*-1]
    
    polygon = translation(polygon, translation_coordinates)  
        
    rotation_matrix = np.array([[np.cos(np.radians(angle)),0,np.sin(np.radians(angle)),0],
                                [0,1,0,0],
                                [0,np.sin(np.radians(angle))*-1, np.cos(np.radians(angle)),0], 
                                [0,0,0,1]]
                               )
    parcial_result = np.dot(rotation_matrix, polygon)  

    
    final_result = translation(parcial_result, inverted_translation_coordinates)
    
    return final_result

def rotation_z(Polygon, Angle, Rotation_Point):
    polygon = Polygon
    angle = Angle
    translation_coordinates = [polygon[0][Rotation_Point]*-1,
                               polygon[1][Rotation_Point]*-1,
                               polygon[2][Rotation_Point]*-1]
    
    inverted_translation_coordinates = [polygon[0][Rotation_Point],
                                        polygon[1][Rotation_Point],
                                        polygon[2][Rotation_Point]*-1]
    
    polygon = translation(polygon, translation_coordinates)  
        
    rotation_matrix = np.array([[np.cos(np.radians(angle)),np.sin(np.radians(angle))*-1,0,0],
                                [np.sin(np.radians(angle)),np.cos(np.radians(angle)),0,0],
                                [0,0,1,0], 
                                [0,0,0,1]]
                               )
    parcial_result = np.dot(rotation_matrix, polygon)  

    
    final_result = translation(parcial_result, inverted_translation_coordinates)
    
    return final_result

def main():
    
    Polygon = np.array([[0,10,10,0,0,10,10,0], 
                        [0,0,10,10,0,0,10,10],
                        [-10,-10,-10,-10,-20,-20,-20,-20]])
    
    
    Polygon = np.append(Polygon,[np.ones(len(Polygon[0]))],axis=0) 
    
    
    Angle = 45
    Rotation_Point = 0
    
    Scaling_Factors = [2,2,0]
    Fixed_Point = 0
        
    Translation_Coordinates = [-10,10,10]
    
    
    
    
    #Final_Result = rotation_y(Polygon, Angle, Rotation_Point)
    Final_Result = rotation_z(Polygon, Angle, Rotation_Point)
    
    #Final_Result = rotation_x(Polygon, Angle, Rotation_Point)
    
    #Final_Result = scaling(Polygon, Scaling_Factors, Fixed_Point)
    
    #Final_Result = translation(Polygon, Translation_Coordinates)
    
    Final_Result = np.delete(Final_Result,(3), axis=0)
    
    print(Final_Result)
    plot(Final_Result)
    
if __name__ == "__main__":
    main()
