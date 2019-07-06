SCRABBLE_SCORING_GROUPS = [
    {'letters' : ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
     'score': 1},
    {'letters': ['D', 'G'],
     'score': 2},
    {'letters': ['B', 'C', 'M', 'P'],
     'score': 3},
    {'letters': ['F', 'H', 'V', 'W', 'Y'],
     'score': 4},
    {'letters': ['K'],
     'score': 5},
    {'letters': ['J', 'X'],
     'score': 8},
    {'letters': ['Z', 'Q'],
     'score': 10}
]
def score(word):
    word_value = 0
    for letter in word.upper():
        for group in SCRABBLE_SCORING_GROUPS:
            if letter in group['letters']:
                word_value += group['score']
                break

    return word_value