
i=0

while i < 10:
    print('this is iteration number {}'.format(i))
    i += 1

i=0

while i < 10:
    break

for h in range(10):
    if h == 3:
        continue
    print(h)

for j in range(10):
    if j == 3:
        print('j=3')
        j += 1
    else:
        print(j)
        j += 1

