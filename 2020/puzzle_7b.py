import re


def read_rules(filename):
    rules = {}
    with open(filename, 'r') as f:
        rule_pattern = re.compile('(?P<color>[a-z ]+) bags contain (?P<children>[a-z0-9 ,]+)')
        child_pattern = re.compile('(?P<count>[0-9]+) (?P<color>[a-z ]+) bag')
        for line in f:
            rule_chunks = rule_pattern.match(line)
            rule_children = {}
            for child in rule_chunks['children'].split(','):
                child_chunks = child_pattern.search(child)
                if child_chunks is not None:
                    rule_children[child_chunks['color']] = child_chunks['count']
            rules[rule_chunks['color']] = rule_children
    return rules


def get_required_bag_count(color, rules):
    bag_count = 0
    child_bags = rules[color]
    for child_color, child_count in rules[color].items():
        bag_count += int(child_count)
        bag_count += int(child_count) * get_required_bag_count(child_color, rules)
    return bag_count


my_rules = read_rules('puzzle_7.txt')
required_bag_count = get_required_bag_count('shiny gold', my_rules)
print(required_bag_count)
