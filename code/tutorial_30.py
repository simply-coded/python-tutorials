names = ['mark', 'nia', 'kate', 'jenny', 'kate']
scores = [90, 80, 65, 87, 90, 60, 68, 78, 91, 90, 63, 64]

n = 3
val = 90

def nth_index(lst, occur, search_for):            
    curr_i = 0
    for x in range(occur):
        curr_i = lst.index(search_for, curr_i)
        index = curr_i
        curr_i += 1


nth_index(scores, n, val)
nth_index(names, 2, 'kate')
