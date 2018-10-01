import unittest
import LCA

a = root = LCA.Node(1)
root.left = LCA.Node(2)
root.right = LCA.Node(3)
root.left.left = LCA.Node(4)
root.right.left = LCA.Node(5)
root.right.right = LCA.Node(6)

class TestLCA(unittest.TestCase):
    def test_LCA_normal(self):
        self.assertEqual(3, LCA.LCA(a, 5, 6))
        self.assertEqual(1, LCA.LCA(a, 2, 6))
    def test_LCA_invalidValue(self):
        self.assertEqual(None, LCA.LCA(a, 10, 6))
        self.assertEqual(None, LCA.LCA(a, None, 6))
    def test_LCA_sameValue(self):
        self.assertEqual(6, LCA.LCA(a, 6, 6))
        self.assertEqual(3, LCA.LCA(a, 3, 3))
    def test_contains_normal(self):
        self.assertEqual(True,LCA.contains(a, 5))
        self.assertEqual(True,LCA.contains(a, 2))
    def test_contains_invalidValue(self):
        self.assertEqual(False,LCA.contains(a, -5))
        self.assertEqual(False,LCA.contains(a, 10))
    def test_contains_None(self):
        self.assertEqual(False,LCA.contains(a, None))

if __name__ == '__main__':
    unittest.main()
