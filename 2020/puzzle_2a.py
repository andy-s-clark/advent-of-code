import re

p = re.compile('(?P<low>[0-9]+)+-(?P<high>[0-9]+) (?P<letter>[a-z]): (?P<password>[a-z]+)')
valid_count = 0
with open("puzzle_2.txt", "r") as f:
    for line in f:
        chunks = p.search(line)
        letter_count = chunks.group('password').count(chunks.group('letter'))
        if int(chunks.group('low')) <= letter_count <= int(chunks.group('high')):
            valid_count += 1

print(valid_count)