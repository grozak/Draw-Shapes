import re


def validateShape(shape):
    if 'type' not in shape.keys():
        return False

    if shape.get('type') == 'point':
        if not isinstance(shape.get('x'), int):
            return False
        if not isinstance(shape.get('y'), int):
            return False
        return True

    elif shape.get('type') == 'polygon':
        if 'points' not in shape.keys():
            return False
        points = shape.get('points')
        if not isinstance(points, list):
            return False
        if len(points) < 3:
            return False
        for point in points:
            if not isinstance(point, list):
                return False
            if len(point) != 2:
                return False
            if not (isinstance(point[0], int) and isinstance(point[1], int)):
                return False
        return True

    elif shape.get('type') == 'rectangle':
        if not isinstance(shape.get('x'), int):
            return False
        if not isinstance(shape.get('y'), int):
            return False
        if not isinstance(shape.get('width'), int):
            return False
        if not isinstance(shape.get('height'), int):
            return False
        return shape.get('width') > 0 and shape.get('height') > 0

    elif shape.get('type') == 'square':
        if not isinstance(shape.get('x'), int):
            return False
        if not isinstance(shape.get('y'), int):
            return False
        if not isinstance(shape.get('size'), int):
            return False
        return shape.get('size') > 0

    elif shape.get('type') == 'circle':
        if not isinstance(shape.get('x'), int):
            return False
        if not isinstance(shape.get('y'), int):
            return False
        if not isinstance(shape.get('radius'), int):
            return False
        return shape.get('radius') > 0


def validateScreen(screen, palette):
    if not isinstance(screen.get('width'), int):
        return False
    if not isinstance(screen.get('height'), int):
        return False
    if not validateColor(screen.get('bg_color'), palette):
        return False
    if not validateColor(screen.get('fg_color'), palette):
        return False
    return screen.get('width') > 0 and screen.get('height') > 0


def validatePalette(palette):
    for color in palette:
        if not re.match('^#[A-Fa-f0-9]{6}$', palette[color]):
            return False
    return True


def validateColor(color, palette):
    if not isinstance(color, str):
        return False

    if re.match('^#[A-Fa-f0-9]{6}$', color):
        return True

    if color.startswith('(') and color.endswith(')'):
        color = [x.strip('()') for x in color.split(',')]
        if len(color) != 3:
            return False
        for c in color:
            try:
                c = int(c)
            except ValueError:
                return False
            if not 0 <= c <= 255:
                return False
        return True
    elif color in palette.keys():
        return True
    return False
