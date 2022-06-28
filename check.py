def fibonacci(n):
    if(n in [0,1]):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
def sumOfDigits(n):
    if(n==0):
        return n
    else:
        return n%10+sumOfDigits(n//10)

def power(base,exp):
    if(base==1):
        return 1
    if(exp==1):
        return base
    else:
        return base*power(base,exp-1)
    
def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

def decToBin(n):
    if(n in [0,1]):
        return n
    return (n%2)+10*decToBin(n//2)
    
def flatten(arr):
    ans = []
    for i in arr:
        if(type(i) is list):
            ans.extend(flatten(i))
        else:
            ans.append(i)
    return ans

def prod(arr):
    if(len(arr)==1):
        return arr[0]
    else:
        return arr[0]*prod(arr[1:])
def palindrome(string):
    if(len(string)==1):
        return True
    if(string[0]!=string[-1]):
        return False
    else:
        return palindrome(string[1:-1])


"""Given a string array words, return the maximum
 value of length(word[i]) * length(word[j]) where 
 the two words do not share common letters. If no 
 such two words exist, return 0"""
 
from itertools import combinations
from re import S


def maxProduct(words):
    d = {}
    for w in words:
        mask = 0
        for c in set(w):
            mask |= (1 << (ord(c) - 97))
        d[mask] = max(d.get(mask, 0), len(w))
    return max([d[x] * d[y] for x, y in combinations(d.keys(), 2) if not x & y] or [0])


