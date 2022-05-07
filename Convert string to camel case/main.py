import re
import numpy as np

def str_to_camel(text):
    idx_to_capitalize = re.finditer("-|_", text)
    text = text.replace("-", "")
    text = text.replace("_", "")
    idx = [x.start() for x in idx_to_capitalize]

    for x in range(len(idx)):

        init_idx = idx[0]

        if x == 0:

            text = text[:idx[0]] + text[idx[0]].upper() + text[idx[0] + 1:]
        else:
            idx_adj = idx[x] - x

            text = text[:idx_adj] + text[idx_adj].upper() + text[idx_adj + 1:]

    return (text)