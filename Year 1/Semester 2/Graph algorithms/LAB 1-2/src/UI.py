from src.DirectedGraph import DirectedGraph
import os.path
import re
from collections import deque
from src.Exception import VertexError, EdgeError, VertexOrEdge, YesOrNo, FileError


class UI:
    def __init__(self):
        """ Constructor for UI.
        """
        self._directed_graph = DirectedGraph(list(range(0)))

    def _menu(self):
        """ This function prints the menu for UI.
        """
        print("What do you want to do?")
        print("Type 'print' to print the graph.")
        print("Type 'add' to add an edge or a vertex.")
        print("Type 'delete' to delete an edge or a vertex.")
        print("Type 'vertices' to get the number of vertices.")
        print("Type 'degree' to get the in/out degree of a vertex.")
        print("Type 'update' to update the cost for an edge.")
        print("Type 'create' to create a random graph.")
        print("Type 'save' to save the graph in a file.")
        print("Type 'load' to load an old graph.")
        print("Type 'get' to get the edges with cost.")
        print("Type 'isolated' to get the isolated vertices.")
        print("Type 'short' to find a lowest length path between 2 vertices.")
        print("Type 'exit' to exit.")

    def _read_from_keyboard(self):
        """ This function reads from keyboard the vertices and the edges with the costs.
        Also it checks if the input is correct.
        """
        vertices = input("How many vertices?")
        a = re.search('[a-zA-Z]', vertices)
        if a == None:
            vertices = int(vertices)
        else:
            print("You have to give me a number!")
            self.run_console()
        edges = input("How many edges?")
        a = re.search('[a-zA-Z]', edges)
        if a == None:
            edges = int(edges)
        else:
            print("You have to give me a number!")
            self.run_console()
        if edges > vertices*vertices:
            print("I can't create the graph that you want!")
            self.run_console()
        for i in range(edges):
            x = input("X = ")
            y = input("Y = ")
            c = input("Cost = ")
            a = re.search('[a-zA-Z]', x)
            if a == None:
                x = int(x)
            else:
                print("The vertex must be a number.")
                return
            a = re.search('[a-zA-Z]', y)
            if a == None:
                y = int(y)
            else:
                print("The vertex must be a number.")
                return
            a = re.search('[a-zA-Z]', c)
            if a == None:
                c = int(c)
            else:
                print("The cost must be a number.")
                return
            try:
                self._directed_graph.add_vertex(x)
            except VertexError:
                pass
            try:
                self._directed_graph.add_vertex(y)
            except VertexError:
                pass
            try:
                self._directed_graph.add_edge(x, y, c)
            except EdgeError:
                print("You can't add an edge that already exists.")
            except VertexError:
                print("One of the vertices or both don't exist.")

    def _read_from_file(self):
        """ This function reads from a file a graph. On the first line is the number of vertices and the edges.
        And then on each line is going to be the first vertex, the second one and the cost for that edge.
        """
        file_name = input("What is the file name?")
        if not os.path.exists(file_name):
            print("The file doesn't exist.")
            self.run_console()
        file = open(file_name, "rt")
        first_line = file.readline()
        n, m = first_line.split()
        n = int(n)
        self._directed_graph = DirectedGraph(list(range(n)))
        for line in file.readlines():
            x, y, c = line.split(maxsplit=2, sep=" ")
            self._directed_graph.add_edge(int(x), int(y), int(c))
        file.close()

    def print_both(self):
        """ This function prints the outbounds and the inbounds for the graph.
        """
        print("Outbounds: ")
        for x in self._directed_graph.vertices():
            s = str(x) + ":"
            for y in self._directed_graph.out_neighbours(x):
                s = s + " " + str(y)
            print(s)
        print("Inbounds: ")
        for x in self._directed_graph.vertices():
            s = str(x) + ":"
            for y in self._directed_graph.in_neighbours(x):
                s = s + " " + str(y)
            print(s)

    def print_inbound(self):
        """ This function prints the inbounds for the graph.
        """
        for x in self._directed_graph.vertices():
            s = str(x) + ":"
            for y in self._directed_graph.in_neighbours(x):
                s = s + " " + str(y)
            print(s)

    def print_outbounds(self):
        """ This function prints the outbounds for the graph.
        """
        for x in self._directed_graph.vertices():
            s = str(x) + ":"
            for y in self._directed_graph.out_neighbours(x):
                s = s + " " + str(y)
            print(s)

    def print_inbounds_for_a_vertex(self, vertex):
        """ This function prints the inbounds of a vertex.
        :param vertex: the vertex for which we want to see the inbounds.
        :type vertex: integer
        """
        if self._directed_graph.check_vertex(vertex) == False:
            print("The vertex doesn't exist.")
            return
        s = str(vertex) + ":"
        for y in self._directed_graph.in_neighbours(vertex):
            s = s + " " + str(y)
        print(s)

    def print_outbounds_for_a_vertex(self, vertex):
        """ This function prints the outbounds of a vertex.
        :param vertex: the vertex for which we want to see the outbounds.
        :type vertex: integer
        """
        if self._directed_graph.check_vertex(vertex) == False:
            print("The vertex doesn't exist.")
            return
        s = str(vertex) + ":"
        for y in self._directed_graph.out_neighbours(vertex):
            s = s + " " + str(y)
        print(s)

    def print_specific(self):
        """ This function connects the inbounds and outbounds print.
        """
        vertex = input("For what vertex do you want to know more?")
        print("Type 'in' to print the inbounds for the given vertex.")
        print("Type 'out' to print the outbounds for the given vertex.")
        print("Type 'both' to print both for the given vertex.")
        vertex = int(vertex)
        in_or_out_or_both = input()
        in_or_out_or_both = in_or_out_or_both.lower()
        if in_or_out_or_both == "in":
            self.print_inbounds_for_a_vertex(vertex)
        elif in_or_out_or_both == "out":
            self.print_outbounds_for_a_vertex(vertex)
        elif in_or_out_or_both == "both":
            print("Inbounds: ")
            self.print_inbounds_for_a_vertex(vertex)
            print("Outbounds: ")
            self.print_outbounds_for_a_vertex(vertex)

    def _print(self):
        """ This function connects the printing for the graph: in/out/both or specific if we want details about a vertex.
        """
        print("What do you want to print?")
        print("Type 'in' to print the inbounds.")
        print("Type 'out' to print the outbounds.")
        print("Type 'both' to print both.")
        print("Type 'specific' to print the inbounds/outbounds for a specific vertex.")
        in_out_both = input()
        in_out_both = in_out_both.lower()
        if in_out_both == "in":
            self.print_inbound()
        elif in_out_both == "out":
            self.print_outbounds()
        elif in_out_both == "both":
            self.print_both()
        elif in_out_both == "specific":
            self.print_specific()

    def add_vertex(self):
        """ This function checks the input and it adds the vertex to the graph.
        :return:
        """
        vertex = input("What is the vertex you want to add?")
        x = re.search('[a-zA-Z]', vertex)
        if x == None:
            vertex = int(vertex)
        else:
            print("The vertex must be a number.")
            return
        try:
            self._directed_graph.add_vertex(vertex)
        except VertexError:
            print("You can't add a vertex that already exists.")

    def add_edge(self):
        """ This function checks the input and it adds the edge to the graph.
        """

        x = input("X = ? ")
        y = input("Y = ? ")
        c = input("Cost = ? ")
        a = re.search('[a-zA-Z]', x)
        if a == None:
            x = int(x)
        else:
            print("The vertex must be a number.")
            return
        a = re.search('[a-zA-Z]', y)
        if a == None:
            y = int(y)
        else:
            print("The vertex must be a number.")
            return
        a = re.search('[a-zA-Z]', c)
        if a == None:
            c = int(c)
        else:
            print("The cost must be a number.")
            return
        try:
            self._directed_graph.add_edge(x, y, c)
        except EdgeError:
            print("You can't add an edge that already exists.")
        except VertexError:
            print("One of the vertices or both don't exist.")

    def add(self):
        """ This function connects add_vertex and add_edge.
        :raises VertexOrEdge: if the input is not vertex or edge.
        """
        vertex_or_edge = input("What do you want to add? Vertex or edge?")
        vertex_or_edge = vertex_or_edge.lower()
        if vertex_or_edge == "vertex":
            self.add_vertex()
        elif vertex_or_edge == "edge":
            self.add_edge()
        else:
            raise VertexOrEdge

    def delete_vertex(self):
        """ This function checks the input and deletes the vertex from the graph.
        """
        vertex = input("What is the vertex you want to delete?")
        x = re.search('[a-zA-Z]', vertex)
        if x == None:
            vertex = int(vertex)
        else:
            print("The vertex must be a number.")
            return
        try:
            self._directed_graph.delete_vertex(vertex)
        except VertexError:
            print("You can't delete a vertex that doesn't exist.")

    def delete_edge(self):
        """ This function checks the input and deletes the edge from the graph.
        """
        x = input("X = ? ")
        y = input("Y = ? ")
        a = re.search('[a-zA-Z]', x)
        if a == None:
            x = int(x)
        else:
            print("The vertex must be a number.")
            return
        a = re.search('[a-zA-Z]', y)
        if a == None:
            y = int(y)
        else:
            print("The vertex must be a number.")
            return
        try:
            self._directed_graph.delete_edge(x, y)
        except VertexError:
            print("One or both the vertices don't exist.")
        except EdgeError:
            print("Edge doesn't exist.")

    def delete(self):
        """ This function connects delete_vertex and delete_edge
        :raises VertexOrEdge: if the input is not vertex or edge.
        """
        vertex_or_edge = input("What do you want to delete? Vertex or edge?")
        vertex_or_edge = vertex_or_edge.lower()
        if vertex_or_edge == "vertex":
            self.delete_vertex()
        elif vertex_or_edge == "edge":
            self.delete_edge()
        else:
            raise VertexOrEdge

    def get_number_of_vertices(self):
        """ This function prints the number of vertices and also the list of vertices if the user wants to.
        :raise YesOrNo: if the user doesn't answer with yes or no.
        """
        print("The number of vertices are: ", len(self._directed_graph.vertices()))
        yes_or_no = input("Do you want to print the list of vertices? Yes or no?")
        yes_or_no = yes_or_no.lower()
        if yes_or_no == "yes":
            for i in range(len(self._directed_graph.vertices())):
                print(self._directed_graph.vertices()[i])
        elif yes_or_no == "no":
            return
        else:
            raise YesOrNo


    def get_degree(self):
        """ This function counts the in and out degree for a given vertex. Also it validates the input.
        """
        vertex = input("For what vertex do you want to know the in and out degree?")
        in_degree = 0
        out_degree = 0
        x = re.search('[a-zA-Z]', vertex)
        if x == None:
            vertex = int(vertex)
        else:
            print("The vertex must be a number.")
            return
        if self._directed_graph.check_vertex(vertex) == False:
            print("Vertex doesn't exist")
            return
        for y in self._directed_graph.in_neighbours(vertex):
            in_degree += 1
        for y in self._directed_graph.out_neighbours(vertex):
            out_degree += 1
        print("In degree", in_degree)
        print("Out degree", out_degree)

    def update_cost(self):
        """ This function validates the input and it updates the cost for a given edge.
        """
        x = input("X = ? ")
        y = input("Y = ? ")
        cost = input("New cost = ? ")
        a = re.search('[a-zA-Z]', x)
        if a == None:
            x = int(x)
        else:
            print("The vertex must be a number.")
            return
        a = re.search('[a-zA-Z]', y)
        if a == None:
            y = int(y)
        else:
            print("The vertex must be a number.")
            return
        a = re.search('[a-zA-Z]', cost)
        if a == None:
            cost = int(cost)
        else:
            print("The cost must be a number.")
            return
        try:
            self._directed_graph.update_cost(x, y, cost)
        except EdgeError:
            print("The edge doesn't exist.")
        except VertexError:
            print("A vertex or both don't exist.")


    def create_random_graph(self):
        """ This function creates a random graph and also validates the input and it checks if it's possible to create
        a graph with the given number of vertices and edges.
        """
        vertices = input("How many vertices do you want to have?")
        edges = input("How many edges do you want to have?")
        a = re.search("[a-zA-Z]", vertices)
        if a == None:
            vertices = int(vertices)
        else:
            print("You can't have letters in the number of vertices!")
            self.create_random_graph()
        a = re.search("[a-zA-Z]", edges)
        if a == None:
            edges = int(edges)
        else:
            print("You can't have letters in the number of edges!")
            self.create_random_graph()

        if edges > vertices*vertices:
            print("It's impossible to create your graph! I'm sorry!")
            self.create_random_graph()

        self._directed_graph = DirectedGraph(list(range(vertices)))
        self._directed_graph.create_random_graph(vertices, edges)


    def save_graph(self):
        """ This function saves the graph to a file.
        """
        file_name = input("What is the file name?")
        self._directed_graph.save_graph_to_a_text_file(file_name)

    def load_graph(self):
        """ This function loads the graph from a given text file.
        """
        file_name = input("What is the file name?")
        try:
            self._directed_graph.load_graph_from_a_text_file(file_name)
        except FileError:
            print("The file doesn't exist.")


    def get_edges_and_cost(self):
        """ This function prints the list of edges with the costs.
        """
        lista = self._directed_graph.get_edges()
        for i in range(len(lista['edge'])):
            print("Edge:", str(lista['edge'][i][0]), str(lista['edge'][i][1]), "  Cost:", str(lista['cost'][i]))

    def get_all_the_isolated_vertices(self):
        """ This function prints the list of isolated vertices.
        """
        for i in range(len(self._directed_graph.find_all_the_isolated_vertices())):
            print(self._directed_graph.find_all_the_isolated_vertices()[i])

    def get_lowest_length_path(self):
        """
        I print the lowest length path between 2 vertices. I check if the vertices exist and if there is a path between them.
        And if there is a path between them, it just reverse the path and it prints it.
        """
        start_vertex = int(input("What is the first vertex?"))
        end_vertex = int(input("What is the second vertex?"))
        discovered = [False] * len(self._directed_graph.vertices())
        path = deque()
        try:
            ok = self._directed_graph.accessible(start_vertex, end_vertex, discovered, path)
        except VertexError:
            print("One or both of the vertices doen't exist.")
            return
        path.reverse()
        if ok:
            print("The path is: ", list(path))
            print("The distance is: ", len(list(path)) - 1)
        else:
            print("There is no path between the given vertices.")



    def run_console(self):
        """ This function is the heart of the UI. It gets the input and it connects all the functions from UI.
        """
        console_or_file = input("Do you want to read from keyboard (Type 'keyboard') or from given input ( Type 'given' ) \n"
                                "(graph1k.txt, graph10k.txt, graph100k.txt, graph1m.txt) or \n"
                                "from another file? ( Type 'file' ) \n or you can create a random graph ( Type 'random' ) \n")
        console_or_file = console_or_file.lower()
        if console_or_file == "keyboard":
            self._read_from_keyboard()
        elif console_or_file == "given":
            self._read_from_file()
        elif console_or_file == "file":
            file_name = input("What is the file name?")
            if not os.path.exists(file_name):
                print("The file doesn't exist.")
                self.run_console()
            self._directed_graph.load_graph_from_a_text_file(file_name)
        elif console_or_file == "random":
            self.create_random_graph()
        else:
            print("You have to choose between: keyboard, given or file.")
            self.run_console()
        while True:
            self._menu()
            command = input("Command: \n")
            command = command.lower()
            if command == "print":
                self._print()
            elif command == "add":
                try:
                    self.add()
                except VertexOrEdge:
                    print("You have to choose between vertex or edge.")
            elif command == "delete":
                try:
                    self.delete()
                except VertexOrEdge:
                    print("You have to choose between vertex or edge.")
            elif command == "vertices":
                try:
                    self.get_number_of_vertices()
                except YesOrNo:
                    print("You have to choose between yes or no.")
            elif command == "degree":
                self.get_degree()
            elif command == "update":
                self.update_cost()
            elif command == "create":
                self.create_random_graph()
            elif command == "save":
                self.save_graph()
            elif command == "load":
                self.load_graph()
            elif command == "get":
                self.get_edges_and_cost()
            elif command == "isolated":
                self.get_all_the_isolated_vertices()
            elif command == "short":
                self.get_lowest_length_path()
            elif command == "exit":
                break