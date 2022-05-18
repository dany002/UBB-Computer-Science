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
        self.__activities_duration = {}
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

    def remove_vertex(self, vertex):
        outbound = self.out_neighbours(vertex)
        inbound = self.in_neighbours(vertex)
        for element in outbound:
            self.__inbound[element].remove(vertex)
        for element in inbound:
            self.__outbound[element].remove(vertex)
        del self.__inbound[vertex]
        del self.__outbound[vertex]
        self.__vertices.remove(vertex)



    def delete_vertex(self, vertex):
        """ This function deletes a vertex from the graph.

        :param vertex: vertex that is going to be deleted.
        :type vertex: integer
        :raises VertexError: if the vertex doesn't exist.
        """
        print("VERTEXXX", vertex)
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
        print(vertex, "vertices:", self.__vertices)
        self.__vertices.pop(vertex)
        print(vertex, "vertices:", self.__vertices)

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


    def BFS(self, start, final):
        """
        It finds the path between a start vertex and a final vertex. By using a queue, a list of visited and also it uses a list of previous
        verices to find the shortest path. It uses backward BFS so it starts from the final index and it finds the neighbors using inbounds.
        :param start: integer
        :param final: integer
        """
        if self.check_vertex(start) == False:
            raise VertexError("The vertex doesn't exist.")
        if self.check_vertex(final) == False:
            raise VertexError("The vertex doesn't exist.")

        queue = []
        visited = [final]
        prev = {}
        for vertex in self.__vertices:
            prev[vertex] = None

        queue.append(final)
        while queue:
            current_node = queue.pop(0)
            for node in self.__inbound[current_node]:
                if node not in visited:
                    visited.append(node)
                    queue.append(node)
                    prev[node] = current_node
                    if node == start:
                        queue.clear()
                        break

        self.trace_route(start, final, prev)

    def trace_route(self, start, end, prev):
        """
        It prints the shortest route/path using prev list created in BFS.
        :param start: integer
        :param end: integer
        :param prev: list
        """
        node = start
        route = []

        while node != None:
            route.append(node)
            node = prev[node]
        if start not in route or end not in route:
            print("There is no path between the given vertices.")
        else:
            print(route)


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
            for i in range(len(self.__vertices)):
                for j in range(len(self.__vertices)):
                    if distance[i][j] > distance[i][k] + distance[k][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]
                        next[i][j] = next[i][k]

        print("Next = ")
        self.print_matrix(next)
        print("Distance = ")
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


    def predecessor_counting_algorithm(self):
        sorted = []
        queue = []
        count = {}
        for vertex in self.__vertices:
            count[vertex] = len(self.in_neighbours(vertex))
            if count[vertex] == 0:
                queue.append(vertex)
        while len(queue) != 0:
            vertex = queue.pop(0)
            sorted.append(vertex)
            for y in self.__outbound[vertex]:
                count[y] = count[y] - 1
                if count[y] == 0:
                    queue.append(y)

        if len(sorted) < len(self.__vertices):
            return None
        return sorted



    def set_activity_duration(self, activity, duration):
        self.__activities_duration[activity] = duration

    def get_all_activities_duration(self):
        return self.__activities_duration

    def compute_times(self, sorted_list):
        first = -1
        last = len(sorted_list)
        inf = 999

        self.add_vertex(first)
        self.add_vertex(last)

        sorted_list.insert(0, first)
        self.__activities_duration[first] = 0
        for vertex in self.__vertices:
            if len(self.in_neighbours(vertex)) == 0 and vertex != first and vertex != last:
                self.add_edge(first, vertex, 0)

        sorted_list.append(last)

        self.__activities_duration[last] = 0
        for vertex in self.__vertices:
            if len(self.out_neighbours(vertex)) == 0 and vertex != first and vertex != last:
                self.add_edge(vertex, last, 0)

        earliest_start_time = {}
        earliest_end_time = {}
        for vertex in self.__vertices:
            earliest_start_time[vertex] = 0
            earliest_end_time[vertex] = 0

        latest_start_time = {}
        latest_end_time = {}
        for vertex in self.__vertices:
            latest_start_time[vertex] = inf
            latest_end_time[vertex] = inf

        for i in range(1, len(sorted_list)):
            for predecessor in self.in_neighbours(sorted_list[i]):
                earliest_start_time[sorted_list[i]] = max(earliest_start_time[sorted_list[i]],
                                                          earliest_end_time[predecessor])
            earliest_end_time[sorted_list[i]] = earliest_start_time[sorted_list[i]] + self.__activities_duration[
                sorted_list[i]]

        latest_end_time[last] = earliest_end_time[last]
        latest_start_time[last] = latest_end_time[last] - self.__activities_duration[last]
        latest_start_time[first] = 0
        latest_end_time[first] = 0

        for i in range(len(sorted_list) - 1, 0, -1):
            for successor in self.out_neighbours(sorted_list[i]):
                latest_end_time[sorted_list[i]] = min(latest_end_time[sorted_list[i]], latest_start_time[successor])
            latest_start_time[sorted_list[i]] = latest_end_time[sorted_list[i]] - self.__activities_duration[sorted_list[i]]

        sorted_list.pop(0)
        sorted_list.pop()
        self.remove_vertex(first)
        self.remove_vertex(last)


        critical_activities = []
        for activity in sorted_list:
            if earliest_start_time[activity] == latest_start_time[activity]:
                critical_activities.append(activity)

        return earliest_start_time, earliest_end_time, latest_start_time, latest_end_time, critical_activities


    def activities_scheduling(self):
        sorted_list = self.predecessor_counting_algorithm()
        if sorted_list is None:
            raise FileError("The graph is not DAG")
        print("The result of topological sorting: ", sorted_list)


        earliest_start_time, earliest_end_time, latest_start_time, latest_end_time, critical_activities = \
            self.compute_times(sorted_list)

        for vertex in sorted_list:
            print(f"Activity {vertex}: earliest starting time: {earliest_start_time[vertex]} - "
                  f"earliest ending time {earliest_start_time[vertex] + self.__activities_duration[vertex]} | "
                  f"latest starting time: {latest_start_time[vertex]} - "
                  f"latest ending time {latest_start_time[vertex] + self.__activities_duration[vertex]}")
        print(f"Total cost of the project: {earliest_start_time[len(sorted_list)]}")
        print("Critical activities: ", end="")
        for activity in critical_activities:
            print(activity, end=" ")
        print("")
