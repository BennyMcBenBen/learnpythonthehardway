lexicon = {
    "north" : "direction",
    "south" : "direction",
    "east" : "direction",
    "west" : "direction",
    "go" : "verb",
    "stop": "verb",
    "kill": "verb",
    "eat": "verb",
    "the": "stop",
    "in": "stop",
    "of": "stop",
    "from": "stop",
    "at": "stop",
    "it": "stop",
    "door": "noun",
    "bear": "noun",
    "princess": "noun",
    "cabinet": "noun"
}

def get_word_tuple(word):
    """ 
    Returns a (word_type, word) tuple for the specified word. If word is not
    found in the lexicon and not a number, the word type returned is 'error'.
    """
    if word.lower() in lexicon:
        return (lexicon[word.lower()], word)
    else:
        try:
            return ('number', int(word))
        except ValueError:
            return ('error', word)

def scan(sentence):
    """
    Returns a (word_type, word) tuple for each word in sentence.
    """
    words = sentence.split()
    return [get_word_tuple(word) for word in words]
    
