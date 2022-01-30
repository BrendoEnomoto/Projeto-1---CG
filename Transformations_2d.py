import numpy as np

def translation(Polygon, Translation_Coordinates):
    polygon = Polygon
    translation_coordinates = Translation_Coordinates
    translation_matrix = np.array([[1,0,translation_coordinates[0]],
                                   [0,1,translation_coordinates[1]],
                                   [0,0,1]])
    result = np.dot(translation_matrix, polygon)
    return result

def scaling(Polygon, Scaling_Factors, Fixed_Point):
    polygon = Polygon
    scaling_factors = Scaling_Factors
    translation_coordinates = [polygon[0][Fixed_Point]*-1,
                               polygon[1][Fixed_Point]*-1]
    
    inverted_translation_coordinates = [polygon[0][Fixed_Point],
                                    polygon[1][Fixed_Point]]
    
    polygon = translation(polygon, translation_coordinates)
    
  
    scaling_matrix = np.array([[scaling_factors[0],0,0],
                               [0,scaling_factors[1],0],
                               [0,0,1]])
    parcial_result = np.dot(scaling_matrix, polygon)
    
    final_result = translation(parcial_result, inverted_translation_coordinates)
    
    return final_result

def rotation(Polygon, Angle, Rotation_Point):
    polygon = Polygon
    angle = Angle
    translation_coordinates = [polygon[0][Rotation_Point]*-1,
                               polygon[1][Rotation_Point]*-1]
    
    inverted_translation_coordinates = [polygon[0][Rotation_Point],
                                        polygon[1][Rotation_Point]]
    
    polygon = translation(polygon, translation_coordinates)  
        
    rotation_matrix = np.array([[np.cos(np.radians(angle)), np.sin(np.radians(angle))*-1, 0],
                                [np.sin(np.radians(angle)), np.cos(np.radians(angle)), 0], 
                                [0,0,1]]
                               )
    parcial_result = np.dot(rotation_matrix, polygon)  

    
    final_result = translation(parcial_result, inverted_translation_coordinates)
    
    return final_result

def main():
    
    Polygon = np.array([[0,10,10,0],
                        [0,0,10,10]])

if __name__ == "__main__":
    main()

