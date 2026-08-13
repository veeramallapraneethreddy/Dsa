class Solution:
    def longestRepeating(self,s,queryCharacters,queryIndices):
        n=len(s)
        tree=[None]*(4*n)
        def build(node,left,right):
            if left==right:
                tree[node]=(s[left],s[left],1,1,1)
                return
            middle=(left+right)//2
            build(node*2,left,middle)
            build(node*2+1,middle+1,right)
            merge(node)
        def merge(node):
            a=tree[node*2]
            b=tree[node*2+1]
            left_char,left_end,left_prefix,left_suffix,left_best=a
            right_char,right_end,right_prefix,right_suffix,right_best=b
            length=left_node_length[node*2]
            right_length=left_node_length[node*2+1]
            prefix=left_prefix
            suffix=right_suffix
            best=max(left_best,right_best)
            if left_end==right_char:
                best=max(best,left_suffix+right_prefix)
                if left_prefix==length:
                    prefix=length+right_prefix
                if right_suffix==right_length:
                    suffix=right_length+left_suffix
            tree[node]=(left_char,right_end,prefix,suffix,best)
        def update(node,left,right,index,character):
            if left==right:
                tree[node]=(character,character,1,1,1)
                return
            middle=(left+right)//2
            if index<=middle:
                update(node*2,left,middle,index,character)
            else:
                update(node*2+1,middle+1,right,index,character)
            merge(node)
        left_node_length=[0]*(4*n)
        def set_length(node,left,right):
            left_node_length[node]=right-left+1
            if left<right:
                middle=(left+right)//2
                set_length(node*2,left,middle)
                set_length(node*2+1,middle+1,right)
        set_length(1,0,n-1)
        build(1,0,n-1)
        answer=[]
        for i in range(len(queryCharacters)):
            update(1,0,n-1,queryIndices[i],queryCharacters[i])
            answer.append(tree[1][4])
        return answer