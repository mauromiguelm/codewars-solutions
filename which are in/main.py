def in_array(array1, array2):
    return(sorted(list(set([x for x in array1 if any(x in word for word in array2)]))))