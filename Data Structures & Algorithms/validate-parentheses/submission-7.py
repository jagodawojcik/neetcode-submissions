class Solution:
    def isValid(self, s: str) -> bool:

        bracket_lookup = {'(' : ')', '[' : ']', '{' : '}'}

        bracket_store = []

        for b in s:
            if b in bracket_lookup:
                bracket_store.append(b)
            else:
                if not bracket_store:
                    return False
                if bracket_lookup[bracket_store[-1]] != b:
                    return False
                bracket_store.pop()

        return False if bracket_store else True


