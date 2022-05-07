import math
def is_square(n):
    try:
        m = math.sqrt(n)
        return int(m)==float(m)
    except Exception:
        return False