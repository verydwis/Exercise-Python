class Solution(object):
    def isValid(s):
        for i in range(len(s)):
            s =s.replace('{}','').replace('[]','').replace('()','')
        return s ==''
s = "()"

print("isValid:",Solution.isValid(s))