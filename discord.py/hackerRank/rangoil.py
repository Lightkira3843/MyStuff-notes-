def rangoli(size):
    import string
    alpha = string.ascii_lowercase

    def print_rangoli(size):
        L = []
        for i in range(size):
            s = "-".join(alpha[i:size])
            L.append((s[::-1]+s[1:]).center(4*size-3, "-"))

            print(f"{i}th L is: ",L)

        print("final L is: ",L)
        return "\n".join(L[:0:-1]+L)

    return print_rangoli(size)


print(rangoli(5))