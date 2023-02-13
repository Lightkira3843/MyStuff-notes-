N = int(input("Enter a Number: "))
lst=[]
for _ in range(N):
    n = input("Command: ").split()
    cmd=n[0]
    args = n[1:]
    
    if cmd != "print":
        cmd += "("+ ",".join(args) +")"
        eval("lst."+cmd)
    else:
        print(lst)