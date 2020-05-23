class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        rows = self.matrix_string.splitlines()
        if index-1 >= len(rows) or index <= 0:
            raise Exception("Index out of range")
        
        return list(map(int, rows[index-1].split(' ')))

    def column(self, index):
        rows = self.matrix_string.splitlines()
        rows = list([i.split() for i in rows])
        columns = []
        if index-1 >= len(rows) or index <= 0:
            raise Exception("Index out of range")
        for i in range(len(rows)):
            if rows[i][index-1] != ' ':
        	    columns.append(int(rows[i][index-1]))
        return columns
