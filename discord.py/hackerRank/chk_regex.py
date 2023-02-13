def is_regex(string):
    special_characters = set('.*?[]{}()^$|\\')
    in_char_set = False
    escaped = False
    for char in string:
        if escaped:
            escaped = False
            continue
        if char in special_characters:
            if char == ']':
                in_char_set = False
            elif char == '[':
                in_char_set = True
            elif char == '\\':
                escaped = True
        elif in_char_set:
            continue
        elif char in '.*?^{}$':
            continue
        else:
            return False
    return True
print(is_regex("[a-z]"))