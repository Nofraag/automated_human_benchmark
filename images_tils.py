

def find_color_on_screen(px, color, c):
    for x in range(c[0][0], c[1][0]):
        for y in range(c[0][1], c[3][1]):
            if px[x, y] == color:
                return (x, y)
