class Solution:
    def validSequence(self,word1,word2):
        n=len(word1)
        m=len(word2)
        suffix=[0]*n
        j=m-1
        for i in range(n-1,-1,-1):
            if j>=0 and word1[i]==word2[j]:
                j-=1
            suffix[i]=m-1-j
        answer=[]
        index=0
        changed=False
        for j in range(m):
            while index<n:
                if word1[index]==word2[j]:
                    answer.append(index)
                    index+=1
                    break
                if not changed and (index+1<n and suffix[index+1]>=m-j-1):
                    answer.append(index)
                    index+=1
                    changed=True
                    break
                index+=1
            else:
                return []
        return answer