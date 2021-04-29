def chess_board_cell_color(cell1, cell2):
    x1, y1 = get_cell_x_and_y(cell1)
    x2, y2 = get_cell_x_and_y(cell2)
    return is_cell_dark(x1, y1) == is_cell_dark(x2, y2)


def get_cell_x_and_y(coordinate):
    x = ord(coordinate[0]) - (ord("A")-1)
    y = int(coordinate[1])
    return x, y


def is_cell_dark(x, y):
    if x % 2 == y % 2:
        return True
    else:
        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    output = chess_board_cell_color("A1", "C3")
    print(output)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
