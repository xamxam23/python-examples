def perm(p,s):
    n = len(s)
    if n==0:
        print p
    else:
        for i in range(0,n):
            perm(p+s[i], s[0:i]+s[i+1:n]);
perm("","abc")
