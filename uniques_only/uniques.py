def uniques_only(input_iterable):
    hashable_seen = set()
    seen = list()
    for val in input_iterable:
        try:
            if val not in hashable_seen:
                hashable_seen.add(val)
                seen.append(val)
                yield val
        except: 
            if val not in seen:
                seen.append(val)
                yield val