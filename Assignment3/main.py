A = [0.5, 0.2, 0, 0.9, 0]
B = [1, 0, 0.1, 0.5, 0.5]


def suma(A, B):
    return [max(e) for e in zip(A, B)]


def przekroj(A, B):
    return [min(e) for e in zip(A, B)]


def dopelnienie(A):
    return [1 - e for e in A]


print("A: {0}".format(A))
print("B: {0}".format(B))
print("Suma: {0}".format(suma(A, B)))
print("Przekroj: {0}".format(przekroj(A, B)))
print("Dopelnienie A: {0}".format(dopelnienie(A)))
print("Dopelnienie B: {0}".format(dopelnienie(B)))
