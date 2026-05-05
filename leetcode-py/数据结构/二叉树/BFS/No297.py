from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        dq = deque([root])
        res = []
        while dq:
            node = dq.popleft()
            if node:
                res.append(str(node.val))
                dq.append(node.left)
                dq.append(node.right)
            else:
                res.append("null")
        return '[' + ",".join(res) + ']'
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return 
        li = data[1:-1].split(',')
        root = TreeNode(int(li[0]))
        dq = deque([root])
        i = 1
        while dq:
            node = dq.popleft()
            if li[i] != "null":
                node.left = TreeNode(int(li[i]))
                dq.append(node.left)
            i += 1
            if li[i] != 'null':
                node.right = TreeNode(int(li[i]))
                dq.append(node.right)
            i += 1
        return root