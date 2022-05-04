from src.DirectedGraph import DirectedGraph
from src.Exception import VertexError, VertexOrEdge, FileError, EdgeError
import unittest

class TestDirectedGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.__directed_graph = DirectedGraph(list(range(1000)))

    def tearDown(self) -> None:
        pass

    def test_add_edge(self):
        self.__directed_graph.add_edge(1, 4, 10)
        self.assertEqual(self.__directed_graph.get_edges()['edge'][0][0], 1)
        self.assertEqual(self.__directed_graph.get_edges()['edge'][0][1], 4)
        self.assertEqual(self.__directed_graph.get_edges()['cost'][0], 10)
        with self.assertRaises(EdgeError) as err:
            self.__directed_graph.add_edge(1, 4, 10)
        self.assertEqual(str(err.exception), "You can't add an edge that already exists.")

        with self.assertRaises(VertexError) as ve:
            self.__directed_graph.add_edge(1004, 23, 13)
        self.assertEqual(str(ve.exception), "One of the vertices or both don't exist.")

    def test_update_cost_of_an_edge(self):
        self.__directed_graph.add_edge(1, 4, 10)
        self.__directed_graph.update_cost(1, 4, 14)
        self.assertEqual(self.__directed_graph.get_edges()['cost'][0], 14)
        with self.assertRaises(EdgeError) as err:
            self.__directed_graph.update_cost(1, 7, 13)
        self.assertEqual(str(err.exception), "The edge doesn't exist.")

        with self.assertRaises(VertexError) as ve:
            self.__directed_graph.update_cost(1897, 1975, 15)
        self.assertEqual(str(ve.exception), "A vertex or both don't exist.")

    def test_add_vertex(self):
        self.__directed_graph.add_vertex(1007)
        self.assertEqual(len(self.__directed_graph.vertices()), 1001)
        with self.assertRaises(VertexError) as ve:
            self.__directed_graph.add_vertex(172)
        self.assertEqual(str(ve.exception), "You can't add a vertex that already exists.")

    def test_find_edge_for_2_vertices(self):
        self.__directed_graph.add_edge(1, 4, 10)
        self.__directed_graph.add_edge(7, 9, 13)
        self.assertEqual(self.__directed_graph.find_edge_for_2_vertices(1, 4), 0)
        self.assertEqual(self.__directed_graph.find_edge_for_2_vertices(7, 9), 1)
        self.assertEqual(self.__directed_graph.find_edge_for_2_vertices(13, 243), -1)

    def test_delete_edge(self):
        self.__directed_graph.add_edge(1, 4, 10)
        self.__directed_graph.add_edge(7, 9, 13)
        self.__directed_graph.add_edge(14, 5, 123)
        self.__directed_graph.add_edge(7, 94, 131)
        self.assertEqual(len(self.__directed_graph.get_edges()['cost']), 4)
        self.__directed_graph.delete_edge(7, 9)
        self.assertEqual(len(self.__directed_graph.get_edges()['cost']), 3)
        self.assertEqual(self.__directed_graph.get_edges()['edge'][0][0], 1)
        self.assertEqual(self.__directed_graph.get_edges()['edge'][1][0], 14)
        self.assertEqual(self.__directed_graph.get_edges()['edge'][2][0], 7)
        self.assertEqual(self.__directed_graph.get_edges()['edge'][0][1], 4)
        self.assertEqual(self.__directed_graph.get_edges()['edge'][1][1], 5)
        self.assertEqual(self.__directed_graph.get_edges()['edge'][2][1], 94)
        self.assertEqual(self.__directed_graph.get_edges()['cost'][0], 10)
        self.assertEqual(self.__directed_graph.get_edges()['cost'][1], 123)
        self.assertEqual(self.__directed_graph.get_edges()['cost'][2], 131)
        self.__directed_graph.delete_edge(7, 94)
        with self.assertRaises(EdgeError) as err:
            self.__directed_graph.delete_edge(10, 15)
        self.assertEqual(str(err.exception), "Edge doesn't exist.")

        with self.assertRaises(VertexError) as ve:
            self.__directed_graph.delete_edge(1003, 12410)
        self.assertEqual(str(ve.exception), "One or both the vertices don't exist.")

    def test_delete_vertex(self):
        self.__directed_graph.add_edge(1, 4, 10)
        self.__directed_graph.add_edge(7, 9, 13)
        self.__directed_graph.add_edge(14, 5, 123)
        self.__directed_graph.add_edge(7, 94, 131)
        self.__directed_graph.add_edge(39, 7, 12)
        self.__directed_graph.add_edge(41, 7, 23)
        self.assertEqual(len(self.__directed_graph.get_edges()['cost']), 6)
        self.__directed_graph.delete_vertex(7)
        self.assertEqual(len(self.__directed_graph.get_edges()['cost']), 2)
        self.assertEqual(self.__directed_graph.get_edges()['edge'][0][0], 1)
        self.assertEqual(self.__directed_graph.get_edges()['edge'][1][0], 14)
        self.assertEqual(self.__directed_graph.get_edges()['edge'][0][1], 4)
        self.assertEqual(self.__directed_graph.get_edges()['edge'][1][1], 5)
        self.assertEqual(self.__directed_graph.get_edges()['cost'][0], 10)
        self.assertEqual(self.__directed_graph.get_edges()['cost'][1], 123)
        self.assertEqual(len(self.__directed_graph.vertices()), 999)
        with self.assertRaises(VertexError) as ve:
            self.__directed_graph.delete_vertex(7)
        self.assertEqual(str(ve.exception), "The vertex doesn't exist.")

    def test_out_neighbours(self):
        self.__directed_graph.add_edge(1, 4, 10)
        self.__directed_graph.add_edge(7, 9, 13)
        self.__directed_graph.add_edge(14, 5, 123)
        self.__directed_graph.add_edge(7, 94, 131)
        self.assertEqual(self.__directed_graph.out_neighbours(7), [9, 94])
        with self.assertRaises(VertexError) as ve:
            self.__directed_graph.out_neighbours(1032)
        self.assertEqual(str(ve.exception), "The vertex doesn't exist.")

    def test_in_neighbours(self):
        self.__directed_graph.add_edge(1, 4, 10)
        self.__directed_graph.add_edge(7, 9, 13)
        self.__directed_graph.add_edge(14, 5, 123)
        self.__directed_graph.add_edge(7, 94, 131)
        self.__directed_graph.add_edge(13, 4, 1231)
        self.assertEqual(self.__directed_graph.in_neighbours(4), [1, 13])
        with self.assertRaises(VertexError) as ve:
            self.__directed_graph.in_neighbours(1032)
        self.assertEqual(str(ve.exception), "The vertex doesn't exist.")

    def test_isolated_vertex(self):
        self.__directed_graph.add_edge(1, 4, 10)
        self.__directed_graph.add_edge(7, 9, 13)
        self.__directed_graph.add_edge(14, 5, 123)
        self.__directed_graph.add_edge(7, 94, 131)
        self.__directed_graph.add_edge(13, 4, 1231)
        self.assertEqual(self.__directed_graph.isolated_vertex(132), True)
        self.assertEqual(self.__directed_graph.isolated_vertex(14), False)
        with self.assertRaises(VertexError) as ve:
            self.__directed_graph.isolated_vertex(1023)
        self.assertEqual(str(ve.exception), "The vertex doesn't exist.")

    def test_find_all_the_isolated_vertices(self):
        new_graph = DirectedGraph(range(5))
        new_graph.add_edge(1, 4, 10)
        new_graph.add_edge(1, 3, 15)
        self.assertEqual(new_graph.find_all_the_isolated_vertices(), [0,2])
