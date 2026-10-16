def occurs(x, e):
    return e == x if isinstance(e, str) else any(occurs(x, p) for p in e[1:])


def fill(e, a, v):
    if e == a:
        return v
    if isinstance(e, str):
        return e
    if e[0] == "call":
        return ("call", fill(e[1], a, v), fill(e[2], a, v))
    sign, b, *rest = e
    if e[0] == "->":
        rest[0] = fill(rest[0], a, v)
    if b == a:
        return (sign, b, *rest)
    if occurs(b, v):
        c = next(c for c in "abcdefghijklmnopqrstuvwxyz" if not occurs(c, v) and not occurs(c, rest[-1]) and c != a)
        rest[-1] = fill(rest[-1], b, c)
        b = c
    rest[-1] = fill(rest[-1], a, v)
    return (sign, b, *rest)


def type_of(e, uses):
    if e == "Type":
        return "Type"
    if isinstance(e, str):
        return uses.get(e)
    if e[0] == "->":
        _, a, A, B = e
        if has_type(A, "Type", uses) and has_type(B, "Type", {**uses, a: A}):
            return "Type"
    if e[0] == "call":
        _, F, V = e
        T = type_of(F, uses)
        if T is None and F[0] == "↦":
            A = type_of(V, uses)
            B = A and type_of(F[2], {**uses, F[1]: A})
            T = B and ("->", F[1], A, B)
        if T and T[0] == "->" and has_type(V, T[2], uses):
            return fill(T[3], T[1], V)
    return None


def has_type(e, T, uses):
    if not isinstance(e, str) and e[0] == "↦":
        _, a, C = e
        return T[0] == "->" and T[1] == a and has_type(T, "Type", uses) and has_type(C, T[3], {**uses, a: T[2]})
    return type_of(e, uses) == T
