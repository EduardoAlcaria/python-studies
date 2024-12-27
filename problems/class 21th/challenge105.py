def grades(* data, sit=False):
    g = dict()
    g['total'] = len(data)
    major = 0
    minor = 0
    for e, m in enumerate(data):
        if e == 0:
            minor = m
            major = m
        else:
            if m > major:
                major = m
            if m < minor:
                minor = m
    g['major'] = major
    g['minor'] = minor
    av = 0
    for a in data:
        av += a
    g['avarege'] = av/len(data)
    if sit == False:
        return g
    else:
        if g['avarege'] >= 7:
            g['sitation'] = "GOOD"
        if g['avarege'] >= 5 and g['avarege'] < 7:
            g['sitation'] = "REASONABLE"
        if g['avarege'] >= 0 and g['avarege'] < 5:
            g['sitation'] = "BAD"
        return g
r = grades(5.5, 9.5, 10, 6.5, sit=True)
print(r)