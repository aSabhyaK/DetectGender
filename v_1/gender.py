def gender(s):
    while s[0:1] == ' ':
        s = s[1:len(s)];
    while s[len(s) - 1:len(s)] == ' ':
        s = s[0:len(s) - 1];

    name = s;
    if len(s) < 3:
        return "Invalid";

    i = 26 + 25 + 24 + 22;
    j = 26 + 25 + 24 + 23 + 7;

    value = hex(ord(name[len(name) - 1].lower()));

    if value == hex(j) or value == hex(i):
        return "Female";

    else:
        return "Male";

    return "Ambiguous";

print(gender('Priya'))
print(gender('Raju'))
print(gender('Sabhya'))
