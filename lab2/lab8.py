C = {1, 2, 3, 4, 5}
F = {4, 5, 6, 7, 8}
S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
print("The students who play both sports is ", C.intersection(F))
print("The students who play only one sport are", C.symmetric_difference(F))
print("The students who play neither sports are", S.difference((C.union(F))))