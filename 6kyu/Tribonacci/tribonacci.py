def tribonacci(signature, n):
    if n <= 0:
        return []
    elif n > len(signature):
        [signature.append(signature[i-2] + signature[i-1] + signature[i]) for i in range(2, n-1)]
        return signature
    else:
        a = []
        [a.append(signature[i]) for i in range(0, n)]
        return a
