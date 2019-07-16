SCRABBLE_SCORING_GROUPS = {  
    # Letter : Value
    'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 
    'R':1, 'S':1, 'T':1, 'D':2, 'G':2, 'B':3, 'C':3, 
    'M':3, 'P':3, 'F':4, 'H':4, 'V':4, 'W':4, 'Y':4,
    'K':5, 'J':8, 'X':8, 'Z':10, 'Q':10
}

def score(word):
    return sum(map(letter_value, word.upper()))

def letter_value(char, scoring_group=SCRABBLE_SCORING_GROUPS):
    # return value of character
    if char in scoring_group: 
        return scoring_group[char] 
    else: 
        return 0