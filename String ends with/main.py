import re
def solution(string, ending):
    return bool(re.search( r"({}$)".format(re.escape(ending)), re.escape(string)))