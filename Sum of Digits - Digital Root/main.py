def digital_root(n):
    #recursive solution to iterate over digital_root
    sum_n = sum([int(x) for x in str(n)])
    return(sum_n if len(str(sum_n)) <2 else digital_root(sum_n))