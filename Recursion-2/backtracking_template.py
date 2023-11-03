def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)

def find_solution(candidates):
    pass

def is_valid(candidates):
    pass

def place(candidates):
    pass

def remove(candidates):
    pass

def output(candidates):
    pass

list_of_candidates = list()