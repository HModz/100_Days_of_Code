import colorgram

colors_list=[]
number_of_colors = 6
colors = colorgram.extract("a.jpg", number_of_colors)

for i in range(number_of_colors):
    next_color = colors[i]
    rgb = next_color.rgb
    color=(rgb.r,rgb.g,rgb.b)
    print(rgb)
    colors_list.append(color)

print(colors_list)
