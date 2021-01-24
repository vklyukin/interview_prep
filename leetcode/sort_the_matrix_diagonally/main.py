class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        row_number, col_number = len(mat), len(mat[0])
        
        for diag_index in range(-row_number + 1, col_number):
            # col_index - row_index = diag_index
            
            diag_elements = [
                mat[row_index][diag_index + row_index]
                for row_index in range(max(0, -diag_index), row_number)
                if 0 <= diag_index + row_index < col_number
            ]
            
            diag_elements.sort()
                
            for i, row_index in enumerate(
                range(max(0, -diag_index), row_number)
            ):
                col_index = diag_index + row_index
                if col_index < 0 or col_index >= col_number:
                    continue
                mat[row_index][col_index] = diag_elements[i]
                
        return mat
        