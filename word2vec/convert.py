with open('metadata.tsv','w') as F:
    F.write('word\tindex\n')
    with open('word_embedding','r') as f:
        row_index = 0
        for row in f:
            row = row.strip()
            row_index += 1
            if row_index == 1:
                num_chars = int(row.split()[0])
                emb_dim = int(row.split()[1])
                continue
            items = row.split()
            char = items[0]
            emb_vec = [float(val) for val in items[1:]]
            F.write(char+'\t'+str(row_index-2)+'\n')
