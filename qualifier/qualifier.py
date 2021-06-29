from typing import Any, List, Optional


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centereded: If the items should be aligned to the centered, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    ...

    table = ''
    columns = [] # will store same column values from each row.
    table_bottom = '' # └────┘ or └────┴────┘ etc

    #create a 2d list of objects that have a similar column representation in order to determine the width of each column in a row.
    for i in range(len(max(rows, key=len))):
        temp_column = []
        for row in rows:
            if i <= len(row)-1:
                temp_column.append(row[i])
            else:
                pass
        if temp_column != []:
            columns.append(temp_column)
    # build table roof and bottom. table_bottom will be added last to the table. ┌───┐ or ┌───┬────┐ etc
    for i in range(len(columns)):
        columns_v2 = [ str(x) for x in columns[i]]
        column_max_len = len(max(columns_v2, key=len)) if len(max(columns_v2, key=len)) > (len(str(labels[i])) if labels != None else 0) else len(str(labels[i]))

        if i == 0:
            table += u'\u250C' + (column_max_len + 2) * u'\u2500'
            table_bottom += u'\u2514' + (column_max_len + 2) * u'\u2500'
            if len(columns) - 1 == 0:
                table += u'\u2510' + '\n'
                table_bottom += u'\u2518' + '\n'
        elif not i is len(columns):
            table += u'\u252C' + (column_max_len + 2) * u'\u2500'
            table_bottom += u'\u2534' + (column_max_len + 2) * u'\u2500'
            if i == len(columns) - 1:
                table += u'\u2510' + '\n'
                table_bottom += u'\u2518' + '\n'
    # Fill in column labels if available.
    if  labels != None:
        close_labels = ''
        for i in range(len(labels)):
            columns_v2 = [ str(x) for x in columns[i]]
            column_max_len = len(max(columns_v2, key=len)) if len(max(columns_v2, key=len)) > len(str(labels[i])) else len(str(labels[i]))
            if centered:
                if i == 0:
                    table += u'\u2502' + str(labels[i]).center(column_max_len + 2)
                    close_labels += u'\u251c' + u'\u2500' * (column_max_len + 2)
                    if len(labels) - 1 == 0:
                        table += u'\u2502' + '\n'
                        close_labels += u'\u2524' + '\n'
                elif not i is len(labels):
                    table += u'\u2502' + str(labels[i]).center(column_max_len + 2)
                    close_labels += u'\u253c' + u'\u2500' * (column_max_len + 2)
                    if i == len(labels) - 1:
                        table += u'\u2502' + '\n'
                        close_labels += u'\u2524' + '\n'
            else:
                if i == 0:
                    table += u'\u2502' + ' ' + '{:<{length}}'.format(labels[i], length = (column_max_len + 1))
                    close_labels += u'\u251c' + u'\u2500' * (column_max_len + 2)
                    if len(labels) - 1 == 0:
                        table += u'\u2502' + '\n'
                        close_labels += u'\u2524' + '\n'
                elif not i is len(labels):
                    table += u'\u2502' + ' ' + '{:<{length}}'.format(labels[i], length = (column_max_len + 1))
                    close_labels += u'\u253c' + u'\u2500' * (column_max_len + 2)
                    if i == len(labels) - 1:
                        table += u'\u2502' + '\n'
                        close_labels += u'\u2524' + '\n'
        table += close_labels

    for row in rows:
        for i in range(len(columns)):
            columns_v2 = [ str(x) for x in columns[i]]
            column_max_len = len(max(columns_v2, key=len)) if len(max(columns_v2, key=len)) > (len(str(labels[i])) if labels != None else 0 ) else len(str(labels[i]))
            if row != []:
                if centered:
                    if i == 0:
                        table += u'\u2502' + str(row[i]).center(column_max_len + 2)
                        if len(row) - 1 == 0:
                            if len(columns) - 1 == i:
                                table += u'\u2502' + '\n'
                            else:
                              table += u'\u2502'
                    elif i < len(row):
                        table += u'\u2502' + str(row[i]).center(column_max_len + 2)
                        if i == len(row) - 1:
                            if i != len(columns) - 1:
                                table += u'\u2502'
                            else:
                               table += u'\u2502' + '\n'
                    else:
                        if len(columns)-1 == i:
                            table += ' '.center(column_max_len + 2) + u'\u2502' + '\n'
                        else:
                            table += ' '.center(column_max_len + 2) + u'\u2502'
                else:
                    if i == 0:
                        table += u'\u2502' + ' ' + '{:<{length}}'.format(row[i], length = (column_max_len + 1))
                        if len(row) - 1 == 0:
                            if len(columns) - 1 == i:
                                table += u'\u2502' + '\n'
                            else:
                               table += u'\u2502'
                    elif i < len(row):
                        table += u'\u2502' + ' ' + '{:<{length}}'.format(row[i], length = (column_max_len + 1))
                        if len(row) - 1 == i:
                            if i != len(columns) - 1:
                                table += u'\u2502'
                            else:
                               table += u'\u2502' + '\n'
                    else:
                        if len(columns)-1 == i:
                            table += ' ' + '{:<{length}}'.format(' ', length = (column_max_len + 1)) + u'\u2502' + '\n'
                        else:
                            table += ' ' + '{:<{length}}'.format(' ', length = (column_max_len + 1)) + u'\u2502'
            else:
                table += u'\u2502' + ' ' + '{:<{length}}'.format(' ', length = (column_max_len + 1))
                if len(columns) - 1 == i:
                    table += u'\u2502' + '\n'

    table +=  table_bottom
    return table

def main():
    print(make_table(
        rows=[
            ["Apple", 5],
            ["Banana", 3],
            ["Cherry", 7],
        ],
        labels=["Fruit", "Tastiness"],
    ))
main()
