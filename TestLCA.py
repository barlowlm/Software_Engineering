import unittest
import LCA

class TestLCA(unittest.TestCase):
        
	def test_lca(self):
                root = LCA.Node(20) 
                root.left = LCA.Node(8) 
                root.right = LCA.Node(22) 
                root.left.left = LCA.Node(4) 
                root.left.right = LCA.Node(12) 
                root.left.right.left = LCA.Node(10) 
                root.left.right.right = LCA.Node(14)
                n1 = 10 ; n2 = 14
                t = LCA.lca(root, n1, n2) 
                print "LCA of %d and %d is %d" %(n1, n2, t.data) 
                self.assertEqual(LCA.lca(root, n1, n2).data, 12)
                
                n1 = 14 ; n2 = 8
                t = LCA.lca(root, n1, n2) 
                print "LCA of %d and %d is %d" %(n1, n2 , t.data)  
                self.assertEqual(LCA.lca(root, n1, n2),t)
                
                n1 = 10 ; n2 = 22
                t = LCA.lca(root, n1, n2) 
                print "LCA of %d and %d is %d" %(n1, n2, t.data) 
                self.assertEqual(LCA.lca(root, n1, n2),t)

if __name__=="__main__":
        unittest.main()