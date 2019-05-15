import re
errors = []
linenum = 0
pattern = re.compile("ec2-34-236-124-244", re.IGNORECASE)  # Compile a case-insensitive regex
with open ('tcpdumps.txt', 'rt') as myfile:
    for line in myfile:
        linenum += 1
        if pattern.search(line) != None:      # If a match is found
            errors.append((linenum, line.rstrip('\n')))
for err in errors:                            # Iterate over the list of tuples
    print("Line " + str(err[0]) + ": " + err[1])