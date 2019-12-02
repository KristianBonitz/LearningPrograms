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

    if re.search(r"\(;", input_string) == None:
        raise ValueError("Incorrect Value")

    # divide into branches based on (; & )
    input = re.split(r"(\(;|\)|;)", input_string)

    result, lenght = create_branch(input)
    return result

# confirm elements with: 
def is_valid_property(input):
    return re.match(r"[A-Z]+(\[\w+\])+", input)

def create_properties(property_string):
    properties = {}
    key = ''
    value = []

    property_array = re.split(r"(\[\w+\])", property_string)

    for item in property_array:
        if item == '':
            pass
        elif '[' in item:
            value.append(item.strip('[]'))
        elif key != '':
            #complete property
            properties[key] = value
            #start new property
            key = item
            value = []
        else:
            key = item
    
    properties[key] = value
    return properties

def create_branch(input_array, pos=2):
    properties = {}
    children = []
    #step through input, generating properties and children as needed.
    while pos < len(input_array) and input_array[pos] != ')':
        value = input_array[pos]
        if value == '':
            pass

        elif ';' in value:
            #create child, move pos 1 space.
            child, pos = create_branch(input_array, pos+1)
            children.append(child)

        elif is_valid_property(value):
            properties = create_properties(value)

        else:
            raise ValueError(value, "is invalid value")

        pos += 1

    print(properties, children)
    if children == []:
        return SgfTree(properties), pos
    else:
        return SgfTree(properties, children), pos 

# Get input
# read first ';'
# break at second ';'
# take each key with their value and create a property value from it