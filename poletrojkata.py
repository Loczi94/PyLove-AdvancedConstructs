
def calculate_area(points):
    A, B, C = points[0], points[1], points[2]
    area = 0.5 * abs(A[0]*B[1]+B[0]*C[1]+C[0]*A[1]-C[0]*B[1]-A[0]*C[1]-B[0]*A[1])
    print('Pole trojkata wynosi '+str(area))
    return area

if __name__ == '__main__':
    calculate_area([[0,0],[10,10],[10,0]])