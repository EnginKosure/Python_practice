# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.

def pig_it(text):
    lst = text.split()
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])


pig_it('Pig latin is cool')  # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !


def pig_it1(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())
