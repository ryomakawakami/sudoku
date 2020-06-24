digits = '123456789'

rows = 'ABCDEFGHI'
columns = '123456789'
squares = [r + c for r in rows for c in columns]

# Each square referred to as a number
unitList = [list(range(9*i, 9*i+9)) for i in range(9)] + [list(range(i, i+73, 9)) for i in range(9)] \
    + [[r*9+c for r in rs for c in cs] for rs in ((0,1,2), (3,4,5), (6,7,8)) for cs in ((0,1,2), (3,4,5), (6,7,8))]

units = [None for i in range(81)]
peers = [None for i in range(81)]
for i in range(81):
    units[i] = [unit for unit in unitList if i in unit]

    s = set(units[i][0] + units[i][1] + units[i][2])
    s.remove(i)
    peers[i] = list(s)
