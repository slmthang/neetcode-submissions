class Solution:
    def encode(self, strs: list[str]) -> str:
        # Avoid repeated string copies with list join
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Locate the next delimiter
            j = s.find('#', i)
            length = int(s[i:j])
            
            # Slice the exact string using the parsed length
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Advance pointer past this chunk
            i = end
            
        return res