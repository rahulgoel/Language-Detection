import nltk
from nltk.corpus import PlaintextCorpusReader
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np
from scipy.sparse import coo_matrix
from sklearn.naive_bayes import MultinomialNB
from nltk import sent_tokenize,word_tokenize,porter
from sklearn import cross_validation
import pickle
def getCorpus (root):
    word_lists = PlaintextCorpusReader (root, '.*')
    lang_hash = {}
    for i in word_lists.fileids():
        [language, file_name] = i.split ('/')
        if language not in lang_hash:
            lang_hash [language] = [file_name]
        else:
            lang_hash[language].append (file_name)
    
    word_dic = {}
    for keys in lang_hash:
        file_list = lang_hash[keys]
        set_words = set()
        lis = []
        for lang_file in file_list:
            sentences = sent_tokenize( (word_lists.raw (keys + '/' +lang_file)))
            lis.extend(sentences)
        word_dic[keys] = lis

    return word_dic
    

def createNgram (dic):
    feat_dict = {}
    count_dict = {}
    count_vect = TfidfVectorizer (analyzer = 'char', ngram_range = (3,6), max_features = 15000)
    
    all_word_list = []
    l = 0
    y_train = np.zeros ((1,1))
    for keys in dic:
        all_word_list.extend (dic[keys])
        class_labels = np.zeros ((len (dic [keys]), 1))
        class_labels[:] = l
        
        y_train = np.concatenate ((y_train, class_labels))
        l = l + 1
    y_train = y_train[1:]
    y_train = coo_matrix(y_train)
    x_train = count_vect.fit_transform (all_word_list)
    count_dict[keys] = count_vect
    return x_train, y_train, count_vect
    

def trainClassifier (x_train, y_train):
    clf = MultinomialNB().fit(x_train, y_train)
    return clf

def testClassifierScore (classifier, x_test, y_test):
    return classifier.score(x_test,y_test)

def testClassifier (classifier, x_test, count_vect, names):
    x_test_counts = count_vect.transform(x_test)
    predicted = classifier.predict(x_test_counts)
    out_list = predicted.tolist()
    names = map(lambda x : names[int(x)], out_list)
    prob = classifier.predict_proba (x_test_counts)
    lang_prob = map (lambda x : max(x), prob)
    return zip(names, lang_prob)
 
def refresh():
    corpus_root =  './europarl_raw/'   
    corpus = getCorpus (corpus_root)
    names = corpus.keys()
    b = createNgram (corpus)
    del corpus
    count_vect = b[2]
    classifier = trainClassifier (b[0] , np.ravel(b[1].toarray()))
    del b
    f = open('classifier.pickle', 'wb')
    pickle.dump((classifier, count_vect, names), f)
    f.close()

    predicted = testClassifier (classifier, ["Le parole est l\u0027ombre du fait","lorem ipsum"], count_vect, names)
    print predicted
