

class Solution(object):
    def preorder(self, root): 
        res = []
        def func(node):
            if not node:
               return
            res.append(node.val)
            for c in node.children:
                func(c)
        func(root)
        return res

     
