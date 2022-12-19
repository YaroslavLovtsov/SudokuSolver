import pseudo_graph as pg
from colorama import init as cl_init, Fore as clFore, Back as clBack
from Sudoku.Solution import Solution


def print_possibles_only(check_list, impossible_set):
    cur_line = ' '
    for check_elem in check_list:
        if check_elem in impossible_set:
            cur_line += ' '
        else:
            cur_line += f'{check_elem}'

        cur_line += ' '

    return cur_line


def print_sudoku_board(sud_brd, show_hints=False):
    hor_line_top = pg.HORIZONTAL * 7 + pg.TOP
    hor_line = pg.HORIZONTAL * 7 + pg.CROSS
    hor_line_bottom = pg.HORIZONTAL * 7 + pg.BOTTOM

    nums_set = set([el+1 for el in range(9)])
    first_line = True

    print(f'{pg.LEFT_TOP}{hor_line_top * 8}{pg.HORIZONTAL * 7}{pg.RIGHT_TOP}')
    rows_lng = len(sud_brd)

    pgv = pg.VERTICAL

    for row_index, cur_row in enumerate(sud_brd):
        line1 = pgv
        line2 = pgv
        line3 = pgv

        curr_impossible_set = set()
        for cur_str in cur_row:
            if type(cur_str) is not tuple and cur_str != '.':
                curr_impossible_set.add(int(cur_str))

        for col_index, cur_str in enumerate(cur_row):
            if type(cur_str) is tuple or cur_str == '.':
                impossible_set = set().union(curr_impossible_set)

                qdr_row = row_index // 3
                qdr_col = col_index // 3

                for cur_row_index in range(rows_lng):
                    cur_elem = sud_brd[cur_row_index][col_index]
                    if type(cur_elem) is not tuple and cur_elem != '.':
                        impossible_set.add(int(cur_elem))

                for cur_row_index in range(3):
                    for cur_col_index in range(3):
                        cur_elem = sud_brd[3 * qdr_row + cur_row_index][3 * qdr_col + cur_col_index]
                        if type(cur_elem) is not tuple and cur_elem != '.':
                            impossible_set.add(int(cur_elem))

                possible_tuple = tuple(nums_set.difference(impossible_set))
                if not show_hints:
                    all_are_impossible = list(nums_set)

                    cur_line_1 = print_possibles_only([1, 2, 3], all_are_impossible)
                    line1 += f'{clBack.WHITE}{clFore.LIGHTMAGENTA_EX}{cur_line_1}{clFore.RESET}{clBack.RESET}{pgv}'
                    cur_line_2 = print_possibles_only([4, 5, 6], all_are_impossible)
                    line2 += f'{clBack.WHITE}{clFore.LIGHTMAGENTA_EX}{cur_line_2}{clFore.RESET}{clBack.RESET}{pgv}'
                    cur_line_3 = print_possibles_only([7, 8, 9], all_are_impossible)
                    line3 += f'{clBack.WHITE}{clFore.LIGHTMAGENTA_EX}{cur_line_3}{clFore.RESET}{clBack.RESET}{pgv}'
                elif len(possible_tuple) == 1:
                    line1 += f'{clBack.WHITE}       {clBack.RESET}{pg.VERTICAL}'
                    line2 += f'{clBack.WHITE}{clFore.BLACK}   {possible_tuple[0]}   {clFore.RESET}{clBack.RESET}{pgv}'
                    line3 += f'{clBack.WHITE}       {clBack.RESET}{pg.VERTICAL}'
                else:
                    cur_line_1 = print_possibles_only([1, 2, 3], impossible_set)
                    line1 += f'{clBack.WHITE}{clFore.LIGHTMAGENTA_EX}{cur_line_1}{clFore.RESET}{clBack.RESET}{pgv}'
                    cur_line_2 = print_possibles_only([4, 5, 6], impossible_set)
                    line2 += f'{clBack.WHITE}{clFore.LIGHTMAGENTA_EX}{cur_line_2}{clFore.RESET}{clBack.RESET}{pgv}'
                    cur_line_3 = print_possibles_only([7, 8, 9], impossible_set)
                    line3 += f'{clBack.WHITE}{clFore.LIGHTMAGENTA_EX}{cur_line_3}{clFore.RESET}{clBack.RESET}{pgv}'
            else:
                line1 += f'{clBack.WHITE}       {clBack.RESET}{pg.VERTICAL}'
                line2 += f'{clBack.WHITE}{clFore.LIGHTCYAN_EX}   {cur_str}   {clFore.RESET}{clBack.RESET}{pg.VERTICAL}'
                line3 += f'{clBack.WHITE}       {clBack.RESET}{pg.VERTICAL}'

        if not first_line:
            print(f'{pg.LEFT}{hor_line * 8}{pg.HORIZONTAL * 7}{pg.RIGHT}')

        print(line1)
        print(line2)
        print(line3)

        first_line = False

    print(f'{pg.LEFT_BOTTOM}{hor_line_bottom * 8}{pg.HORIZONTAL * 7}{pg.RIGHT_BOTTOM}')

simple_example = [
    ['.', '6', '9', '7', '5', '.', '8', '.', '2'],
    ['.', '8', '.', '.', '9', '3', '.', '.', '.'],
    ['7', '.', '.', '.', '8', '2', '.', '9', '6'],
    ['.', '.', '.', '5', '.', '.', '.', '.', '.'],
    ['.', '5', '.', '3', '.', '7', '4', '.', '9'],
    ['3', '4', '7', '.', '2', '9', '.', '.', '1'],
    ['8', '7', '2', '.', '4', '5', '.', '1', '3'],
    ['.', '.', '.', '.', '3', '8', '.', '5', '.'],
    ['5', '.', '.', '2', '.', '.', '.', '.', '.']
]

cl_init()

print('----------------------------------------------------------------')
print('Simple example.......')
for simple_el in simple_example:
    print(simple_el)
print('----------------------------------------------------------------')
result = Solution(simple_example)
result.sudoku_solver(result.board)
print_sudoku_board(result.board)
print('================================================================')
print('Hello world.......')
