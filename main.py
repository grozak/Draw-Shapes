import json
import shapes
import validate
import draw
import argparse


def readShapesFromJson(data):
    shapes_list = []
    if 'Figures' not in data.keys():
        return []
    palette = data['Palette']
    i = 1
    for shape in data['Figures']:
        if (validate.validateShape(shape)):
            color = ''
            if 'color' in shape:
                if validate.validateColor(shape['color'], palette):
                    color = shape['color']
            if shape['type'] == 'point':
                shapes_list.append(shapes.Point(shape['x'], shape['y']))
            elif shape['type'] == 'polygon':
                points = []
                for point in shape['points']:
                    points.append(shapes.Point(point[0], point[1]))
                shapes_list.append(shapes.Polygon(points, color))
            elif shape['type'] == 'rectangle':
                point = shapes.Point(shape['x'], shape['y'])
                rect = shapes.Rectangle(point, shape['width'], shape['height'], color)
                shapes_list.append(rect)
            elif shape['type'] == 'square':
                point = shapes.Point(shape['x'], shape['y'])
                shapes_list.append(shapes.Square(point, shape.get('size'), color))
            elif shape['type'] == 'circle':
                point = shapes.Point(shape['x'], shape['y'])
                shapes_list.append(shapes.Circle(point, shape.get('radius'), color))
            else:
                print('Wrong type in Figure number', i, 'in file.')
        else:
            print('Wrong parameters in Figure number', i, 'in file.')
        i = i + 1
    return shapes_list


def main(input, output):
    try:
        with open(input) as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError as E:
        print('Wrong Json file:', E)
        return
    except FileNotFoundError as E:
        print(E)
        return

    if 'Screen' in data.keys():
        screen = data['Screen']
    else:
        print('No \"Screen\" in file')
        return
    if 'Palette' in data.keys():
        palette = data['Palette']
    else:
        print('No \"Palette\" in file')
        return

    shapes_list = readShapesFromJson(data)

    draw.draw(screen['width'], screen['height'], screen['bg_color'], screen['fg_color'], palette, shapes_list, output)


if __name__ == "__main__":
    input = 'sample.json'
    output = 'out.png'
    main(input, output)

