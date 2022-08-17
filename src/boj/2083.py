standardGroup = [17,80]

while(1):
    person = input().split()
    if(person[0]=="#"):
        break
    age = int(person[1])
    weight = int(person[2])

    if(age>=standardGroup[0] or weight>=standardGroup[1]):
        print(person[0],"Senior")
    else:
        print(person[0],"Junior")