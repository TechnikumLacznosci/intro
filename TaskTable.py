from SimpleTable import *


def instantiate_table(window, data_list):
    # Define number of columns
    column_count = len(data_list[0])
    # Define number of rows
    row_count = len(data_list)
    # Empty table object with size row_count x column_count
    table = SimpleTable(window, row_count, column_count)
    table.grid(row='0', column='0')

    def get_from_table(i, j, tab):
        return data_list[i][data_list[i].keys()[j]]

    # Fill table with values
    for i in range(0, row_count):
        for j in range(0, column_count):
            table.set(i, j, get_from_table(i, j, table))