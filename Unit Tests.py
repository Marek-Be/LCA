import unittest
import LCA

LCA.graph.update({'A': ['B', 'C']})
LCA.graph.update({'B': ['C', 'D']})
LCA.graph.update({'C': ['D']})
LCA.graph.update({'D': ['C']})
LCA.graph.update({'E': ['F']})
LCA.graph.update({'F': ['C']})

list1 = [1,2,3,6,10]
list2 = [10,501,628,723]

class TestLCA(unittest.TestCase):
    def test_LCA_normal(self):
        self.assertEqual("A", LCA.LCA(LCA.graph, "A", "B"))
        self.assertEqual("B", LCA.LCA(LCA.graph, "C", "D"))
    def test_LCA_invalidValue(self):
        self.assertEqual("", LCA.LCA(LCA.graph, "Z", "X"))
    def test_LCA_sameValue(self):
        self.assertEqual("A", LCA.LCA(LCA.graph, "A", "A"))
        self.assertEqual("D", LCA.LCA(LCA.graph, "D", "D"))
    def test_checkTwoLists_normal(self):
        self.assertEqual(10, LCA.checkTwoLists(list1,list2))
    def test_checkTwoLists_empty(self):
        self.assertEqual("", LCA.checkTwoLists([],[]))
if __name__ == '__main__':
    unittest.main()
