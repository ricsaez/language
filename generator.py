def has_type(e, T, uses):
    if e == "Type":
        return T == "Type"
    if e in uses:
        return uses[e] == T
    if e[0] == "->":
        _, a, A, B = e
        return T == "Type" and has_type(A, "Type", uses) and has_type(B, "Type", {**uses, a: A})
    if e[0] == "↦":
        _, a, C = e
        return T[0] == "->" and T[1] == a and has_type(T, "Type", uses) and has_type(C, T[3], {**uses, a: T[2]})
    return False
