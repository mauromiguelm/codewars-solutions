import re
def solution(string, ending):
    return bool(re.search( r"({}$)".format(ending), string))
