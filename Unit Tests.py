import unittest
import LCA

LCA.graph.update({'A': ['B', 'C']})
LCA.graph.update({'B': ['C', 'D']})
LCA.graph.update({'C': ['D']})
LCA.graph.update({'D': ['C']})
LCA.graph.update({'E': ['F']})
LCA.graph.update({'F': ['C']})

class TestLCA(unittest.TestCase):

if __name__ == '__main__':
    unittest.main()
