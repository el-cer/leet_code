'''class Solution:
    def __init__(self,matrix):
        self.matrix = matrix
        self.spiralOrder()
    def spiralOrder(self) :
        print(self.matrix[0])
        for m in range(len(self.matrix)):
                
                       while len(self.matrix) !=0: 
                            list_1 = [self.matrix[0]]
                            self.matrix.remove(list_1)
                            list_2 = [self.matrix[m-len(self.matrix)+1:len(self.matrix)][:-1]]
                            self.matrix.remove(list_2)
                            list_3 = [self.matrix[len(self.matrix)][::-1]]
                            self.matrix.remove(list_3)
                            list_4 = [self.matrix[1:m-len(self.matrix)+1][0]]
                            self.matrix.remove(list_4)
                            main_list = list_1+list_2+list_3+list_4
                            print(main_list)
                            
'''
        
class Solution:
 

    def spiralOrder(self,matrix):
        result = []
        while matrix:
            # Traverse the first row
            result.extend(matrix.pop(0))

            # Traverse the last column
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop(-1))

            # Traverse the last row in reverse order
            if matrix and matrix[0]:
                result.extend(matrix.pop(-1)[::-1])

            # Traverse the first column in reverse order
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))

        return matrix

sol = Solution()
sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
