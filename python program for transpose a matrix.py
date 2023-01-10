m = [[4,5],[5,6],[6,7]]
for row in m :
	print(row)
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
for row in rez:
	print(row)
