def print_formatted(number):
    width = len(bin(number).lstrip("0b"))
    for i in range(1, number + 1):
        print(f"{i:{width}d} {oct(i).lstrip('0o').rjust(width, ' ')} {hex(i).lstrip('0x').upper().rjust(width, ' ')} {bin(i).lstrip('0b').rjust(width, ' ')}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)