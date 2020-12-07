import logging
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


def get_reverse_rules(rules):
    reverse_rules = {}
    for parent_name, children in rules.items():
        for child in children:
            if child in reverse_rules:
                reverse_rules[child].append(parent_name)
            else:
                reverse_rules[child] = [parent_name]
    return reverse_rules


def find_possible_parent_colors(color, reverse_rules):
    if color not in reverse_rules:
        return []
    possible_parent_colors = list(reverse_rules[color])
    traversed_colors = [color]
    to_traverse = list(reverse_rules[color])
    while len(to_traverse) > 0:
        child_color = to_traverse.pop()
        try:
            for parent_color in reverse_rules[child_color]:
                possible_parent_colors.append(parent_color)
        except KeyError:
            continue
        traversed_colors.append(child_color)
        to_traverse = set(possible_parent_colors).difference(set(traversed_colors))
    return set(possible_parent_colors)


my_rules = read_rules('puzzle_7.txt')
my_reverse_rules = get_reverse_rules(my_rules)
logging.debug(my_reverse_rules)
my_possible_colors = find_possible_parent_colors('shiny gold', my_reverse_rules)
logging.debug(my_possible_colors)
print(len(my_possible_colors))
