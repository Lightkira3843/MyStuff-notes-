def minion_game(string):
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            sub_string = string[i:j + 1]
            if sub_string[0] in vowels:
                kevin_score += 1
                print(f"Kevin's substring: {sub_string}")
            else:
                stuart_score += 1
                print(f"Stuart's substring: {sub_string}")
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

minion_game("BANANA HII")


#--------------------------------------------------------------------------------


def minion_game2(string):
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

minion_game2("BANANA")