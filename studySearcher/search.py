# searches the dataset for matches


def clean(text):
    """
    returns a list of words, from text, removing unnecessary punctuation and
    stopwords
    """
    from stopwords import stopwords
    import string
    
    # trimming stopwords:
    stops = stopwords()
    ret = [word for word in text.split() if (word not in stops) and len(word) > 1]
    
    # trimming punctuation:
    punc = string.punctuation
    for i in range(len(ret)):
        og = ret[i]
        if  og[0] in punc: og = og[1:]
        if og[-1] in punc: og = og[:-1]
        ret[i] = og
        
    return ret
    

def similarity_score(text_small, text_large, min_small = 10, min_large = 50):
    """
    complexity: len(small) * len(large)
    @param text_small: the smaller text 
                       (in this case the text which's validity is being checked)
    @param text_large: the larger text (in this case the scientific study)
    
    returns: a number (-1 <= n <= 100) representing the similarity
             -1 if the data isn't populated enough for reliability
    """

    # cleaning text:    
    filtered_small = clean(text_small)
    filtered_large = clean(text_large)
    
    fSmallLen = len(filtered_small)
    fLargeLen = len(filtered_large)
    
    if (fSmallLen < min_small) or (fLargeLen < min_large): return -1
    
    max_rating = fLargeLen * fSmallLen
    hits = 0
    for sm_word in filtered_small:
        for big_word in filtered_large:
            if sm_word == big_word: hits += 1
    return 100. * hits / max_rating
    
