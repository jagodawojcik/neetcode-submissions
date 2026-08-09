class Solution:
    def isValid(self, s: str) -> bool:

        bracket_lookup = {'(' : ')', '[' : ']', '{' : '}'}

        bracket_store = []

        for b in s[::-1]:
            if b in bracket_lookup:
                if not bracket_store:
                    return False
                closing_bracket = bracket_store.pop()
                if bracket_lookup[b] != closing_bracket:
                    return False
            else:
                bracket_store.append(b)

        return False if bracket_store else True


