standardGroup = ['a','e','i','o','u','A','E','I','O','U']

while(1):
    sentPerLine = input().split()
    count=0
    if (sentPerLine[-1] == "#"):
        break
    else:
        for sent in sentPerLine:
            for alp in sent:
                for standard in standardGroup:
                    if(alp == standard):
                        count+=1
                        break
                    else:
                        continue
    print(count)
