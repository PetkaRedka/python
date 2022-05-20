class Matrix:

    def __init__(self, matrix):
        self.__matrix = matrix

    
    def __add__(self, other):
    
        # Заполнение нулями
        while (len(self.__matrix[0]) != len(other.__matrix[0])):

            if len(self.__matrix[0]) < len(other.__matrix[0]):
                for i in range(len(self.__matrix)):
                    self.__matrix[i].append(0)
            
            elif len(self.__matrix[0]) > len(other.__matrix[0]):
                for i in range(len(other.__matrix)):
                    other.__matrix[i].append(0)
        
        while (len(self.__matrix) != len(other.__matrix)):

            if len(self.__matrix) < len(other.__matrix):
                self.__matrix.append([0 for i in range(len(self.__matrix[0]))])
            
            elif len(self.__matrix) > len(other.__matrix):
                other.__matrix.append([0 for i in range(len(self.__matrix[0]))])


        result = [[self.__matrix[i][j] + other.__matrix[i][j]  for j in range
                    (len(self.__matrix[0]))] for i in range(len(self.__matrix))]

        return Matrix(result)

    def __str__(self):

        string = ""
        for i in range(len(self.__matrix[0])):
            for j in range(len(self.__matrix)):

                string += str(self.__matrix[i][j]) + " "
            string += "\n" 

        return string

    
matrix1 = Matrix([[1, 2, 3],
                  [2, 3, 1],
                  [3, 2, 1]])
matrix2 = Matrix([[3, 3, 3],
                  [3, 3, 3],
                  [3, 3, 3]])
matrix3 = Matrix([[1, 2, 3],
                  [2, 3, 1]])
matrix4 = Matrix([[2, 2],
                  [2, 2],
                  [2, 2]])
matrix5 = Matrix([[2, 2, 2],
                  [2, 2, 2],
                  [2, 2, 2]])
print(matrix1 + matrix2 + matrix3 + matrix4 + matrix5)