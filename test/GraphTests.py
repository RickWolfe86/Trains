import unittest
from lib.Graph import Graph

class GraphTests(unittest. TestCase):

    def setUp(self):
        self.list_routes = "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"

    def test_output_1(self):
        # The distance of the route A-D.
        graph_routesAC = Graph()
        graph_routesAC.build_graph(self.list_routes)
        graph_routesAC.path_list = graph_routesAC.build_path_list('A', 'C')
        value = graph_routesAC.find_path_size(["A", "B", "C"])

        self.assertEqual(9, value)

    def test_output_2(self):
        # The distance of the route A-B-C.
        graph_routesAD = Graph()
        graph_routesAD.build_graph(self.list_routes)
        graph_routesAD.path_list = graph_routesAD.build_path_list('A', 'D')
        value = graph_routesAD.find_path_size(["A", "D"])

        self.assertEqual(5, value)

    def test_output_3(self):
        # The distance of the route A-D-C.
        graph_routesAC = Graph()
        graph_routesAC.build_graph(self.list_routes)
        graph_routesAC.path_list = graph_routesAC.build_path_list('A', 'C')
        value = graph_routesAC.find_path_size(["A", "D", "C"])

        self.assertEqual(13, value)

    def test_output_4(self):
        # The distance of the route A-E-B-C-D.
        graph_routesAD = Graph()
        graph_routesAD.build_graph(self.list_routes)
        graph_routesAD.path_list = graph_routesAD.build_path_list('A', 'D')
        value = graph_routesAD.find_path_size(["A", "E", "B", "C", "D"])

        self.assertEqual(22, value)

    def test_output_5(self):
        # The distance of the route A-E-D.
        graph_routesAD = Graph()
        graph_routesAD.build_graph(self.list_routes)
        graph_routesAD.path_list = graph_routesAD.build_path_list('A', 'D')
        value = graph_routesAD.find_path_size(["A", "E", "D"])

        self.assertEqual('NO SUCH ROUTE', value)

    def test_output_6(self):
        # The number of trips starting at C and ending at C with a maximum of 3 stops.  In the sample data below,
        # there are two such trips: C-D-C (2 stops). and C-E-B-C (3 stops).
        graph_routesCC3 = Graph()
        graph_routesCC3.build_graph(self.list_routes)
        graph_routesCC3.path_list = graph_routesCC3.build_path_list('C', 'C', max_path_stop=3)
        value = len(graph_routesCC3.path_list)

        self.assertEqual(2, value)

    def test_output_7(self):
        # The number of trips starting at A and ending at C with exactly 4 stops.  In the sample data below,
        # there are three such trips: A to C (via B,C,D); A to C (via D,C,D); and A to C (via D,E,B).
        graph_routesAC4 = Graph()
        graph_routesAC4.build_graph(self.list_routes)
        graph_routesAC4.path_list = graph_routesAC4.build_path_list('A', 'C', path_stop=4)
        value = len(graph_routesAC4.path_list)

        self.assertEqual(3, value)

    def test_output_8(self):
        # The length of the shortest route (in terms of distance to travel) from A to C.
        graph_routesAC = Graph()
        graph_routesAC.build_graph(self.list_routes)
        graph_routesAC.path_list = graph_routesAC.build_path_list('A', 'C')
        value = graph_routesAC.shortest_path()

        self.assertEqual(9, value)

    def test_output_9(self):
        # The length of the shortest route (in terms of distance to travel) from B to B.
        graph_routesBB = Graph()
        graph_routesBB.build_graph(self.list_routes)
        graph_routesBB.path_list = graph_routesBB.build_path_list('B', 'B')
        value = graph_routesBB.shortest_path()

        self.assertEqual(9, value)

    def test_output_10(self):
        # The number of different routes from C to C with a distance of less than 30.  In the sample data, the trips
        # are: CDC, CEBC, CEBCDC, CDCEBC, CDEBC, CEBCEBC, CEBCEBCEBC.
        graph_routesCC = Graph()
        graph_routesCC.build_graph(self.list_routes)
        graph_routesCC.path_list = graph_routesCC.build_path_list('C', 'C', max_distance=30)
        value = graph_routesCC.number_routes()

        self.assertEqual(7, value)

    if __name__ == '__main__':
        unittest.main()
