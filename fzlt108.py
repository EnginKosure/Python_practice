# Create a function that returns the whole of the first sentence
# which contains a specific word. Include the full stop at the end of the sentence.

txt = "I have a cat. I have a mat. Things are going swell."


def sentence_searcher(t, w):
    l = t.lower()
    arr = t.split('.')
    # print(arr)
    for i in arr.lower():
        if i.find(w.lower()) != -1:
            print(i)
            return i
        else:
            return ''


# sentence_searcher(txt, "have")  # "I have a cat."

sentence_searcher(txt, "MAT")  # "I have a mat."

sentence_searcher(txt, "things")  # "Things are going swell."

sentence_searcher(txt, "flat")  # ""
