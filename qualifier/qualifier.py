from typing import Any, List, Optional


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    Box_draw_chars = {"vertical_pipe": u'\u2502', "right_top": u'\u2510', "right_bottom": u'\u2518', "left_top": u'\u250C', \
    "left_bottom": u'\u2514', "horiz_pipe": u'\u2500', "cross": u'\u253c', "top_t": u'\u252c', "bottom_t": u'\u2534', "left_t": u'\u251c', \
    "right_t": u'\u2524' }

    print(Box_draw_chars["horiz_pipe"]);

def main():
    make_table([12])
main()
