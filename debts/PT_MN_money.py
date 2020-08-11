from collections import defaultdict

debts = [[7.67, ['Allen', 'Jacob', 'Ben']], [10.26, ['Allen', 'Ben']], [15.73, ['Allen', 'Jacob', 'Ben', 'Jonathan', 'Hunter']], 
         [8.92, ['Allen', 'Ben']], [8.54, ['Allen', 'Jacob', 'Ben', 'Jonathan']], [90, ['Allen', 'Ben']], [40, ['Ben']]]
totals = defaultdict(float)

for item in debts:
    number, names = item
    for name in names:
        totals[name] += number / len(names)

for name, total in totals.items():
    print((name + ':\t' + str(round(total,2))).expandtabs(12))