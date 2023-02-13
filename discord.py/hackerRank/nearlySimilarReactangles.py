
def nearlySimilarRectangles(sides):
    count = 0
    for i in range(0,len(sides)-1):
        x = sides[i];
        for j in range(i+1, len(sides)):
            # if sides[i][0] * sides[j][1] == sides[i][1] * sides[j][0]:
                y = sides[j];
                if x[0]/y[0] == x[1]/y[1]:
                    count += 1
    return count
  