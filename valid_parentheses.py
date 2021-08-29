def valid_parentheses(string):
    opened = False
    cnt = 0
    for letter in string:
        if letter == "(":
            opened = True
            cnt += 1
            continue
        if opened and letter == ")":
            cnt -= 1
            if cnt == 0:
                opened = False
            continue
        if not opened and letter == ")":
            cnt = -1
            break
    if cnt != 0:
        return False
    return True
