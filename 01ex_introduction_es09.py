t = tuple( [(a,b,c) for a in range (1,100) for b in range (1,100) for c in range (1,100) if c**2 == b**2 + a**2])
print(t)