def fib (limit) :
    #Return a fibonacci number
    previous = [0,1]
    i = 2
    while previous[i-1] + previous[i-2] < limit:
        yield previous[i-1] + previous[i-2]
        previous.append(previous[i-1] + previous[i-2])
        i+=1


def list_fib(limit) :
    # Construct a list of Fibonacci series
    list = [0,1]
    for i in fib(limit):
        list.append(i)
    return list


if __name__ == "__main__":
    assert (list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13])
    assert (list_fib(40) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    assert (list_fib(80) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
    assert (list_fib(160) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])
    assert (list_fib(440) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377])

