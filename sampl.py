from collections import Counter

s1=["hello","hi","lani"]
s2=["hello",'hey','lani']
s3=[]
for s1,s2 in zip(s1,s2):
    if len(s1) != len(s2):
        s3.append("No")
        continue
    s=Counter(s1)
    t=Counter(s2)
    temp='yes'
    for i in s:
        if s[i] != t.get(i,0):
            temp= 'No'
            break
    s3.append(temp)

print(s3)

    