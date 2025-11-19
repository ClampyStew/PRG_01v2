colors_dict = {}
new_colors = []

filename = 'colors.csv'
with open(filename, 'r') as file:
    for line in file:
        line = line.strip('\n')
        data_list = line.split(',')

for name in colors_dict:
    color = colors_dict[name]

    if color in new_colors:
        name_list = new_colors[color]
    else:
        name_list = []

    name_list.append(name)
    new_colors[color] = name_list

print("Colors Dict\n", colors_dict)
print('\nNewColors \n', new_colors)