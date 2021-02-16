# The Naive String Matching Algorithm
def naive(pattern, text):
    assert len(pattern) <= len(text)
    occurrences=[]
    for i in range(0, len(text)-len(pattern)+1):
        matching = True
        for j in range(0, len(pattern)):
            if text[i+j] != pattern[j]:
                matching = False
                break
                if matching:
                    occurrences.append(i)
                    return occurrences




