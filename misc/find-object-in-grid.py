def getResponse(x,y):
    pass

def find_object_in_grid(grid):
    n,m = len(grid), len(grid[0])

    # finding column
    leftCol, rightCol = 0,m-1
    while leftCol < rightCol:
        getResponse(0, leftCol)
        midCol = (rightCol - leftCol) // 2 
        if getResponse(0, rightCol) == HOT:
            leftCol = midCol+1
        elif getResponse(0, rightCol) == COLD:
            rightCol = midCol
        elif getResponse(0, rightCol) == SAME:
            leftCol = rightCol = midCol
        elif getResponse(0, rightCol) == EXACT:
            return (0, rightCol)

    # finding row
    topRow, bottomRow = 0, n-1
    while topRow < bottomRow:
        getResponse(topRow, leftCol)
        midRow = (bottomRow - topRow) / 2 
        if getResponse(leftCol, bottomRow) == HOT:
            topRow = midRow+1
        elif getResponse(leftCol, bottomRow) == COLD:
            bottomRow = midRow
        elif getResponse(leftCol, bottomRow) == SAME:
            topRow = bottomRow = midRow
        elif getResponse(leftCol, bottomRow) == EXACT:
            return (bottomRow, leftCol)

    return getResponse(bottomRow, leftCol)
