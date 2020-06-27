l = eval(input("Enter a list: "))
dup = []
for i in l:
    if "".join(sorted(i)) not in dup:
        dup.append("".join(sorted(i)))
anagrams= []
for i in range(len(dup)):
    anagrams.append([])
    for ele in l:
        if "".join(sorted(ele)) == dup[i]:
            anagrams[i].append(ele)
    print(anagrams[i])
