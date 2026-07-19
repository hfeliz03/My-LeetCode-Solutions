class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_position = {}
        for i, char in enumerate(s): last_position[char] = i
        stack = []
        used = set()

        for i, char in enumerate(s):
            if char in used: continue
            while (
                stack
                and char < stack[-1]
                and last_position[stack[-1]] > i
            ):
                removed = stack.pop()
                used.remove(removed)
            stack.append(char)
            used.add(char)
        return "".join(stack)