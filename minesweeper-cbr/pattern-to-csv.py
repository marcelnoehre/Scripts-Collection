pattern = input()
csv = ''
for char in pattern:
    csv += '"' + char + '",'
print(csv[:-1])