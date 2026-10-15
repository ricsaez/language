types = {"Type"}                              # Type : Type


def step(types):
    new = set()
    for α in types:                           # α : Type
        for β in types:                       # β : Type
            new.add(f"({α} → {β})")           # then  α → β : Type
    return types | new


for round in range(3):
    print(f"round {round}: {len(types)} types")
    for t in sorted(types, key=len)[:5]:
        print("   ", t)
    types = step(types)
