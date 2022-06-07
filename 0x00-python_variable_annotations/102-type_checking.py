#!/usr/bin/env python3
""" Type annotations are a way to explicitly
define the type of a variable."""


from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
