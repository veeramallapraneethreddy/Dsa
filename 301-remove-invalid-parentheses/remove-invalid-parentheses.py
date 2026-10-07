class Solution:
    def removeInvalidParentheses(self,s):
        result=[]
        def backtrack(index,path,left,right,remove_left,remove_right):
            if index==len(s):
                if left==right and remove_left==0 and remove_right==0:
                    result.append(''.join(path))
                return
            if s[index]=='(':
                if remove_left>0:
                    backtrack(index+1,path,left,right,remove_left-1,remove_right)
                path.append('(')
                backtrack(index+1,path,left+1,right,remove_left,remove_right)
                path.pop()
            elif s[index]==')':
                if remove_right>0:
                    backtrack(index+1,path,left,right,remove_left,remove_right-1)
                if left>right:
                    path.append(')')
                    backtrack(index+1,path,left,right+1,remove_left,remove_right)
                    path.pop()
            else:
                path.append(s[index])
                backtrack(index+1,path,left,right,remove_left,remove_right)
                path.pop()
        left=0
        right=0
        for ch in s:
            if ch=='(':
                left+=1
            elif ch==')':
                if left>0:
                    left-=1
                else:
                    right+=1
        backtrack(0,[],0,0,left,right)
        return list(set(result))