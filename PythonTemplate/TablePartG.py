import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

connection = hb.Connection()
table = connection.table('powers')

# Scan the 'powers' table
data = list(table.scan())

# Iterate over each row
for key, value in data:
    color = value[b'custom:color']
    name = value[b'professional:name']
    power = value[b'personal:power']
    # Iterate over each row again to find matching color
    for key1, value1 in data:
        color1 = value1[b'custom:color']
        name1 = value1[b'professional:name']
        power1 = value1[b'personal:power']
        # If color matches and names are different, print them
        if color == color1 and name != name1:
            print('{}, {}, {}, {}, {}'.format(name, power, name1, power1, color))
