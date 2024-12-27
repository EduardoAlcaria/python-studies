def grades(* data, sit=False):
    g = dict()
    g['total'] = len(data)
    g['major'] = max(data)
    g['minor'] = min(data)
    g['avarege'] = sum(data)/g['total']
    if sit:
        if g['avarege'] >= 7:
            g['situation'] = "GOOD"
        elif g['avarege'] >= 5:
            g['situation'] = "REASONABLE"
        else:
            g['situation'] = "BAD"
    return g
r = grades(5.5, 2.5, 8.5, sit=True)
print(r)