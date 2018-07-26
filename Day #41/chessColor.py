def solution(cell1, cell2):
    return color(cell1) == color(cell2)

def color(cell):
    arr = [1,0,1,0,1,0,1,0]
    if cell[0] in ['B', 'D', 'F', 'H']:
        arr = arr[::-1]
    return arr[int(cell[1]) - 1]
