# Scaffold for solution to DIT873 / DAT346, Programming task 2


def encode_list(s_list):
    
    #Appending this so that the last "true" n in the for-loop gets counted aswell
    s_list.append('')
    aTuple = [s_list[0], 0]
    for n in s_list:
        if n == aTuple[0]:
            aTuple[1] += 1
        else:
            yield [aTuple[0], aTuple[1]] #Seems to be problem with some reference if just aTuple itself is returned
            aTuple[0] = n
            aTuple[1] = 1


def create_list (s_list):
    # returns the run-length encoded list
    encoded_list=[]
    # Your code below
    encoded_list = [aTuple for aTuple in encode_list(s_list)]
    return encoded_list


# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]
    assert create_list([1,1,1,1,1,1, 2,2,2,2, 3, 4,4,4,4,4,4,4,4,4,4, 5, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, 7, 5]) == [[1, 6], [2, 4], [3, 1], [4, 10], [5, 1], [1, 15], [7, 1], [5, 1]]
    assert create_list(['1', '1', '1', '2', '3', '3', '4', '4', '5', '1','1','7','5']) == [['1', 3], ['2', 1], ['3', 2], ['4', 2], ['5', 1], ['1', 2], ['7', 1], ['5', 1]]
    assert create_list(['a', 'a', 'a', 'b', 'c', 'c', 'd', 'd', 'e', 'a', 'a', 'g', 'e']) == [['a', 3], ['b', 1], ['c', 2], ['d', 2], ['e', 1], ['a', 2], ['g', 1], ['e', 1]]
    assert create_list([]) == []


