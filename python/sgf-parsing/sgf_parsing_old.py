import re

class SgfTree(object):
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    input = re.split(r"(\(\;|\[\w*\])", input_string)
    print(input)
    m = re.search(r"(\w*)\[(\w*)\]", input_string)

    if m:
        #print (input_string, f'{m.group(1)}:[{m.group(2)}]')
        return(SgfTree({m.group(1):[m.group(2)]}))
    else:
        raise ValueError("File format incorrect");

# Get input
# read first ';'
# break at second ';'
# take each key with their value and create a property value from it
# parse("(;FF[4]D[22];CC[32])")
parse("(;FF[4]E[22][RR](;EF[23])(;EG[22]))")