import copy
from random import randint
from src.Exception import VertexError, EdgeError, FileError
import os.path

class DirectedGraph:
    def __init__(self, vertices):
        """ Constructor for graph.

        :param vertices: a list of initial vertices.
        :type vertices: a list of ints.
        """
        self.__inbound = {}
        self.__outbound = {}
        self.__cost = {'edge': [], 'cost': []}
        self.__vertices = vertices
        self.start(vertices)


    def start(self, vertices):
        """ This function creates the inbound and outbound list for each vertex.

        :param vertices: a list of initial vertices.
        :type vertices: a list of ints.
        """
        for vertex in vertices:
            self.__inbound[vertex] = []
            self.__outbound[vertex] = []

    def add_edge(self, x, y, c):
        """ This function adds an edge to the graph.

        :param x: the first vertex
        :type x: integer
        :param y: the second vertex
        :type y: integer
        :param c: the cost of the edge
        :type c: integer
        :raises EdgeError: if the edge already exists
        :raises VertexError: if at least one vertex doesn't exist.
        """
        try:
            if self.is_edge(x, y) == True:
                raise EdgeError("You can't add an edge that already exists.")
        except VertexError:
            raise VertexError("One of the vertices or both don't exist.")
        self.__inbound[y].append(x)
        self.__outbound[x].append(y)
        self.__cost['edge'].append([x,y])
        self.__cost['cost'].append(c)

    def get_edges(self):
        """ This function returns the list of edges with costs.

        :return: list with the edges and the costs for each edge.
        """
        return self.__cost

    def update_cost(self, first_vertex, second_vertex, new_cost):
        """ This function updates the cost for a given edge.

        :param first_vertex: first vertex of the edge.
        :type first_vertex: integer
        :param second_vertex: second vertex of the edge
        :type second_vertex: integer
        :param new_cost: the new cost for the given edge
        :type new_cost: integer
        :raises EdgeError: if the edge doesn't exist
        :raises VertexError: if at least one vertex doesn't exist.
        """
        try:
            if self.is_edge(first_vertex, second_vertex) == True:
                i = self.find_edge_for_2_vertices(first_vertex, second_vertex)
                self.__cost['cost'][i] = new_cost
            else:
                raise EdgeError("The edge doesn't exist.")
        except VertexError:
            raise VertexError("A vertex or both don't exist.")


    def add_vertex(self, vertex):
        """ This function adds a vertex to the graph.

        :param vertex: vertex that is going to be added.
        :type vertex: integer
        :raises VertexError: if the vertex already exists.
        """
        if vertex in self.__vertices:
            raise VertexError("You can't add a vertex that already exists.")
        self.__inbound[vertex] = []
        self.__outbound[vertex] = []
        self.__vertices.append(vertex)

    def find_edge_for_2_vertices(self, first_vertex, second_vertex):
        """ This function returns the index for a given edge.

        :param first_vertex: first vertex of edge.
        :type first_vertex: integer
        :param second_vertex: second vertex of edge
        :type second_vertex: integer
        :return: the i-th element from the list, if the edge was found. -1 otherwise.
        """
        for i in range(len(self.__cost['edge'])):
            if self.__cost['edge'][i][0] == first_vertex and self.__cost['edge'][i][1] == second_vertex:
                return i
        return -1

    def delete_edge(self, first_vertex, second_vertex):
        """ This function deletes an edge from the graph.

        :param first_vertex: first vertex of the edge.
        :type first_vertex: integer
        :param second_vertex: second vertex of the edge.
        :type second_vertex: integer
        :raises EdgeError: if the edge doesn't exist.
        :raises VertexError: if at least one vertex doesn't exist.
        """
        try:
            if self.is_edge(first_vertex, second_vertex) == True:
                k = self.find_edge_for_2_vertices(first_vertex, second_vertex)
                del self.__cost['cost'][k]
                del self.__cost['edge'][k]

                for i in range(len(self.__outbound[first_vertex])):
                    if self.__outbound[first_vertex][i] == second_vertex:
                        del self.__outbound[first_vertex][i]
                        break

                for i in range(len(self.__inbound[second_vertex])):
                    if self.__inbound[second_vertex][i] == first_vertex:
                        del self.__inbound[second_vertex][i]
                        break

            else:
                raise EdgeError("Edge doesn't exist.")
        except VertexError:
            raise VertexError("One or both the vertices don't exist.")

    def delete_vertex(self, vertex):
        """ This function deletes a vertex from the graph.

        :param vertex: vertex that is going to be deleted.
        :type vertex: integer
        :raises VertexError: if the vertex doesn't exist.
        """
        if vertex not in self.__vertices:
            raise VertexError("The vertex doesn't exist.")
        vertex = int(vertex)
        i = 0
        while i < len(self.__outbound[vertex]): # I parse the list of dout[vertex].
            j = 0
            while j < len(self.__inbound[self.__outbound[vertex][i]]): # I parse the list of the din[x] where x is every element from dout[vertex]/
                if self.__inbound[self.__outbound[vertex][i]][j] == vertex: # If the element from din[x] == vertex we delete it.
                    k = self.find_edge_for_2_vertices(vertex, self.__outbound[vertex][i]) # I find the edge to delete it.
                    del self.__cost['cost'][k]
                    del self.__cost['edge'][k]
                    del self.__inbound[self.__outbound[vertex][i]][j]

                    break # There is always an element.
                j += 1
            i += 1
        self.__outbound.pop(vertex)
        i = 0
        while i < len(self.__inbound[vertex]): # I parse the list of the din[vertex]
            j = 0
            while j < len(self.__outbound[self.__inbound[vertex][i]]): # I parse the list of the dout[x] where x is every element from din[vertex]
                if self.__outbound[self.__inbound[vertex][i]][j] == vertex: # If the element from dout[x] == vertex we delete it.
                    k = self.find_edge_for_2_vertices(self.__inbound[vertex][i], vertex)
                    del self.__cost['cost'][k]
                    del self.__cost['edge'][k]
                    del self.__outbound[self.__inbound[vertex][i]][j]
                    break # There is only an element.
                j += 1
            i += 1
        self.__inbound.pop(vertex)
        self.__vertices.pop(vertex)

        # dout[0] -> 154 161 306 437 670 886 908; din[0] -> 0: 154 326 423 583
        # 0: 154 161 306 437 670 886 908 <- out
        # 0: 154 326 423 583 <- in
        # din[154] -> 154: 0 14 232 532 837
        # dout[154] -> 154: 0 90

    def vertices(self):
        """ This function returns the list of vertices.

        :return: list of vertices.
        """
        return self.__vertices

    def check_vertex(self, vertex):
        """ This function checks if a vertex is in the list of vertices.

        :param vertex: vertex that is going to be checked
        :type vertex: integer
        :return: True if the vertex is found, false otherwise
        """
        return vertex in self.__vertices

    def out_neighbours(self, x):
        """ This function returns the out neighbours for a given vertex.

        :param x: the vertex for which we want to know the out neighbours
        :type x: integer
        :raises VertexError: if the vertex is not in the list of vertices.
        :return: a copy of the list of out neighbours for the given vertex.
        """
        if self.check_vertex(x) == False:
            raise VertexError("The vertex doesn't exist.")
        return copy.copy(self.__outbound[x])


    def is_edge(self, x, y):
        """ This function checks if there is an edge between 2 vertices.

        :param x: the first vertex
        :type x: integer
        :param y: the second vertex
        :type y: integer
        :raises VertexError: if the vertex is not in the list of vertices.
        :return: True if there is an edge, False otherwise.
        """
        if self.check_vertex(x) == False or self.check_vertex(y) == False:
            raise VertexError("One of the vertices or both don't exist.")
        return y in self.__outbound[x]


    def in_neighbours(self, x):
        """ This function returns the in neighbours for a given vertex.

        :param x: the vertex for which we want to know the in neighbours
        :type x: integer
        :raises VertexError: if the vertex is not in the list of vertices.
        :return: a copy of the list of in neighbours for the given vertex.
        """
        if self.check_vertex(x) == False:
            raise VertexError("The vertex doesn't exist.")
        return copy.copy(self.__inbound[x])


    def isolated_vertex(self, vertex):
        """ This function checks if a vertex is isolated.

        :param vertex: vertex for which we want to check if it is isolated.
        :type vertex: integer
        :raises VertexError: if the vertex is not in the list of vertices.
        :return: True if the vertex is an isolated one, False otherwise.
        """
        if self.check_vertex(vertex) == False:
            raise VertexError("The vertex doesn't exist.")
        if len(self.__inbound[vertex]) == 0 and len(self.__outbound[vertex]) == 0:
            return True
        return False

    def find_all_the_isolated_vertices(self):
        """ This function returns a list with all the isolated vertices.

        :return: list with isolated vertices.
        """
        new_list_with_the_isolated_vertices = []
        for vertex in self.__vertices:
            if self.isolated_vertex(vertex) == True:
                new_list_with_the_isolated_vertices.append(vertex)

        return new_list_with_the_isolated_vertices

    def save_graph_to_a_text_file(self, file_name):
        """ This function save the graph in a text file. On the first line is going to be
        the number of vertices. On the second line is going to be the isolated vertices.
        And then on the next lines are going to be the edges with the cost.

        :param file_name: name of the file.
        :type file_name: string
        """
        file = open(file_name, "wt")
        file.write(str(len(self.__vertices)) + '\n')
        file.write("Isolated " + str(self.find_all_the_isolated_vertices()) + '\n')
        for i in range(len(self.__cost['edge'])):
            file.write(str(self.__cost['edge'][i][0]) + " " + str(self.__cost['edge'][i][1]) + " " +str(self.__cost['cost'][i]) + '\n')
        file.close()

    def load_graph_from_a_text_file(self, file_name):
        """ This function loads the graph from a given text file and it creates a graph with the informations from file.

        :param file_name: name of the file
        :type file_name: string
        :raises FileError: if the file doesn't exist.
        """
        if not os.path.exists(file_name):
            raise FileError("File doesn't exist.")
        file = open(file_name, "rt")
        self.__vertices = []
        number_of_vertices = file.readline()
        isolated = file.readline()
        isolated = isolated.split(maxsplit=1, sep=" ")
        new_isolated = isolated[1]
        self.__outbound = {}
        self.__inbound = {}
        if len(isolated[1]) != 3:
            new_isolated = new_isolated[1:-2] # We get rid of [].
            vertices = new_isolated.split(sep=",")
            for i in range(len(vertices)):

                vertex = int(vertices[i])
                self.__vertices.append(vertex)
                self.__inbound[vertex] = []
                self.__outbound[vertex] = []

        for line in file.readlines():
            first_vertex, second_vertex, cost = line.split(maxsplit=2, sep=" ")
            first_vertex = int(first_vertex)
            second_vertex = int(second_vertex)
            cost = int(cost)
            if first_vertex not in self.__vertices:
                self.__vertices.append(first_vertex)
                self.__inbound[first_vertex] = []
                self.__outbound[first_vertex] = []
            if second_vertex not in self.__vertices:
                self.__vertices.append(second_vertex)
                self.__inbound[second_vertex] = []
                self.__outbound[second_vertex] = []
            self.add_edge(first_vertex, second_vertex, cost)
        new_vertices = sorted(self.__vertices)
        self.__vertices = new_vertices
        file.close()

    def create_random_graph(self, vertices, edges):
        """ This function creates a random graph.
        :param vertices: number of vertices for the new graph.
        :type vertices: integer
        :param edges: number of edges for the new graph.
        :type edges: integer
        """
        for i in range(edges):
            x = randint(0, vertices - 1)
            y = randint(0, vertices - 1)
            while self.is_edge(x, y):
                x = randint(0, vertices - 1)
                y = randint(0, vertices - 1)
            cost = randint(0, 1000)
            self.add_edge(x, y, cost)


    def accessible(self, source, destination, discovered, path):
        """
        It checks if the source and the destination is in the list of vertices. If they are not it throws VertexError.
        It mark in the discovered list True the element on which we are. Then it adds in the path that element. It goes
        recursively by changing the destination into an inbound of the neighbour.
        :param source: integer
        :param destination: integer
        :param discovered: list of boolean
        :param path: deque ( it's like a list but more efficient ).
        :return: True or False depending if we have a path or not.
        """
        if source not in self.__vertices:
            raise VertexError
        if destination not in self.__vertices:
            raise VertexError

        discovered[destination] = True

        path.append(destination)

        if source == destination:
            return True

        for i in self.__inbound[destination]:
            if not discovered[i]:
                if self.accessible(source, i, discovered, path):
                    return True

        path.pop()
        return False

    def minimum_walk_with_cost(self):
        """
        It computes the minimum cost for a walk using Floyd-Warshall algorithm. It creates a matrix. On the main diagonal is going to be 0
        In rest, for every element (i,j) it puts the cost of the edge (i,j) if it exists, infinity otherwise.
        After that it takes each vertex from the list of vertices and if the sum of dis[i][k] and dis[k][j] ( where k is the new vertex )
        is greater than dis[i][j], dis[i][j] is going to be the new sum. Also there is a new matrix that keeps the track of the next element
        to find the path.
        :return: 2 matrices.
        """
        distance = [[float('inf') for _ in range(len(self.__vertices))] for _ in range(len(self.__vertices))]
        next = [[None for _ in range(len(self.__vertices))] for _ in range(len(self.__vertices))]
        for i in range(len(self.__vertices)):
            distance[i][i] = 0
            next[i][i] = i

        for i in range(len(self.__cost['edge'])):
            distance[self.__cost['edge'][i][0]][self.__cost['edge'][i][1]] = self.__cost['cost'][i] # I put in every cell of the matrix the cost for that one.
            next[self.__cost['edge'][i][0]][self.__cost['edge'][i][1]] = self.__cost['edge'][i][1]

        for k in range(len(self.__vertices)):
            print("k = ", k)
            self.print_matrix(distance)
            for i in range(len(self.__vertices)):
                for j in range(len(self.__vertices)):
                    if distance[i][j] > distance[i][k] + distance[k][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]
                        next[i][j] = next[i][k]
        print("final = ")
        self.print_matrix(distance)
        return distance, next

    def print_matrix(self, a):
        """
        It prints a matrix in a fancy way.
        :param a: list of lists.
        :return: None
        """
        s = [[str(e) for e in row] for row in a]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))
        print('\n')
