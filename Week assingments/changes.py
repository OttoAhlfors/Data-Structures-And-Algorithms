def changes(A):
    changes = 0
    i = 0

    # Käydään läpi array A
    for i in range(1, len(A)-1):
        if A[i] == A[i - 1] and A[i] == A[i + 1]:
            A[i] = A[i +1] + A[i -1]
            changes += 1
    for i in range(1, len(A)-1):
        if A[i] == A[i + 1] or A[i] == A[i - 1]:
            A[i] = A[i + 1] + 1
            changes += 1
    return changes


if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))     # 2
    print(changes([1, 2, 3, 4, 5]))     # 0
    print(changes([1, 1, 1, 1, 1]))     # 2 