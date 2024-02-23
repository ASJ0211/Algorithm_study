str = input()
s=str.lower()
b=str.upper()
c=0
r=[]
for i in str:
    if i == s[c]:
        r.append(b[c])
    else:
        r.append(s[c])
    c+=1
r=''.join(r)
print(r)