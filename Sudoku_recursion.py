"""Special thanks to Peter Norvig

http://norvig.com/sudopy.shtml
"""

def solve(values, squares_caller, dimension):
    squares = squares_list(squares_caller, dimension)
    unitlist = unitlist_maker(squares_caller, dimension)
    units = units_maker(unitlist, squares)
    peers = peers_maker(units, squares, dimension)
    return search(values, squares, units, peers)

def squares_list(squares_caller, dimension):
    squares = []
    for i in range(dimension**2):
        squares.extend(squares_caller[i])
    return squares

def unitlist_maker(squares_caller, dimension):
    temp_unit_list = []
    row_list = rowmaker(squares_caller, dimension)
    column_list = columnmaker(squares_caller, dimension)
    block_list = blockmaker(squares_caller, dimension)
    temp_unit_list.extend(row_list[:])
    temp_unit_list.extend(column_list[:])
    temp_unit_list.extend(block_list[:])
    return temp_unit_list

def rowmaker(squares_caller, dimension):
    rows_list = []
    for i in range(dimension**2):
        rows_list.append(squares_caller[i])
    return rows_list

def columnmaker(squares_caller, dimension):
    columns_list = []
    for i in range(dimension**2):
        temp_column = []
        for j in range(dimension**2):
            temp_column.append(squares_caller[j][i])
        columns_list.append(temp_column)
    return columns_list

def blockmaker(squares_caller, dimension):
    blocks_list = []
    for m in range(dimension):
        for n in range(dimension):
            temp_block = []
            rowstart = m*dimension
            columnstart = n*dimension
            for i in range(rowstart, rowstart+dimension):
                for j in range(columnstart, columnstart+dimension):
                    temp_block.append(squares_caller[i][j])
            blocks_list.append(temp_block)
    return blocks_list

def units_maker(unitlist, squares):
    units_dict = {}
    for index in squares:
        temp_unit_list = []
        for element in unitlist:
            if index in element:
                temp_unit_list.append(element)
        units_dict[index] = temp_unit_list
    return units_dict

def peers_maker(units, squares, dimension):
    peers_dict = {}
    for index in squares:
        templist = list(sum(units[index],[]))
        for i in range(dimension):
            templist.remove(index)
        for element in templist:
            if templist.count(element) > 1:
                templist.remove(element)
        peers_dict[index] = templist
    return peers_dict


def search(values, squares, units, peers):
    "Using depth-first search and propagation, try all possible values."
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in squares):
        return values ## Solved!
    ## Chose the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d, units, peers), squares, units, peers)
                for d in values[s])

def some(seq):
    "Return some element of seq that is true."
    for e in seq:
        if e: return e
    return False


def assign(values, s, d, units, peers):
    """Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected."""
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2, units, peers) for d2 in other_values):
        return values
    else:
        return False


def eliminate(values, s, d, units, peers):
    """Eliminate d from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected."""
    if d not in values[s]:
        return values ## Already eliminated
    values[s] = values[s].replace(d,'')
    ## (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
    if len(values[s]) == 0:
        return False ## Contradiction: removed last value
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2, units, peers) for s2 in peers[s]):
            return False
    ## (2) If a unit u is reduced to only one place for a value d, then put it there.
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False ## Contradiction: no place for this value
        elif len(dplaces) == 1:
            # d can only be in one place in unit; assign it there
            if not assign(values, dplaces[0], d, units, peers):
                return False
    return values

