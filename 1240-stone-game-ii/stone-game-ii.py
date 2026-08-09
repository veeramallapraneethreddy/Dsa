class Solution:
    def stoneGameII(self,piles):
        n=len(piles)
        suffix=[0]*(n+1)
        for i in range(n-1,-1,-1):
            suffix[i]=suffix[i+1]+piles[i]
        dp={}
        def solve(index,m):
            if index>=n:
                return 0
            if (index,m) in dp:
                return dp[(index,m)]
            best=0
            for x in range(1,2*m+1):
                if index+x>n:
                    break
                opponent=solve(index+x,max(m,x))
                current=suffix[index]-opponent
                best=max(best,current)
            dp[(index,m)]=best
            return best
        return solve(0,1)