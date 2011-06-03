#!/usr/bin/env python
import random
class Node:
    def __init__(self, weight = -1, 
                row = -1, col = -1, 
                next_node = None, next_row = None, next_col = None):
        self.weight = weight
        self.row = row
        self.col = col
        self.next_node = next_node 
        self.next_row = next_row 
        self.next_col = next_col 
    
#    def set_next_node(self, node):
#        self.next_node = node
#
#    def get_next_node(self):
#        return self.next_node

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '({0},{1}) -> {2}'.format(self.row, self.col, self.next_node)


class Graphic :
    def __init__(self, row_list = []):
        self.row_list = row_list
        self.col_list = []
    
    @staticmethod
    def generate_col_list(matrix):
        # SWAP row and column
        col_matrix = [[row[i] for row in matrix] for i in range(matrix.__len__())]
        row, col = 0,0
        ret = []
        for cols in col_matrix:
            row = 0
            cur = Node(col=col)
            ret.append(cur)
            for weight in cols:
                if weight > 0:
                    cur.next_node=Node(weight=weight,row=row,col=col)
                    cur = cur.next_node
                row += 1
            col += 1
        return ret
        
    @staticmethod
    def generate_row_list(matrix):
        row, col = 0, 0
        ret = []
        for rows in matrix:
            col = 0
            cur = Node(row=row)
            ret.append(cur)
            for weight in rows:
                if weight > 0:
                    cur.next_node=Node(weight=weight,row=row,col=col)
                    cur = cur.next_node
                col += 1
            row += 1
        return ret

    @staticmethod
    def generate_matrix(num_nodes, undirected = True, weight=1):
        ret = []
        while ret.__len__() < num_nodes:
            row, col, tmp = ret.__len__(),0, []
            while col < num_nodes:
            #ret.append([random.randint(0,1) for i in range(num_nodes)])
                if col == row : tmp.append(-1)
                elif col < row and undirected: 
                    tmp.append(ret[col][row])
                else:
                    tmp.append(random.randint(0,weight))
                col += 1
            ret.append(tmp)
        return ret

if __name__=='__main__':
    num_nodes = 4
    matrix =  Graphic.generate_matrix(num_nodes,undirected=False,weight=10)
    #tmp = Node(row=0, col=1, next_node=Node(row=0, col=2))
    print matrix
    print "=========ROW LIST===============" 
    tmp = Graphic.generate_row_list(matrix)
    for l in tmp:
        print l
    
    print "=========COL LIST===============" 
    tmp = Graphic.generate_col_list(matrix)
    for l in tmp:
        print l
