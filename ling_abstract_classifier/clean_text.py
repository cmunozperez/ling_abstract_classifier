import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')

def clean_text_stem(string_of_text):
    '''
    A function that takes a string of text and return a stemmed string, without stop words.

    Parameters
    ----------
    string_of_text (str): A text to clean

    Returns
    -------
    A String (str)

    '''
    
    #This instantiates the stemmer
    stemmer = PorterStemmer()

    #This tokenizes the text
    words = nltk.word_tokenize(string_of_text)

    # This removes stopwords
    stop_words = set(stopwords.words('english'))
    no_stop_words = [word for word in words if word.lower() not in stop_words]

    # Apply stemming to each word
    stemmed_words = [stemmer.stem(word) for word in no_stop_words]

    # Join the stemmed words back into a string
    stemmed_text = ' '.join(stemmed_words)
    
    return stemmed_text

def clean_text_lemma(string_of_text):
    '''
    A function that takes a string of text and return a lemmatized string, without stop words.

    Parameters
    ----------
    string_of_text (str): A text to clean

    Returns
    -------
    A String (str)

    '''
    
    #This instantiates the lemmatizer
    lemmatizer = WordNetLemmatizer()

    #This tokenizes the text
    words = nltk.word_tokenize(string_of_text)

    # This removes stopwords
    stop_words = set(stopwords.words('english'))
    no_stop_words = [word for word in words if word.lower() not in stop_words]

    # This applies lemmatization to each word
    lemmatized_words = [lemmatizer.lemmatize(word) for word in no_stop_words]

    # This rejoins text back into a string
    lemmatized_text = ' '.join(lemmatized_words)
    
    return lemmatized_text

def lemmatize(string_of_text):
    '''
    A function that takes a string of text and returns a lemmatized string.

    Parameters
    ----------
    string_of_text (str): A text to lemmatize

    Returns
    -------
    A String (str)

    '''
    
    #This instantiates the lemmatizer
    lemmatizer = WordNetLemmatizer()

    #This tokenizes the text
    words = nltk.word_tokenize(string_of_text)

    # This applies lemmatization to each word
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

    # This rejoins text back into a string
    lemmatized_text = ' '.join(lemmatized_words)

    return lemmatized_text

#prueba_lemma = lemmatize('Is language universal? In particular, is the grammar—the computational system in the mind/brain—that powers human language universal? Could it be universal in the way laws of nature are universal such that any sufficiently intelligent system would all but inevitably converge on it (in either its evolution or its science)? Here we will expound on the conjecture that the answers to these questions are affirmative: grammar—particularly human grammar—is not specific to our species, but universal in the deepest of senses. The implications for xenolinguistics are obviously profound: we should predict that any extraterrestrial intelligence (ET)—indeed any sufficiently intelligent system—we encounter would likely be endowed with a cognitive computational system that runs human-style linguistic “software”, thus eliminating any principled limit to effective communication. However, there would likely be significant differences in the “hardware” used to physically externalize linguistic information, but these would pose mere engineering problems rather than conceptual ones. Indeed, it is not unreasonable to think that the combined intelligence of humans and ETs could overcome these. In that case, effective communication between these “universal minds” would be guaranteed.')

