def is_type(e, uses):
    if e == "Type":
        return True
    if e in uses:
        return uses[e] == "Type"
    if e[0] == "->":
        _, x, A, B = e
        return is_type(A, uses) and is_type(B, {**uses, x: A})
    return False
