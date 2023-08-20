import paralleldots
paralleldots.set_api_key('GXpXOkuZq9sQGqJmnzzbTWZMZTMnrhQLdDISYrTVxB8')
def ner(text):
    ner = paralleldots.ner(text)
    return ner
