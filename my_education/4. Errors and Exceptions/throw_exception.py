def triangle(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        raise InvalidTriangleError('Less or equal to 0')
    p = x + y + z
    return p


class InvalidTriangleError(Exception):
    """
     Raised when a triangle has invalid size
    """


try:
    perimeter = triangle(2, 3, -4)
except InvalidTriangleError as ex:
    print(ex)
else:
    print(perimeter)
