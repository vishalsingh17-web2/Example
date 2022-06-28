def isUnique(s):
    check = 0
    for i in s:
        
        val = ord(i) - ord("a")
        print(val)
        if((check&(1<<val))>0):
            return False
        check |= 1<<val
    return True
# print(isUnique("vishal"))

def lengthOfLongestSubstring(s):
        m = 0
        count = 0
        check = 0
        i=0
        while(i<len(s)):
            val = ord(s[i]) - ord('a')
            if(check&(1<<val)==0):
                count+=1
                if(count>m):
                    print(count)
                    m = count
                check|=(1<<val)
                
            else:
                i-=1
                check = 0
                count = 0
            i+=1
            
        return m
# print(lengthOfLongestSubstring("dvdf"))
def fun(x):
    if(x==1):
        return 1
    if(x>0):
        return x * fun(x-1)
    
# print(fun(5))
def sumOfDigits(x):
    if(x<10):
        return x
    return sumOfDigits(x//10)+x%10
# print(sumOfDigits(12343486593486583746587364857638456))

def reverseNumber(n):
    if(n<10):
        return n
    return n%10*10**(len(str(n))-1) + reverseNumber(n//10)

c = 0
def counter(n,k):
    global c
    if(n//10==0):
        return n
    if(n%10==k):
        c+=1
    counter(n//10,k)
    
counter(10020203302,3)
print(c)


            
    