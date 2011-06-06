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
    
    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        #if self.next_col is not None:  
        #    return '({0},{1}) -> Next Column : {2}'.format(
        #        self.row, self.col, self.next_col)
        return '({0},{1}) -> {2}'.format(
            self.row, self.col, self.next_node, self.next_col)

class SpanningTree:
    @staticmethod
    def kruskal(data, number_nodes):
        ret = {}
        trace, back_trace = {}, {}
        for item in data:
            if item.row not in trace:
                trace[item.row] = item.col
                back_trace[item.col] = item.row
                if not SpanningTree.has_loop(
                    trace, back_trace,item.col, item.row,number_nodes-1):
                    ret[(item.row, item.col)] = item
                    if ret.__len__() == number_nodes -1:
                        break
                else: 
                    del trace[item.row]
                    del back_trace[item.col]
                    
        return ret

    @staticmethod
    def has_loop(trace, back_trace, point, back_point,  max_number):
        cnt, back_cnt = 0,0
        while point in trace and cnt <= max_number:
            point = trace[point]
            cnt += 1
        while back_point in back_trace and back_cnt <= max_number:
            back_point = back_trace[back_point]
            back_cnt += 1
        return cnt > max_number or back_cnt > max_number
        


class Adjancy:
    def __init__(self, matrix):
        self.adjancy_list = self.__set_adjancy_list(matrix)
        self.flattern_array = self.flattern()

    def __set_adjancy_list(self, matrix):
        row_list = Graphic.generate_row_list(matrix)
        col_list = Graphic.generate_col_list(matrix)
        for row in row_list:
            while row is not None:
                cur_col = col_list[row.col]
                while cur_col is not None and row.row != cur_col.row:
                    cur_col = cur_col.next_node
                if cur_col is not None:
                    row.next_col = cur_col.next_node
                row.next_row = row.next_node
                row = row.next_row
        del col_list
        return row_list

    def flattern(self):
        ret = []
        for nodes in self.adjancy_list:
            while nodes is not None:
                ret.append(nodes)
                nodes = nodes.next_row
        return ret

    def unflattern(self, working_array):
        ret, cnt = [], 0
        while cnt < working_array.__len__():
            ret.append(working_array[cnt])
            while working_array[cnt].next_row is not None:
                cnt += 1
            cnt += 1
        return ret 

    def flattern_quick_sort(self):
        data = self.flattern_array[:]
        self.quick_sort(data, 0, data.__len__()-1)
        return data

    def quick_sort(self, data, lower, upper):
        if lower >= upper: return
        pivot, i, j = data[lower].weight, lower, upper
        while i < j:
            while i < upper and data[i].weight <= pivot:
                i += 1
            while j > lower and data[j].weight > pivot :
                j -= 1
            if i < j:
                tmp = data[i]
                data[i] = data[j]
                data[j] = tmp
        tmp = data[j]
        data[j] = data[lower]
        data[lower] = tmp
        self.quick_sort(data, lower, j-1)
        self.quick_sort(data, j+1, upper)
class Graphic :
    def __init__(self, matrix):pass
        #self.matrix = matrix
        #self.adjancy = Adjancy(matrix)

            
    @staticmethod
    def generate_col_list(matrix):
        # SWAP row and column
        col_matrix = [[row[i] for row in matrix] 
                for i in range(matrix.__len__())]
        row, col = 0,0
        ret = []
        for cols in col_matrix:
            row = 0
            cur = Node(col=col)
            ret.append(cur)
            for weight in cols:
                if weight > 0:
                    if cur.row == -1:
                        cur.weight=weight
                        cur.row=row
                    else:
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
                    if cur.col == -1:
                        cur.weight=weight
                        cur.col=col
                    else:
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
                if col == row : tmp.append(0)
                elif col < row and undirected: 
                    tmp.append(ret[col][row])
                else:
                    tmp.append(random.randint(0,weight))
                col += 1
            ret.append(tmp)
        return ret

if __name__=='__main__':
    num_nodes = 10 
    matrix =  Graphic.generate_matrix(num_nodes, undirected=True, weight=100)
    #matrix = [[0,1,1,0],[1,0,0,1],[1,0,0,1],[0,1,1,0]]
    #tmp = Node(row=0, col=1, next_node=Node(row=0, col=2))
    print matrix
    adj = Adjancy(matrix)
    tmp = adj.flattern_quick_sort()
    tmp = SpanningTree.kruskal(tmp, num_nodes)
    for key in tmp.iterkeys():
        print key
#    print "=========ABJ LIST==============="
#    for n in adj.adjancy_list:
#        while n is not None:
#            print '(',n.row,',', n.col,')'
#            if n.next_col is not None:
#                print "Next Column: ",n.next_col.row, n.next_col.col
#            n=n.next_row
#    print "=========FLATTERN==============="
#    for item in adj.flattern_array:
#        print '({0},{1},{2})'.format(item.row, item.col, item.weight)
#
#    print "=========UNFLATTERN==============="
#    for n in adj.unflattern(adj.flattern_array):
#        while n is not None:
#            print '(',n.row,',', n.col,')'
#            if n.next_col is not None:
#                print "Next Column: ",n.next_col.row, n.next_col.col
#            n=n.next_row
