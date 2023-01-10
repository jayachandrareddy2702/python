class Solution(object):
    def generateparenthesis(self, n):
        result = []
        self.generateParenthesisUtil(n,n,'',result)
        return result
    def generateParenthesisUtil(self, left,right,temp,result):
        if left == 0 and right == 0:
            result.append(temp)
            return
        if left>0:
            self.generateParenthesisUtil(left-1,right,temp+'(',result)
        if right > left:
            self.generateParenthesisUtil(left, right-1, temp+ ')',result)
ob = Solution()
print(ob.generateparenthesis(4))
