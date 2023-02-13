stacks=[]
for t in range(int(input())):
    n=input()
    stacks.append(list(map(int,input().split())))
for i in stacks:
    can="Yes"
    new=[]
    for n in range(len(i)):
        if i[0]>=i[-1]:
            new.append(i.pop(0))
            if new[n]>new[n-1]:
                can="No"
                break
        else:
            new.append(i.pop(-1))
            if new[n]>new[n-1]:
                can="No"
                break
    print(can)