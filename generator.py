def types(names, depth, fresh=1):
    found = {"Type"} | {n for n, t in names if t == "Type"}
    if depth == 0:
        return found
    n = f"<{'abcdefghijklmnopqrstuvwxyz'[fresh - 1]}>"
    for s0 in types(names, depth - 1, fresh + 1):
        for s1 in types(names + [(n, s0)], depth - 1, fresh + 1):
            found.add(f"(({n} : {s0}) -> {s1})")
    return found
