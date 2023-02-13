def minion_game(string):
    ll= list(string.replace(" ",""))
    # print(ll)
    # print(list(set(ll)))
    ul= list(set(ll))

    vowels="AEIOU"
    STUART_SCORE=0
    KEVIN_SCORE=0
    ksub_str=[]
    ssub_str=[]
    for i in range(len(ul)):
        for j in range(len(ll)):
            if ul[i] in vowels:
                KEVIN_SCORE += 1
                vsub_str.append(sb_str)
            else:
                STUART_SCORE+=1
                sub_str.append()
                
    print(vsub_str,KEVIN_SCORE)
    print(sub_str,STUART_SCORE)


if __name__ == '__main__':
    s = input()
    minion_game(s)