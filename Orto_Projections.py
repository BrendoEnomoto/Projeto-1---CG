import numpy as np
from Polilinha import plot 
def orto_front(Polygon):
    polygon = Polygon
    orto_frontal_matrix = np.array([[1,0,0,0],
                                    [0,1,0,0],
                                    [0,0,0,0],
                                    [0,0,0,1]])
    result = np.dot(orto_frontal_matrix, polygon)
    result = np.delete(result,(2,3), axis=0)
    return result

def orto_top(Polygon):
    polygon = Polygon
    orto_frontal_matrix = np.array([[1,0,0,0],
                                    [0,0,0,0],
                                    [0,0,1,0],
                                    [0,0,0,1]])
    result = np.dot(orto_frontal_matrix, polygon)
    result = np.delete(result,(1,3), axis=0)
    return result

def orto_side(Polygon):
    polygon = Polygon
    orto_frontal_matrix = np.array([[0,0,0,0],
                                    [0,1,0,0],
                                    [0,0,1,0],
                                    [0,0,0,1]])
    result = np.dot(orto_frontal_matrix, polygon)
    result = np.delete(result,(0,3), axis=0)
    final_result = list(result[1]),list((result[0]))
    return list(final_result)

def main():
    Polygon = np.array([[0,10,10,0,0,10,10,0],
                        [0,0,5,5,0,10,10,0],
                        [10,10,10,10,0,0,0,0]])
    
    Polygon = np.append(Polygon,[np.ones(len(Polygon[0]))],axis=0)
    
    #Final_Result = orto_front(Polygon)
    #Final_Result = orto_top(Polygon)
    Final_Result = orto_side(Polygon)
    
    print(Final_Result)
    plot(Final_Result)
    
if __name__ == "__main__":
    main()