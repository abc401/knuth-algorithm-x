from copy import deepcopy


def exact_cover(subsets: list, elements: list):
    # Calculate matrix for knuth x
    matrix = {
        element: [subset for subset in subsets if element in subset]
        for element in elements
    }
    return knuth_x(matrix)


def knuth_x(matrix: dict, partial_solution: list = [], solutions: list = []):
    '''
    matrix: A dictionary whose keys are the elements of the sets,
        and whose values are the subsets that contain the specific element in them
        
    partial_solution: The subset that have yet been included in the solution set    
    '''
    if not matrix:
        solutions.append(partial_solution.copy())
        print(f'Solution Found: {partial_solution}')
        return solutions
    
    selected = min(matrix, key=lambda x: len(matrix[x]))
    if not matrix[selected]:
        return solutions
    
    for subset in matrix[selected]:
        matrix_copy = deepcopy(matrix)
        remove_subset(matrix_copy, subset)

        partial_solution.append(subset)
        knuth_x(matrix_copy, partial_solution, solutions)
        partial_solution.pop(-1)
    
    return solutions


def combine_solutions(current_solution: list, subset_solutions: list[list]):
    return [current_solution + subset_solution for subset_solution in subset_solutions]
    

def remove_element(matrix: dict, element: str):
    matrix.pop(element)    
    for m_element in matrix:
        matrix[m_element] = [subset for subset in matrix[m_element] if element not in subset]


def remove_subset(matrix: dict, subset: set):
    for s_element in subset:
        remove_element(matrix, s_element)    


def main(filename: str, required_len: int = 5):
    subsets = [
        [1, 4, 7],
        [1, 4],
        [4, 5, 7],
        [3, 5, 6],
        [2, 3, 6, 7],
        [2, 7],
        [1, 4],
    ]
    elements = [1, 2, 3, 4, 5, 6, 7]
    sol_set = exact_cover(subsets, elements)
    print(sol_set)


if __name__ == '__main__':
    main('wordlist.txt')