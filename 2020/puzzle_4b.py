import logging
import re


def read_passports(filename):
    passports = []
    passport = {}
    with open(filename, "r") as f:
        for line in f:
            if line == "\n":
                if len(passport) > 0:
                    passports.append(passport)
                passport = {}
            else:
                for p in line.strip().split(" "):
                    kv = p.split(":")
                    passport[kv[0]] = kv[1]
    if len(passport) > 0:
        passports.append(passport)
    return passports


def is_valid_passport(passport):
    required_fields = {
        'byr': {
            'minimum': 1920,
            'maximum': 2002
        },
        'iyr': {
            'minimum': 2010,
            'maximum': 2020
        },
        'eyr': {
            'minimum': 2020,
            'maximum': 2030
        },
        'hgt': {
            'pattern': re.compile('^(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)$'),
        },
        'hcl': {
            'pattern': re.compile('^#[0-9a-f]{6}$'),
        },
        'ecl': {
            'pattern': re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$'),
        },
        'pid': {
            'pattern': re.compile('^[0-9]{9}$'),
        }
    }
    try:
        for f in required_fields.items():
            field_name = f[0]
            passport[field_name]
            try:
                pattern = f[1]['pattern']
                if not pattern.match(passport[field_name]):
                    logging.info("Pattern match failure for %s in %s" % (field_name, passport))
                    return False
            except KeyError:
                pass
            try:
                minimum = f[1]['minimum']
                if int(passport[field_name]) < minimum:
                    logging.info("Less than minimum of %i for %s in %s" % (minimum, field_name, passport))
                    return False
            except KeyError:
                pass
            try:
                maximum = f[1]['maximum']
                if int(passport[field_name]) > maximum:
                    logging.info("Greater than maximum of %i for %s in %s" % (maximum, field_name, passport))
                    return False
            except KeyError:
                pass
    except KeyError:
        logging.info("Missing %s in %s" % (field_name, passport))
        return False
    return True


logging.basicConfig(level=logging.WARN)
my_passports = read_passports("puzzle_4.txt")
valid_passports = [passport for passport in my_passports if is_valid_passport(passport)]
print(len(my_passports))
print(len(valid_passports))
