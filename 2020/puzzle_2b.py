import re

p = re.compile('(?P<first>[0-9]+)+-(?P<second>[0-9]+) (?P<letter>[a-z]): (?P<password>[a-z]+)')
valid_count = 0
with open("puzzle_2.txt", "r") as f:
    for line in f:
        chunks = p.search(line)
        in_first = chunks.group('letter') == chunks.group('password')[int(chunks.group('first'))-1]
        in_second = chunks.group('letter') == chunks.group('password')[int(chunks.group('second'))-1]
        if (in_first and not in_second) or (not in_first and in_second):
            valid_count += 1
print(valid_count)
