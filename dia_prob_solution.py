s = input()
l = len(s)
i = 0
st = ""
while (i < l-1):
    if (s[i] != s[i+1]):
        st = st + s[i]
        i = i+1
        continue
    else:
        c = 1
        j= i
        while((j < l-1) and (s[j] == s[j+1])):
            c = c+1
            j= j+1
        st = st + s[j] + str(c)
        i = j+1
if (i != l):
    st = st + s[l-1]
print(st)
