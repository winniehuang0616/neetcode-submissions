class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"(":1, "[":2, "{":3, "}":-3, "]":-2, ")":-1}
        box = []
        for i in range(len(s)):
            if mapping[s[i]] > 0: 
                box.append(mapping[s[i]])
            else: 
                if len(box) == 0: return False
                item = box[-1]
                if item + mapping[s[i]] != 0: return False
                else: box.pop()
        if len(box) == 0: return True
        else: return False