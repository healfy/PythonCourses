list1 = [1, 3, 6, 9]
def f(a, L=list1):
    for i in range(len(L)):
        if a == i :
            L.remove(a)
            return L
    L.append(a)
    return L

f(3)
f(3)