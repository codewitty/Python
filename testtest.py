d = {}
f = open("USPresidents.txt")
for line in f:
    (state, president) = line.split()
    if state not in d:
      d[state] = [president]
    else:
      d[state].append(president)
f.close()

print(d)
maxcount = max(len(v) for v in d.values())

for k, v in d.items():
	if len(v) == maxcount:
		print (f'The state with the most presidents is {k} with {maxcount} presidents:')	
		print(*d.get(k), sep = "\n")
