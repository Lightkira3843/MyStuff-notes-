
import string

# Complete the solve function below.
def solve(s):
    names = s.split(" ")
    capitalized_names = [name.capitalize() for name in names]
    return " ".join(capitalized_names)
        

s=input("Enter String: ")    
solve(s)