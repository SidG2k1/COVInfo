# searches the dataset for matches




def similarity_score(text_small, text_large, min_small = 30, min_large = 100):
    """
    complexity: len(small) * len(large)
    @param text_small: the smaller text 
                       (in this case the text which's validity is being checked)
    @param text_large: the larger text (in this case the scientific study)
    returns: a number (-1 <= n <= 100) representing the similarity
    """

    # cleaning text:
    from stopwords import stopwords
    stops = stopwords()
    small_words = text_small.split()
    large_words = text_large.split()
    
    filtered_small = [word for word in small_words if word not in stops]
    filtered_large = [word for word in large_words if word not in stops]
    
    fSmallLen = len(filtered_small)
    fLargeLen = len(filtered_large)
    
    if (fSmallLen < min_small) or (fLargeLen < min_large): return -1
    
    max_rating = fLargeLen * fSmallLen
    hits = 0
    for sm_word in filtered_small:
        for big_word in filtered_large:
            if sm_word == big_word: hits += 1
    return 100. * hits / max_rating
    
