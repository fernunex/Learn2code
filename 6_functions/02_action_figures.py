# 2144 
# Timus Judge Cleaning the Room 
# Volumen 12 


def read_boxes(n: int) -> list[list]:
    """This function reads the boxes from the input, and return
    them as a list of boxes; each box is a list of action figure
    heights.

    Args:
        n (int): number of boxes to read

    Returns:
        list: list of boxes
    """

    boxes = []

    for _ in range(n):
        box = input().split()
        box.pop(0)
        for i in range(len(box)):
            box[i] = int(box[i])
        boxes.append(box)
    return boxes

def box_ok(box: list) -> bool:
    """ Check wether a box has a nondecreasing order

    Args:
        box (list): is the list of action figure heights in a given box 

    Returns:
        bool: True if heights in box are in nondecreasing order, False otherwise.
    """
    for i in range(len(box) - 1):
        if box[i] > box[i+1]:
            return False
    return True


def all_boxes_ok(boxes: list[list]) -> bool:
    """ Check if all individual boxes has a nondecreasing order of heights.

    Args:
        boxes (list): is a list of boxes, each box is a list of action figure heights.

    Returns:
        bool: True if each box in boxes has its action figures in nondecreasing order of height,
        False otherwise
    """
    for box in boxes:
        if not box_ok(box):
            return False
    return True

def boxes_endpoints(boxes: list[list]) -> list[list]:
    """Return a list, where each value is a list of two values:
    the heights of the leftmost and rightmost action figures in a box.

    Args:
        boxes (list[list]): boxes is a list of boxes; each box is a list of action figure heights.

    Returns:
        list[list]: Return a list where each value is a list of two heights.
    """

    enpoints = []
    for box in boxes:
        enpoints.append([box[0], box[-1]])
    return enpoints

def all_endpoints_ok(endpoints: list[list]) -> bool:
    """Check if the endpoints are ordered following the next conditions:
    The list of endpoints [[2,5],[9,15],[15,18]] are correctly sorted, this mean the rightmost is always 
    less or equal than the leftmost of the next box

    This list of endpoints can't be sorted in a increasing order [[2,18],[9,15],[15,18]]

    Args:
        endpoints (list[list]): endpoints is a list, where each value is a list of two values:
            the heights of the leftmost and rightmost action figures in a box.
        
            - Requres: endpoints is sorted by action figure heights.

    Returns:
        bool:
            True: if the endpoints came from boxes that can be put in order
            False: otherwise
    """

    for i in range(len(endpoints) - 1):
        if endpoints[i][-1] > endpoints[i + 1][0]:
            return False
    return True    


# Main Program

# Read input
n = int(input())
boxes = read_boxes(n)

# Check wether all boxes are OK
if not all_boxes_ok(boxes):
    print('NO')
else:
    pass
    # Obtain a new list of boxes with only left and right heigts
    endpoints = boxes_endpoints(boxes)

    # Sort boxes
    endpoints.sort()

    # Determine wether boxes are organized
    if all_endpoints_ok(boxes):
        print('YES')
    else:
        print('NO')
