def unpack_sausages(truck):
    soussages = [c.strip("[").strip(
        "]") for pach in truck for c in pach if c.startswith("[") and c.endswith("]")]
    result = [" ".join(list(x))
              for x in soussages if len(set(x)) == 1 and len(x) == 4]
    if not soussages:
        return ""
    return " ".join([x for i, x in enumerate(result, 1) if i % 5])
