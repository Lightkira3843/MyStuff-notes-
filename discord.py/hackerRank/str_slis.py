# def divide_string(input_string, group_size):
#     return [input_string[i:i+group_size] for i in range(0, len(input_string), group_size)]

# input_string = "lasjdfljsdfjlasdfjdfajfdklsdja"
# group_size = 4
# result = divide_string(input_string, group_size)
# print(result)

# s = input("sting: ")
# n =  int(input("num: "))

# x=0
# l=[]
# for i in range(n,len(s)+n,n):
#     l.append(s[x:i])
#     x=i
# l = [''.join(set(substr)) for substr in l]


# for substr in l:
#     print(substr)


# next 

s = input("sting: ")
n =  int(input("num: "))

x=0
l=[]
for i in range(n,len(s)+n,n):
    chk=s[x:i]
    w=[]
    for j in range(len(chk)):
        for k in range(j,len(chk)):
            if chk[j] == chk[k]:
                w.append(chk[k])
                continue
            w.append(chk[j])
    x=i
    l.append("".join(w))
l = [''.join(set(substr)) for substr in l]


for substr in l:
    print(substr)

