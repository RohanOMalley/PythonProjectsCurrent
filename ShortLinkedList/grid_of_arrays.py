

def grid_of_arrays():
    bottom = [[ [None, (2,2), None], (1,2), None] , (0,2) ,None]
    middle = [[[None, (2,1), bottom[0][0]],(1,1),bottom[0]], (0,1), bottom]
    top = [[[None, (2,0), middle[0][0]],(1,0),middle[0]],(0,0), middle]

    return top
