def solution(A,K):
    if len(A)==0:
        return A
    k = k % len(A)
    return A[-k:] + A[:-k]