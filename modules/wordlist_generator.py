import itertools

def generate_wordlist(chars, length=4):
    wordlist = [''.join(i) for i in itertools.product(chars, repeat=length)]
    return wordlist
