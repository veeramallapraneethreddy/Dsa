class Solution:
    def sumGame(self,num):
        n=len(num)//2
        left=sum(int(x) for x in num[:n] if x!='?')
        right=sum(int(x) for x in num[n:] if x!='?')
        left_question=num[:n].count('?')
        right_question=num[n:].count('?')
        if (left_question+right_question)%2:
            return True
        return left-right!=9*(right_question-left_question)//2