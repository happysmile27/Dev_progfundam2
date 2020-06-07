# import numpy as np

# identity_matrix = np.identity(7)
# print(identity_matrix)


def create_identity_matrix(n):
    id_matrix = []
    for i in range(n):
        row_list = []
        for j in range(n):
            if i == j:
                row_list.append(1)
            else:
                row_list.append(0)
            id_matrix.append(row_list)
        print(row_list)
create_identity_matrix(7)
