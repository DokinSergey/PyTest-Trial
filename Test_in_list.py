
txtbloc = 'a 1 2\nb 2 3\nx 4 1\n\n'
idbase = 'x'
gsr:list[str] = []

# if idbase:
    # gsr += [lstr.strip() for lstr in txtbloc.splitlines() if all((lstr,idbase in lstr))]
# else:
    # gsr += [bstr.strip() for bstr in txtbloc.splitlines() if bstr]
for lstr in txtbloc.splitlines():
    if not lstr:continue
    if idbase in lstr:#continue
        gsr.append(lstr)

print(gsr)
