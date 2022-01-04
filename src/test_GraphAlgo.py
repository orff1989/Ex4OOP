from unittest import TestCase

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        g = DiGraph()
        ga = GraphAlgo()
        ga.graph = g
        ga.load_from_json('../data/A3.json')
        newG= ga.get_graph()
        self.assertEqual(g,newG)

    def test_load_from_json(self):
        g = DiGraph()
        ga = GraphAlgo()
        ga.graph = g
        self.assertTrue(ga.load_from_json('../data/A5.json'))


    def test_save_to_json(self):
        g = DiGraph()
        ga = GraphAlgo()
        ga.graph = g
        ga.load_from_json('../data/A3.json')
        self.assertTrue(ga.save_to_json('A3Test.json'))

    def test_shortest_path(self):
        g = DiGraph()
        ga = GraphAlgo()
        ga.graph = g
        ga.load_from_json('../data/A3.json')

        str = ga.shortest_path(0,5)
        self.assertEqual(str.__str__(), "(6.323938666501508, [0, 5])")

    def test_tsp(self):
        g = DiGraph()
        ga = GraphAlgo()
        ga.graph = g
        ga.load_from_json('../data/A1.json')

        str = ga.TSP([1,4,5,8])
        self.assertEqual(str.__str__(), "([0, 1, 2, 3, 4, 5, 6, 7, 8], 10.836570761834288)")

    def test_center_point(self):
        g = DiGraph()
        ga = GraphAlgo()
        ga.graph = g
        ga.load_from_json('../data/A1.json')

        str = ga.centerPoint()
        self.assertEqual(str.__str__(), "(8, 9.925289024973141)")

