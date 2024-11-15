def handle_movement(cell_list, cell, row_, col_, NUM):

    blank_cell_row, blank_cell_col = 0, 0

    for index, row in enumerate(cell_list):
        for idx, cell in enumerate(row):
            if cell.value == None:
                blank_cell_row, blank_cell_col = index, idx

    if col_ == blank_cell_col:
        if abs(blank_cell_row - row_) == 1:
            cell_list[row_][col_].value, cell_list[blank_cell_row][blank_cell_col].value = cell_list[blank_cell_row][blank_cell_col].value, cell_list[row_][col_].value 
        else:
            pass

    if row_ == blank_cell_row:
        if abs(blank_cell_col - col_) == 1:
            cell_list[row_][col_].value, cell_list[blank_cell_row][blank_cell_col].value = cell_list[blank_cell_row][blank_cell_col].value, cell_list[row_][col_].value
        else:
            pass

    for i in range(NUM):
        for j in range(NUM):
            cell_list[i][j].color = (64, 64, 64, 1) if cell_list[i][j].value is not None else (255, 255, 255)