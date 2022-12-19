from colorama import init as cl_init,  Fore as clFore, Back as clBack, Style as clStyle

LEFT_TOP = chr(9484)
LEFT_BOTTOM = chr(9492)
LEFT = chr(9500)

RIGHT_TOP = chr(9488)
RIGHT_BOTTOM = chr(9496)
RIGHT = chr(9508)

TOP = chr(9516)
BOTTOM = chr(9524)
CROSS = chr(9532)

VERTICAL = chr(9474)
HORIZONTAL = chr(9472)


def border_element(up_wall, left_wall, right_wall, down_wall):
    if not up_wall and not left_wall and right_wall and down_wall:
        result = LEFT_TOP
    elif not up_wall and left_wall and not right_wall and down_wall:
        result = RIGHT_TOP
    elif up_wall and not left_wall and right_wall and not down_wall:
        result = LEFT_BOTTOM
    elif up_wall and left_wall and not right_wall and not down_wall:
        result = RIGHT_BOTTOM
    elif not up_wall and left_wall and right_wall and down_wall:
        result = TOP
    elif up_wall and not left_wall and right_wall and down_wall:
        result = LEFT
    elif up_wall and left_wall and not right_wall and down_wall:
        result = RIGHT
    elif up_wall and left_wall and right_wall and not down_wall:
        result = BOTTOM
    elif not left_wall and not right_wall and (up_wall or down_wall):
        result = VERTICAL
    elif not up_wall and not down_wall and (left_wall or right_wall):
        result = HORIZONTAL
    else:
        result = CROSS

    return f'{clStyle.DIM}{clFore.BLACK}{clBack.LIGHTBLACK_EX}{result}{clBack.RESET}{clFore.RESET}{clStyle.RESET_ALL}'


if __name__ == "__main__":
    print(LEFT_TOP, HORIZONTAL * 4, TOP, HORIZONTAL * 4, RIGHT_TOP, sep='')
    print(VERTICAL, '  1 ', VERTICAL, ' 64 ', VERTICAL, sep='')
    print(LEFT, HORIZONTAL * 4, CROSS, HORIZONTAL * 4, RIGHT, sep='')
    print(VERTICAL, '  2 ', VERTICAL, ' 63 ', VERTICAL, sep='')
    print(LEFT_BOTTOM, HORIZONTAL * 4, BOTTOM, HORIZONTAL * 4, RIGHT_BOTTOM, sep='')
