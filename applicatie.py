with open("steam.json") as f:
    firstline = f.readlines()[0].rstrip()

print(firstline)
