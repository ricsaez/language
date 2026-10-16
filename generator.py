types = {"Type"}

def step(types):
    new = set()
    for s1 in types:
        for s2 in types:
            new.add(f"({s1} → {s2})")
    return types | new
