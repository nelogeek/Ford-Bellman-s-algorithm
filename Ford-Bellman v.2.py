#from collections import defaultdict
import sys

class Graph: 

    def __init__(self, matrix):
        try:
            self.V = len(matrix)
            self.graph = []
            #создание графа из матрицы(ветвей с вершинами)
            for i in range(self.V):
                for j in range(self.V):
                    if (matrix[i][j] != float('inf')):
                        self.add_Edge(i, j, matrix[i][j])
        except:
            print(f"Ошибка в {sys._getframe().f_code.co_name}")
        #---------------------------------------------

    #функция добавления рёбер
    def add_Edge(self, u, v, w):
        try:
            self.graph.append([u, v, w])
        except:
            print(f"Ошибка в {sys._getframe().f_code.co_name}")
    #------------------------
		
    #вывод результата
    def printArr(self, dist):
        try:
            print(f"Расстояние от источника до вершин:") 
            for i in range(self.V):
                try:
                    print(f"{i+1} - {dist[i]}") 
                except:
                    print()
        except:
            print(f"Ошибка в {sys._getframe().f_code.co_name}")
                
    #функция нахождения кратчайшего расстояния от начальной вершин
    #до других вершин (P.s. определяет отрицательные циклы)
    def BellmanFord(self, src):
        try:

            #забиваю список бесконечностями
            dist = [float("Inf")] * self.V 
            dist[src] = 0
            for i in range(self.V - 1): 
                for u, v, w in self.graph: 
                    if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        dist[v] = dist[u] + w 
            #проверка на наличие отрицательного цикла
            for u, v, w in self.graph: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                    print (f"Граф содержит отрицательный цикл")
                    return
            #вывод результата
            self.printArr(dist)
        except:
            print(f"Ошибка в {sys._getframe().f_code.co_name}")
            print("Ошибка! Проверьте вводимые значения!")
#----------------------------------------------------------------------     
    def Input_Matrix_size():
        
        size = Graph.size()
        return size
        
    def size():
        try:
            size = int(input(f"Введите количество элементов, содержащихся в одной строке (столбце): "))
            if size <= 0:
                print("Введите натуральное число!\n")
                
                return Graph.size()
            return size
        except:
            print(f"Ошибка в {sys._getframe().f_code.co_name}")
#----------------------------------------------------------------------
    def Input_line_matrix(size):
        try:
            line = Graph.input_n_check_line(size)
            return line
        except:
            print(f"Ошибка в {sys._getframe().f_code.co_name}")
    
    def input_n_check_line(size):
        try:
            inf = float('inf')
            line = input().split(" ")
            if len(line) != size:
                print("Ошибка! Количество вводимых элементов не соответствует размеру матрицы!\nПовторите попытку")
                return Graph.input_n_check_line(size)
            else:
                for j in range(len(line)):
                    if line[j] == 'i':
                        line[j] = inf
                    else:
                        line[j] = int(line[j])
                if line == None:
                    return Graph.input_n_check_line(size)
                else:
                    return line
        except:
            print(f"Ошибка в {sys._getframe().f_code.co_name}")
#----------------------------------------------------------------------
    def Input_matrix():
        try:
            inf = float('inf')
            size = Graph.Input_Matrix_size()
            print(f"\nВведите матрицу через пробел")
            print(f"Для обозначения бесконечности используйте 'i'")
            matrix = []
            for i in range(size):
                line = Graph.Input_line_matrix(size)
                matrix.append(line)
            
            Graph(matrix).BellmanFord(0)
        except:
            print(f"Ошибка в {sys._getframe().f_code.co_name}")

Graph.Input_matrix()


















