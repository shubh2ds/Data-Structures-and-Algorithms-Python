s = "aabacbebebe"
k = 3 # 3 unique chars
# OP: 7

i = j = 0
longest  = 0
count = {}

while j < len(s):

    if s[j] not in count:
        count[s[j]] = 1
    else:
        count[s[j]] = count[s[j]] + 1
    
    if len(count) < k:
        j = j + 1

    elif len(count) == k:
        longest = max(j-i+1 , longest)
        j = j+1

    elif len(count) > k:
        while len(count) > k:
            count[s[i]] = count[s[i]] - 1
            if count[s[i]] == 0:
                count.pop(s[i])
            i = i + 1
        j = j + 1
print(longest)
    
