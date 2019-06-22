## Reverse Word Order

# Input a sentence of words and will output the words in reverse order.
def reverse_sentence(sentence:str):
    
    sentence = 'My name is Fahim'
    words = sentence.split()
    result = " ".join(words[::-1])
    print(result)
    
    
    ## Other way to do it
    ## Backward indexing using [::-1] is easier tho
    
    #list_words = []
    
    #for i in range(len(words)):
    #    list_words.append(words[len(words)-i-1])

    #result = " ".join(list_words)
    
    
