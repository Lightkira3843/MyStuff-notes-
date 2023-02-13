x = "ABCDCDC"
y = "CDC"
occurrences = 0
start = 0
while start < len(x):
    pos = x.find(y, start)
    if pos == -1:
        break
    occurrences += 1
    start = pos + len(y)

print("The substring '" + y + "' appears " + str(occurrences) + " times in the string '" + x + "'.")
