import matplotlib.pyplot as plt
import re


def draw(width, height, bg_color, fg_color, palette, shapes, output):
    bg_color = convertColor(bg_color, palette)
    fg_color = convertColor(fg_color, palette)

    fig = plt.figure(facecolor=bg_color)

    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.set(xlim=[0, width], ylim=[0, height], aspect=1)
    fig.set_tight_layout(False)



    for shape in shapes:
        color = fg_color
        class_type = type(shape).__name__
        if class_type == 'Point':
            drawing = plt.Circle((shape.x, shape.y), 1, color=color)
        elif class_type == 'Polygon':
            if (shape.color != ''):
                color = convertColor(shape.color, palette)
            points = []
            for point in shape.points:
                points.append((point.x, point.y))
            drawing = plt.Polygon(points, closed=True, color=color)
        elif class_type == 'Rectangle':
            if (shape.color != ''):
                color = convertColor(shape.color, palette)
            drawing = plt.Rectangle((shape.point.x, shape.point.y), shape.width, shape.height, color=color)
        elif class_type == 'Square':
            if (shape.color != ''):
                color = convertColor(shape.color, palette)
            drawing = plt.Rectangle((shape.point.x, shape.point.y), shape.size, shape.size, color=color)
        elif class_type == 'Circle':
            if (shape.color != ''):
                color = convertColor(shape.color, palette)
            drawing = plt.Circle((shape.point.x, shape.point.y), shape.radius, color=color)
        else:
            drawing = None
        ax.add_patch(drawing)
    if output:
        fig.savefig(output, facecolor=bg_color)
    fig.show()


def convertColor(color, palette):
    if not isinstance(color, str):
        return False
    if re.match('^#[A-Fa-f0-9]{6}$', color):
        return color
    if color.startswith('(') and color.endswith(')'):
        color = [x.strip('()') for x in color.split(',')]
        out = "#"
        for c in color:
            out += str(hex(int(c)))[2:]
        return out
    if color in palette.keys():
        return palette[color]
    return

