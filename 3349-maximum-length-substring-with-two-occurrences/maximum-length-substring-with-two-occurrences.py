class Solution:
    def maximumLengthSubstring(self,s:str)->int:
        frequency={}
        left=0
        answer=0
        for right in range(len(s)):
            frequency[s[right]]=frequency.get(s[right],0)+1
            while frequency[s[right]]>2:
                frequency[s[left]]-=1
                left+=1
            answer=max(answer,right-left+1)
        return answer