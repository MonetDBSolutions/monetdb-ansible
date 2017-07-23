#!env python

import sys
import json

def main(scriptname, file_list_file, *nodes):
    result = dict( (node, []) for node in nodes)
    for index, line in enumerate(sorted(open(file_list_file))):
	file, lines = line.strip().split()
        lines = int(lines)
        part = file[28:-4]
	year, month = part.split('_')
	year = int(year)
	month = int(month)
	node = nodes[index % len(nodes)]
	result[node].append(dict(part=part, file=file, lines=lines, year=year, month=month))
    json.dump(result, sys.stdout, indent=4)

if __name__ == "__main__":
    sys.exit(main(*sys.argv))
