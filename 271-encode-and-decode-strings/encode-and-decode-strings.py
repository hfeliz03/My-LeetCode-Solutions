class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""
        for i, string in enumerate(strs):
            encoded += string
            encoded += "\\\\\\encoder\\\\\\" if i < len(strs)-1 else ""
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split("\\\\\\encoder\\\\\\")
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))