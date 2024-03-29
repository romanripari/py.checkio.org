from itertools import chain
def flat_list(array):
    res = []
    def flar_lista_aux(array):
        for a in array:
            if isinstance(a, list):
                flar_lista_aux(a)
            else:
                res.append(a)
    flar_lista_aux(array)
    return res

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')