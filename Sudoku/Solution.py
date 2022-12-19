import random
import datetime


class Solution:
    def __init__(self, board=None):
        self.board = []

        for row in board:
            self.board.append(['.' if elem == 0 else str(elem) for elem in row])

    def try_to_decide4(self, sud_brd):
        rating_dict = {}

        for inx1 in range(9):
            for inx2 in range(9):
                cur_elem = sud_brd[inx1][inx2]
                if type(cur_elem) is tuple:
                    lng = len(cur_elem)
                    if lng in rating_dict.keys():
                        rating_dict[lng].append(((inx1, inx2), cur_elem))
                    else:
                        rating_dict[lng] = [((inx1, inx2), cur_elem)]

        rating_keys_list = list(rating_dict.keys())
        rating_keys_list.sort()

        result_array = []

        if len(rating_dict) == 0:
            return result_array

        rating_supposes_element = rating_dict[rating_keys_list[0]][0]
        for supposes_element in rating_supposes_element[1]:
            current_copy_brd = self.try_to_decide1(sud_brd)
            current_copy_brd[rating_supposes_element[0][0]][rating_supposes_element[0][1]] = str(supposes_element)
            decided_copy_brd = self.try_to_decide_main(current_copy_brd)
            decided_copy_info = self.get_board_info(decided_copy_brd)

            if decided_copy_info[1] == 0:
                result_array.append(decided_copy_brd)

        return result_array

    def try_to_decide3(self, sud_brd):
        result = []
        quadrants = []

        nums_set = set([el + 1 for el in range(9)])

        for ind1 in range(9):
            current_quadrant_y = ind1 // 3
            current_quadrant_x = ind1 % 3
            current_quadrant = []
            current_copy_row = []

            for ind2 in range(9):
                current_y = ind2 // 3
                current_x = ind2 % 3

                current_elem1 = sud_brd[ind1][ind2]
                current_copy_row.append(current_elem1)

                current_elem2 = sud_brd[3 * current_quadrant_y + current_y][3 * current_quadrant_x + current_x]
                current_quadrant.append(current_elem2)

            result.append(current_copy_row)
            quadrants.append(current_quadrant)

        for cur_quadr_inx, cur_quadrant in enumerate(quadrants):
            known_list = []
            unknown_list = []

            for cur_quadr_elem_inx, cur_quadr_elem in enumerate(cur_quadrant):
                if type(cur_quadr_elem) is tuple:
                    unknown_list.append((cur_quadr_elem_inx, cur_quadr_elem))
                else:
                    known_list.append(int(cur_quadr_elem))

            cur_quadr_success = False

            known_set = set(known_list)
            unknown_set = nums_set.difference(known_set)
            for cur_qty in range(2, len(unknown_set)):
                if cur_quadr_success:
                    break

                cur_subsets = self.get_subsets_of_length(list(unknown_set), cur_qty)
                for cur_subset in cur_subsets:
                    if cur_quadr_success:
                        break

                    subsets_only = []
                    dict_unless = {}

                    for cur_quadr_inx1, unknown_list_elem in unknown_list:
                        cur_unknown_set = set(unknown_list_elem)
                        test_set1 = cur_unknown_set.difference(set(cur_subset[0]))
                        test_set2 = cur_unknown_set.intersection(set(cur_subset[1]))

                        if len(test_set1) == 0 and len(test_set2) == 0:
                            subsets_only.append(unknown_list_elem)
                        else:
                            dict_unless[cur_quadr_inx1] = unknown_list_elem

                    if len(subsets_only) == len(cur_subset[0]):
                        for cur_unless_key in dict_unless.keys():
                            cur_diff = list(set(dict_unless[cur_unless_key]).difference(set(cur_subset[0])))
                            if len(cur_diff) == 1:
                                cur_quadr_success = True

                                yy1 = 3 * (cur_quadr_inx // 3) + (cur_unless_key // 3)
                                xx1 = 3 * (cur_quadr_inx % 3) + (cur_unless_key % 3)

                                result[yy1][xx1] = str(cur_diff[0])
                                break

        return self.try_to_decide1(result)

    def try_to_decide2(self, sud_brd):
        result = []
        nums_set = set([el + 1 for el in range(9)])

        for inx1 in range(9):
            current_impossible_in_column = set()

            str_copy = []

            for inx2 in range(9):

                curr_elem_column = sud_brd[inx2][inx1]
                if type(curr_elem_column) is not tuple and curr_elem_column != '.':
                    current_impossible_in_column.add(int(curr_elem_column))

                str_copy.append(curr_elem_column)

            row_possible_list = list(nums_set.difference(current_impossible_in_column))
            for possible_el in row_possible_list:
                last_inx = 9
                items_count = 0

                for cur_inx, str_copy_el in enumerate(str_copy):
                    if type(str_copy_el) is tuple:
                        if possible_el in str_copy_el:
                            last_inx = cur_inx
                            items_count += 1

                if items_count == 1:
                    str_copy[last_inx] = possible_el

            result.append(str_copy)

        return self.try_to_decide1(result)

    def try_to_decide1(self, sud_brd):
        result = []
        success = False

        nums_set = set([el + 1 for el in range(9)])
        rows_lng = len(sud_brd)

        for row_index, cur_row in enumerate(sud_brd):
            str_copy = []
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
                    if len(possible_tuple) == 1:
                        str_copy.append(f'{possible_tuple[0]}')
                        success = True
                    else:
                        str_copy.append(possible_tuple)
                else:
                    str_copy.append(cur_str)

            result.append(str_copy)

        if success:
            return self.try_to_decide1(result)
        else:
            return result.copy()

    @staticmethod
    def get_board_info(sud_brd):
        empty_cells = 0
        contradictions = 0

        for ind1 in range(9):
            current_quadrant_y = ind1 // 3
            current_quadrant_x = ind1 % 3

            current_row = []
            current_column = []

            current_quadrant = []

            for ind2 in range(9):
                current_y = ind2 // 3
                current_x = ind2 % 3

                current_elem1 = sud_brd[ind1][ind2]
                if type(current_elem1) is not tuple and current_elem1 != '.':
                    current_row.append(current_elem1)
                else:
                    empty_cells += 1
                    if current_elem1 is tuple and len(current_elem1) == 0:
                        contradictions += 1

                current_elem2 = sud_brd[ind2][ind1]
                if type(current_elem2) is not tuple and current_elem2 != '.':
                    current_column.append(current_elem2)

                current_elem3 = sud_brd[3 * current_quadrant_y + current_y][3 * current_quadrant_x + current_x]
                if type(current_elem3) is not tuple and current_elem3 != '.':
                    current_quadrant.append(current_elem3)

            current_row_trunc = list(set(current_row))
            if len(current_row) != len(current_row_trunc):
                contradictions += 1
            else:
                pass

            current_column_trunc = list(set(current_column))
            if len(current_column) != len(current_column_trunc):
                contradictions += 1
            else:
                pass

            current_quadrant_trunc = list(set(current_quadrant))
            if len(current_quadrant) != len(current_quadrant_trunc):
                contradictions += 1
            else:
                pass

        return empty_cells, contradictions

    @staticmethod
    def get_subsets_of_length(lst, qty):
        lng = len(lst)

        result = []

        for test_num in range(1, 2 ** lng):
            subset1 = []
            subset0 = []

            cur_test_num = test_num
            for cur_ind in range(lng):
                cur_rest = cur_test_num % 2
                cur_test_num //= 2

                if cur_rest == 1:
                    subset1.append(lst[cur_ind])
                else:
                    subset0.append(lst[cur_ind])

            if len(subset1) == qty:
                result.append(tuple([tuple(subset1), tuple(subset0)]))

        return result

    def try_to_decide_main(self, sudoku_board_original):
        current_sudoku_board1 = self.try_to_decide1(sudoku_board_original)
        start_empty_cells, start_contradictions = self.get_board_info(current_sudoku_board1)
        stop_test = start_contradictions != 0

        while not stop_test:
            current_sudoku_board2 = self.try_to_decide2(self.try_to_decide2(current_sudoku_board1))
            current_sudoku_board3 = self.try_to_decide3(self.try_to_decide1(current_sudoku_board2))
            cur_empty_cells, cur_contradictions = self.get_board_info(current_sudoku_board3)
            current_sudoku_board1 = self.try_to_decide1(current_sudoku_board3)

            if cur_empty_cells < start_empty_cells and cur_contradictions == 0:
                start_empty_cells = cur_empty_cells
            else:
                stop_test = True

        return current_sudoku_board1

    def get_solve_array(self, result_sudoku_board):
        result_sudoku_board_array = [result_sudoku_board]
        decided_sudoku_board = []

        global_stop_test = False

        while not global_stop_test:

            current_board_array = []
            for current_supposed_sudoku_board in result_sudoku_board_array:
                current_decided_board = self.try_to_decide4(current_supposed_sudoku_board)
                for current_decided_elem in current_decided_board:
                    elem_to_add = self.try_to_decide1(current_decided_elem)
                    current_board_array.append(elem_to_add)

            result_sudoku_board_array = []

            for current_elem in current_board_array:
                current_elem_info = self.get_board_info(current_elem)
                if current_elem_info[1] == 0:
                    if current_elem_info[0] == 0:
                        decided_sudoku_board.append(current_elem)
                    else:
                        elem_to_add = self.try_to_decide_main(current_elem)
                        result_sudoku_board_array.append(elem_to_add)

            if len(result_sudoku_board_array) == 0:
                global_stop_test = True

        return decided_sudoku_board

    def sudoku_solver(self, board):
        result_sudoku_board = self.try_to_decide_main(board)
        result_sudoku_board_info = self.get_board_info(result_sudoku_board)

        if result_sudoku_board_info[0] == 0:
            for ind_y, el_y in enumerate(result_sudoku_board):
                for ind_x, el_x in enumerate(el_y):
                    board[ind_y][ind_x] = str(el_x)
        else:
            decided_sudoku_board = self.get_solve_array(result_sudoku_board)
            if len(decided_sudoku_board):
                for ind_y, el_y in enumerate(decided_sudoku_board[0]):
                    for ind_x, el_x in enumerate(el_y):
                        board[ind_y][ind_x] = str(el_x)
            else:
                pass
