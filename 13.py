class Solution(object):
    def romanToInt(self, s):
        rules = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = 0

        for i in range(len(s)):
            if i + 1 < len(s) and rules[s[i]] < rules[s[i+1]]:
                total -= rules[s[i]]
            else:
                total += rules[s[i]]

        return total
