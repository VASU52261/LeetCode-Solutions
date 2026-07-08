

class Solution(object):
    def postorder(self, root):
        res = []
        def func(node):
            if not node:
               return
            for c in node.children:
               func(c)
            res.append(node.val)
        func(root)
        return res
        