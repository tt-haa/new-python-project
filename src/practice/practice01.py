def cumulative_sum(A):
    counter = [A[0]]
    i, f = 2, 1
    while f < len(A):
        counter.append(sum(A[f:(f+i)]))
        f += i
        i += 1
    return counter

A = [5,2,4,6,1,9,7,8,1,6,3,3,3,3,3,3]
print(cumulative_sum(A))
