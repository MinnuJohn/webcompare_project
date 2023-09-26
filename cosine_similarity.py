"""program to compare two strings using consine similarity logic"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
def compare(X,Y):
    # conver above strins to lower
    x = X.lower()
    y = Y.lower()

    # Tokenize the input strings and remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    x_list = word_tokenize(x.translate(translator))
    y_list = word_tokenize(y.translate(translator))

    # creating list of stopwords(ex:“the”, “a”, “an”,)
    list_stop_words = stopwords.words('english') 

    # two empty words to create list to words
    list_1 =[]
    list_2 = []

    # remove stop words from the string x and y
    x_set = {w for w in x_list if not w in list_stop_words} 
    y_set = {w for w in y_list if not w in list_stop_words}

    # form a set containing keywords of both strings 
    rvector = x_set.union(y_set) 
    for w in rvector:
        if w in x_set: 
            list_1.append(1) # create a vector
        else: 
            list_1.append(0)
        if w in y_set:
            list_2.append(1)
        else: 
            list_2.append(0)
    c = 0

    # cosine formula 
    for i in range(len(rvector)):
            c+= list_1[i]*list_2[i]
    cosine =int( (c / float((sum(list_1)*sum(list_2))**0.5))*100)
    return cosine
