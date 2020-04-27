# Scaffold for solution to DIT873 / DAT346, Programming task 3

def sublist(s_list):
    list = []
    lista = []
    len_s_list = len(s_list)

    if len_s_list <= 1:
        yield [s_list]
    if len((dict.fromkeys(s_list))) == 1:
        yield [[s_list[0]]]

    for i in range(1, len_s_list):
        
        if s_list[i-1] <= s_list[i]:
            list.append(s_list[i-1])
        else:
            list.append(s_list[i-1])
            lista.append(list)
            list = []

    yield lista

def longest_common_list(s_list):
    
    list = [ elem for elem in next(sublist(s_list)) ]
    revlist = [ elem for elem in next(sublist(s_list[::-1])) ]
    print(list)
    print(revlist)
    resultlist = [elem for elem in list for elem in revlist if elem in list]
    return max(resultlist, key = len)
    


# The following is called if you execute the script from the commandline
# e.g. with python Solution.py
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]
    assert longest_common_list([2,1,1,2,3,1,7,5,4,3,0,0,3,2,1,1]) == [1,1, 2, 3]
    assert longest_common_list([1,2,3,4,5,4,3,2,1]) == [1,2,3,4,5]
    assert longest_common_list([9,9,9,9,9,9,9,9,9]) == [9]
    assert longest_common_list([1]) == [1]
    assert longest_common_list([]) == []
