class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge = {key: val for key, val in knowledge}
        s = s.split(")")
        res = ""
        print(s)
        for substr in s:
            for i, char in enumerate(substr):
                if char != "(": res += char
                else: 
                    key = substr[i+1:]
                    res += knowledge[key] if key in knowledge else "?"
                    break
        return res
