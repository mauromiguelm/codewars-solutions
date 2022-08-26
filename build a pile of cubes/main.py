def find_nb(m):
    init_vol = 0
    count = 0
    while init_vol < m:
        count += 1
        init_vol += count ** 3
    return(count if init_vol==m else -1)