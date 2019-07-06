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

#### 28 May -- Unable to figure out how to handle escaped characters.
#### Will now try and start cleaning up the script a bit more with better up front handling.

def parse(input_string):
    # Split on capturing (; or [\w*]
    # checking that it is in the format ;key[value]

    # does input handle both: re.match(r";*[A-Z]+(\[\w+\])+")
    # and re.split(r"([\(\)\;\[\]])", input_string)

    input = re.split(r"(?<!\\)([\(\)\;\[\]])", input_string)
    #print(input)
    result, lenght = assemble(input)
    return result
    
    
def assemble(input_array, pos=4):
    properties = {}
    children = []
    key = ''
    value = []

    while pos < len(input_array) and ')' not in input_array[pos]:

        if ';' in input_array[pos]: #loop to allow for more children
            pos += 1
            child, pos = assemble(input_array, pos)
            children.append(child)

        elif '[' in input_array[pos]: #is value
            pos += 1
            value.append( input_array[pos] )

        elif input_array[pos] == '' or  re.match(r"(?<!\\)[\(\)\]\[]", input_array[pos]):
            pass

        elif re.match(r"^[A-Z]*$", input_array[pos]): #is key
            if key != '':
                properties[key] = value
                value = [];

            key = input_array[pos]

        else:
            print(input_array[pos])
            raise ValueError(input_array[pos], "contains invalid characters")
        pos += 1

    if len(value) == 0:
        raise ValueError(key, "does not have any values")
    properties[key] = value
    print(properties, children)
    
    if properties == {'':[]}:
        raise ValueError(input_array, "is invalid")
    elif children == []:
        return SgfTree(properties), pos
    else:
        return SgfTree(properties, children), pos

# Get input
# read first ';'
# break at second ';'
# take each key with their value and create a property value from it
#FF[4]D[22];CC[32])")

#TEST CASES
parse("(;FF[4]E[22][RR](;EF[23])(;EG[22]))")
parse("(;A[\\]b\nc\nd\t\te \n\\]])")
#parse("(;Aa[b])")

