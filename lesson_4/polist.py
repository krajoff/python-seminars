def polist(pol):
    for idx in range(0, len(pol)):
        if 'x' in pol[idx]:
            idx_mul = pol[idx].index('*')
            if pol[idx][idx_mul + 3:]:
                pol[idx] = [int(pol[idx][0:idx_mul]), int(pol[idx][idx_mul + 3:])]
            else:
                pol[idx] = [int(pol[idx][0:idx_mul]), 1]
        else:
            pol[idx] = [int(pol[idx]), 0]
    return pol
