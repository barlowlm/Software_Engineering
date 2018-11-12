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
                #print "LCA of %d and %d is %d" %(n1, n2, t.data) 
                self.assertEqual(LCA.lca(root, n1, n2).data, 12)
                
                n1 = 14 ; n2 = 8
                t = LCA.lca(root, n1, n2) 
                #print "LCA of %d and %d is %d" %(n1, n2 , t.data)  
                self.assertEqual(LCA.lca(root, n1, n2),t)
                
                n1 = 10 ; n2 = 22
                t = LCA.lca(root, n1, n2) 
                #print "LCA of %d and %d is %d" %(n1, n2, t.data) 
                self.assertEqual(LCA.lca(root, n1, n2),t)
                
                #testLCA_DAG
                graph = {'1': ['2', '5', '3'],
                '3': ['5', '6','7'],
                '2': ['4']}

                path = []
                
                graph2 = {1: [2, 5, 3],
                3: [5, 6,7],
                2: [4]}

                #Test 1: LCA 2-3
                self.assertEqual(LCA.findLCA(graph,'1', '2', '3', path), '1')

                #Test 2: LCA 4-5
                self.assertEqual(LCA.findLCA(graph,'1', '4', '5',path), '1')

                #Test 3: LCA 5-6
                self.assertEqual(LCA.findLCA(graph2,1, 5, 6,path), 3)

                #Test 4: LCA 1-7
                self.assertEqual(LCA.findLCA(graph2,1, 1, 7,path), 1)

                graph={'G':['D','F'],
                'D': ['C'],
                'C': ['B'],
                'B':['A'],
                'F':['F'],
                'F':['E'],
                'E':['B']}

                 #Test 5: LCA G-G
                self.assertEqual(LCA.findLCA(graph,'G', 'G', 'G',[]), 'G')

                #Test 6: LCA G-C
                self.assertEqual(LCA.findLCA(graph,'G', 'G', 'C',[]), 'G')

                #Test 7: LCA G-C
                self.assertEqual(LCA.findLCA(graph,'G', 'C', 'E',[]), 'G')

                #Test 8: LCA G-C
                self.assertEqual(LCA.findLCA(graph,'G', 'A', 'B',[]), 'B')

        def test_pathTo(self):
                graph2 = {1: [2, 5, 3],
                3: [5, 6,7],
                2: [4]}

                #Test 1: test all values equal None
                self.assertEqual(LCA.find_all_paths(graph2, None, 0, []), [])

                #Test 2: test path to root
                print(LCA.find_all_paths(graph2, 1, 1))
                self.assertEqual(LCA.find_all_paths(graph2, 1, 1), [[1]])


                #Test 3: test for key not in tree
                self.assertEqual(LCA.find_all_paths(graph2, 1, 50), [])

                #Test 4: path to 4
                graph2 = {1: [2, 3],
                2: [4, 5],
                2: [6,7]}

                self.assertEqual(LCA.find_all_paths(graph2, 1, 4), [])

                #Test 5: path to 6
                self.assertEqual(LCA.find_all_paths(graph2, 1, 6), [[1, 2, 6]])
        
                #Test 6: path to 3
                self.assertEqual(LCA.find_all_paths(graph2, 1, 3), [[1, 3]])

                #Test 7: path to 2
                self.assertEqual(LCA.find_all_paths(graph2, 1, 2), [[1, 2]])

        def test_pathsTo(self):
                graph = {'A': ['B', 'C'],
                'B': ['C', 'D'],
                'C': ['D'],
                'D': ['C'],
                'E': ['F'],
                'F': ['C']}

                #Test 1: test all values equal None
                self.assertEqual(LCA.find_all_paths(graph, '', None), [])

                #Test 2: test path to root
                root = LCA.Node(1)
                self.assertEqual(LCA.find_all_paths(graph, 1, 1), [[1]])

                #Test 3: test for key not in tree
                self.assertEqual(LCA.find_all_paths(graph, 1, 50), [])

                #Test 4: paths to A-D
                self.assertEqual(LCA.find_all_paths(graph, 'A', 'D'), [['A', 'B', 'C', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']])

if __name__=="__main__":
        unittest.main()