# encoding:utf-8
import numpy as np



def getEmbedding(infile_path="embedding"):
    row_index = 0
    with open(infile_path, "rb") as infile:
        for row in infile:
            row = row.strip()
            row_index += 1
            if row_index == 1:
                num_chars = int(row.split()[0])
                emb_dim = int(row.split()[1])
                emb_matrix = np.zeros((num_chars, emb_dim))
                continue
            items = row.split()
            char = items[0]
            emb_vec = [float(val) for val in items[1:]]
            emb_matrix[row_index-2] = emb_vec
    return emb_matrix
