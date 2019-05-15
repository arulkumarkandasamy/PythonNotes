import re
errors = []
linenum = 0
pattern = re.compile("error", re.IGNORECASE)  # Compile a case-insensitive regex
with open ('logfile.txt', 'rt') as myfile:
    for line in myfile:
        linenum += 1
        if pattern.search(line) != None:      # If a match is found
            errors.append((linenum, line.rstrip('\n')))
for err in errors:                            # Iterate over the list of tuples
    print("Line " + str(err[0]) + ": " + err[1])