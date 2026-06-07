class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parentVal, childVal, isLeft in descriptions:
            if parentVal not in nodes:
                nodes[parentVal] = TreeNode(parentVal)

            if childVal not in nodes:
                nodes[childVal] = TreeNode(childVal)

            parentNode = nodes[parentVal]
            childNode = nodes[childVal]

            if isLeft == 1:
                parentNode.left = childNode
            else:
                parentNode.right = childNode

            children.add(childVal)

        for val in nodes:
            if val not in children:
                return nodes[val]