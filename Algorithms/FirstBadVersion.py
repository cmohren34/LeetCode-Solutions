def first_bad_version(n: int) -> int:
    # list becomes from 1 to n, b/c n is the first bad version
    low = 1
    high = n

    # normally you would do <= but in this case if it is equal then that is the answer
    while low < high:
        mid = (low + high) // 2

        if isBadVersion(low):
            return low

        if isBadVersion(mid):
            high = mid
        else:
            low = mid + 1

    # then the first bad version was the one given
    return low