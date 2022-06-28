def permutations(p,s):
    if(s==""):
        return [p]
    ans = []
    for i in range(len(s)):
        ans+=permutations(p+s[i],s[:i]+s[i+1:])
    return ans
permutations("","abc")
