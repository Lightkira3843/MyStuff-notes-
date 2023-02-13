
import string

# Complete the solve function below.
def solve(s):
    if s[0] in string.ascii_lowercase or s[0] in string.ascii_uppercase :
        return s.title()
    else:
        return s
            