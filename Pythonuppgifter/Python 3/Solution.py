# Scaffold for solution to DIT873 / DAT346, Programming task 3

def sublist(s_list):
    list = []
    lista = []

    if len(s_list) <= 1:
        yield [s_list]
    if len((dict.fromkeys(s_list))) == 1:
        yield [[s_list[0]]]

    for i in range(1, len(s_list)):
        list.append(s_list[i-1])
        lista = lista[:] + [[elem for elem in list]]
        
        if s_list[i-1] > s_list[i]:
           list = []

    yield lista

def longest_common_list(s_list):
    
    list = [ elem for elem in next(sublist(s_list)) ]
    revlist = [ elem for elem in next(sublist(s_list[::-1])) ]

    resultlist = [elem for elem in list for elem in revlist if elem in list]

    return max(resultlist, key = len, default=[])
    

if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]
    assert longest_common_list([2,1,1,2,3,1,7,5,4,3,0,0,3,2,1,1]) == [1,1, 2, 3]
    assert longest_common_list([1,2,3,4,5,4,3,2,1]) == [1,2,3,4,5]
    assert longest_common_list([1,2,3,4,0,3,2,1]) == [1,2,3]
    assert longest_common_list([9,9,9,9,9,9,9,9,9]) == [9]
    assert longest_common_list([1,2,3,4,5,6,7,8]) == []
    assert longest_common_list([1]) == [1]
    assert longest_common_list([]) == []

