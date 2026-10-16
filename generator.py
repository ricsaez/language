def occurs(x, e):
    return e == x if isinstance(e, str) else any(occurs(x, p) for p in e[1:])


def fresh(*es):
    n = 0
    while True:
        for c in "abcdefghijklmnopqrstuvwxyz":
            name = c if n == 0 else f"{c}{n}"
            if not any(occurs(name, e) for e in es):
                return name
        n += 1


def fill(e, a, v):
    if e == a:
        return v
    if isinstance(e, str):
        return e
    if e[0] == "call":
        return ("call", fill(e[1], a, v), fill(e[2], a, v))
    sign, b, *rest = e
    if sign == "->":
        rest[0] = fill(rest[0], a, v)
    if b == a:
        return (sign, b, *rest)
    if occurs(b, v):
        c = fresh(v, rest[-1], a)
        rest[-1] = fill(rest[-1], b, c)
        b = c
    rest[-1] = fill(rest[-1], a, v)
    return (sign, b, *rest)


def work_out(e):
    if isinstance(e, str):
        return e
    if e[0] == "call":
        F, V = work_out(e[1]), work_out(e[2])
        if not isinstance(F, str) and F[0] == "↦":
            return work_out(fill(F[2], F[1], V))
        return ("call", F, V)
    sign, a, *rest = e
    return (sign, a, *[work_out(p) for p in rest])


def written_same(x, y):
    if isinstance(x, str) or isinstance(y, str):
        return x == y
    if x[0] != y[0]:
        return False
    if x[0] == "call":
        return written_same(x[1], y[1]) and written_same(x[2], y[2])
    c = fresh(x, y)
    return all(written_same(p, q) for p, q in zip(x[2:-1], y[2:-1])) and written_same(fill(x[-1], x[1], c), fill(y[-1], y[1], c))


def same(x, y):
    return written_same(work_out(x), work_out(y))


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
        T = T and work_out(T)
        if T and T[0] == "->" and has_type(V, T[2], uses):
            return fill(T[3], T[1], V)
    return None


def has_type(e, T, uses):
    if not isinstance(e, str) and e[0] == "↦":
        W = work_out(T)
        if isinstance(W, str) or W[0] != "->" or not has_type(T, "Type", uses):
            return False
        _, a, C = e
        _, b, A, B = W
        c = fresh(e, W, *uses)
        return has_type(fill(C, a, c), fill(B, b, c), {**uses, c: A})
    t = type_of(e, uses)
    return t is not None and same(t, T)
