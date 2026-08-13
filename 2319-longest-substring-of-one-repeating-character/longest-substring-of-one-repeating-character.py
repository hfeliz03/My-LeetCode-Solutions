#Segment tree, crazy problem
class Node:
    def __init__(self, length=0, prefix=0, suffix=0, best=0,
                 left_char="", right_char=""):
        self.length = length
        self.prefix = prefix
        self.suffix = suffix
        self.best = best
        self.left_char = left_char
        self.right_char = right_char


class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: list[int]
    ) -> list[int]:

        s = list(s)
        n = len(s)

        tree = [Node() for _ in range(4 * n)]

        def merge(left, right):
            node = Node()

            node.length = left.length + right.length

            node.left_char = left.left_char
            node.right_char = right.right_char

            # Initially these cannot cross the boundary
            node.prefix = left.prefix
            node.suffix = right.suffix

            node.best = max(left.best, right.best)

            # Can the runs connect across the middle?
            if left.right_char == right.left_char:

                # A repeating substring crosses the boundary
                node.best = max(
                    node.best,
                    left.suffix + right.prefix
                )

                # Entire left side is one character,
                # so the prefix can continue into the right side
                if left.prefix == left.length:
                    node.prefix = left.length + right.prefix

                # Entire right side is one character,
                # so the suffix can continue into the left side
                if right.suffix == right.length:
                    node.suffix = right.length + left.suffix
            return node

        def build(index, l, r):
            # Leaf node
            if l == r:
                tree[index] = Node(
                    length=1,
                    prefix=1,
                    suffix=1,
                    best=1,
                    left_char=s[l],
                    right_char=s[l]
                )
                return

            mid = (l + r) // 2

            build(index * 2, l, mid)
            build(index * 2 + 1, mid + 1, r)

            tree[index] = merge(
                tree[index * 2],
                tree[index * 2 + 1]
            )

        def update(index, l, r, position, char):
            if l == r:
                s[position] = char
                tree[index] = Node(
                    length=1,
                    prefix=1,
                    suffix=1,
                    best=1,
                    left_char=char,
                    right_char=char
                )
                return

            mid = (l + r) // 2

            if position <= mid:
                update(
                    index * 2,
                    l,
                    mid,
                    position,
                    char
                )
            else:
                update(
                    index * 2 + 1,
                    mid + 1,
                    r,
                    position,
                    char
                )

            tree[index] = merge(
                tree[index * 2],
                tree[index * 2 + 1]
            )
        build(1, 0, n - 1)
        answer = []

        for position, char in zip(
            queryIndices,
            queryCharacters
        ):
            update(
                1,
                0,
                n - 1,
                position,
                char
            )
            answer.append(tree[1].best)

        return answer