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
    required_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    ]
    try:
        for f in required_fields:
            passport[f]
    except KeyError:
        return False
    return True


my_passports = read_passports("puzzle_4.txt")
valid_passports = [passport for passport in my_passports if is_valid_passport(passport)]
print(len(valid_passports))
