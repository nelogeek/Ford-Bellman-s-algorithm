#from collections import defaultdict

class Graph: 

    def __init__(self, matrix): 
        self.V = len(matrix)
        self.graph = []
        #создание графа из матрицы(ветвей с вершинами)
        for i in range(self.V):
            for j in range(self.V):
                if (matrix[i][j] != float('inf')):
                    self.add_Edge(i, j, matrix[i][j])
        #---------------------------------------------

    #функция добавления рёбер
    def add_Edge(self, u, v, w): 
        self.graph.append([u, v, w])
    #------------------------
		
    #вывод результата
    def printArr(self, dist):
        print(f"Расстояние от источника до вершин:") 
        for i in range(self.V):
            try:
                print(f"{i+1} - {dist[i]}") 
            except:
                print()
                
	#функция нахождения кратчайшего расстояния от начальной вершин
        #до других вершин (P.s. определяет отрицательные циклы)
    def BellmanFord(self, src): 

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
    
i = float('inf')

matrix = [
#      1   2   3   4   5   6
    [  i,  i,  5,  5,  2,  12  ],#1
    [  i,  i,  i,  i,  i,   2  ],#2
    [  i,  2,  i,  i,  i,   i  ],#3
    [  i,  2,  i,  i,  i,   i  ],#4
    [  i,  i,  1,  2,  i,   i  ],#5
    [  i,  i,  i,  i,  i,   i  ] #6
]

g = Graph(matrix).BellmanFord(0) 

















