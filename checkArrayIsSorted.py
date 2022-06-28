def sorted(arr):
    assert len(arr)!=0
    
    if(len(arr) in [0,1]):
        return True
    return arr[0]<arr[1] and sorted(arr[1:])
# print(sorted([1]))

def linearSearch(arr,k, index):
    if(index==len(arr)):
        return []
    elif(arr[index]==k):
        return [index] + linearSearch(arr,k,index+1)
    return linearSearch(arr,k,index+1)
    
# print(linearSearch([1,2,3,6,8,5,4,3,3,6,7,81,1,1,1,1,1,1,1],1,0))

def reverseList(arr,index,start,end,ans):
    if(index==len(arr) or index==end):
        return
    elif(index>=start and index<end):
        reverseList(arr,index+1,start,end,ans)
        ans.append(arr[index])
    else:
        ans.append(arr[index])
        reverseList(arr,index+1,start,end,ans)
       
        
    
# ans = []
# reverseList([1,2,3,4,5,6,7,8,9,0],0,2,7,ans)
# print(ans)

def elementJustGreater(arr, start,end, target):
    if(start<=end):
        mid = start+(end-start)//2
        if(arr[mid]==target):
            if(mid+1<len(arr)):
                return arr[mid+1]
            else:
                return -1
        elif(arr[mid]>target):
            return elementJustGreater(arr,start,mid-1,target)
        else:
            return elementJustGreater(arr,mid+1,end,target)
    else:
        if(start<len(arr)):
            return arr[start]
        else:
            return -1
# print(elementJustGreater([1,4,5,6,7,8,10],0,7,1))

def patternOne(x):
    print(x*"* ")
    if(x>1):
        patternOne(x-1)
    print(x*"* ")
# patternOne(5)

def removeElementFromString(s,e):
    if(s==""):
        return s
    elif(s[0:len(e)]==e):
        return removeElementFromString(s[len(e):],e)
    else:
        return s[0] + removeElementFromString(s[1:],e)
# print(removeElementFromString("Viaashaaaal","sh"))

def subsets(p,s):
    if(s==""):
        return [p]
    return subsets(p+s[0],s[1:])+subsets(p,s[1:])
    

# print(subsets("","abc"))
def permutation(p,s):
    if(s==[]):
        return [p]
    ans = []
    for i in range(len(s)):
        ans += permutation(p+[s[i]],s[0:i]+s[i+1:])
    return ans
# print(permutation([],[1,1,3]))

#  Letter Combinations of a Phone Number
ans = []
def helper(p,s,target,res):
        if(p==target):
            return [res];
        elif(p>target):
            return []
        for i in range(len(s)):
            ans.append(helper(p+s[i],s,target,res+[p+s[i]]))

        return ans

# print(helper(0,[2,3,6,7],7,[]))

def escape(p,x,y,n):
    if(x+1==n or y+1==n):
        if(x+1==n):
            return [p+"R"]
        else:
            return [p+"D"]
    ans= []
    
    ans+=escape(p+"R",x+1,y,n)+escape(p+"D",x,y+1,n)+escape(p+"d",x+1,y+1,n)
    return ans
    
# print(escape("",0,0,5))

class Solution:
    def isEscapePossible(self, blocked, source, target) -> bool:
        if(len(blocked)==0):
            return True
        elif(source in blocked):
            return False
        elif(source[0]<0 or source[1]<0):
            return False
        elif(source==target):
            return True
        elif(source[0]==target[0]):
            return self.isEscapePossible(blocked,[source[0],source[1]+1],target) or self.isEscapePossible(blocked,[source[0],source[1]-1],target)
        elif(source[1]==target[1]):
            return self.isEscapePossible(blocked,[source[0]+1,source[1]],target) or self.isEscapePossible(blocked,[source[0]-1,source[1]],target)
        
        return self.isEscapePossible(blocked,[source[0]+1,source[1]],target) or self.isEscapePossible(blocked,[source[0],source[1]+1],target) or self.isEscapePossible(blocked,[source[0]-1,source[1]],target) or self.isEscapePossible(blocked,[source[0],source[1]-1],target)
    
print(Solution().isEscapePossible([[0,1],[1,0],[1,1],[1,2]],[2,0],[5,5]))